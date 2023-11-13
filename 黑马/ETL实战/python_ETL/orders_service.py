
from model.orders.OrdersDetailModel import OrdersDetailModel
from model.orders.OrdersModel import OrdersModel
from model.orders.RetailOriginJsonModel import RetailOriginJsonModel
from model.orders.SingleProductSoldModel import SingleProductSoldModel
from util import mysql_util
from config import projrct_config as conf
import time
from util import logging_util
from util import file_util
import datetime


# =============================== 元数据库 =========================================
# 创建数据库连接对象
metadata_util = mysql_util.get_mysql_util()

# 创建日志对象
logger = logging_util.init_logger('order_metadata')


# 判断元数据表是否存在，若不存在，则创建
metadata_util.check_table_exists_and_create(
    db_name=conf.metadata_db,
    tb_name=conf.file_monitor_meta_table_name,
    tb_cols=conf.file_monitor_meta_table_create_cols
)


# 获取所有要采集的json文件的列表
all_json_list = file_util.get_dir_files_list(conf.json_origin_path)

# 获取已经采集的json文件列表
processed_json_list = []
# 通过查询元数据表获取
sql = f"select file_name from {conf.file_monitor_meta_table_name}"
# 执行sql
result =  metadata_util.query(sql)

# 将查询结果放入列表中
processed_json_list = [file_path[0] for file_path in result]

# 获取未采集的json文件列表
new_json_list = file_util.get_new_by_compare_lists(processed_json_list,all_json_list)

# =============================== 目标数据库 =======================================
# 创建数据库连接对象
target_conn = mysql_util.get_mysql_util()

# 创建日志对象
logger = logging_util.init_logger('orsdes_target')

# 创建CSV文件(订单+订单详情+单个商品销售表)
csv_orders_file = open(conf.retail_output_csv_root_path + conf.retail_orders_output_csv_file_name,'a',encoding='utf8')
csv_orders_detail_file = open(conf.retail_output_csv_root_path + conf.retail_orders_detail_output_csv_file_name,'a',encoding='utf8')
# csv_single_product_sold_file = open(conf.retail_output_csv_root_path + conf.retail_singleproduct_sold_output_csv_file_name,'a',encoding='utf8')

# 写入CSV文件表头(订单+订单详情+单个商品销售表)
csv_orders_file.write(OrdersModel.generate_csv_header())
csv_orders_detail_file.write(OrdersDetailModel.generate_csv_header())
# csv_single_product_sold_file.write(SingleProductSoldModel.generate_csv_header())


# 检查表是否存在，若不存在则创建
# 订单表
target_conn.check_table_exists_and_create(
    db_name=conf.target_db,
    tb_name=conf.target_orders_table_name,
    tb_cols=conf.target_orders_table_cols_name
)

# 订单详情表
target_conn.check_table_exists_and_create(
    db_name=conf.target_db,
    tb_name=conf.target_orders_detail_table_name,
    tb_cols=conf.target_orders_detail_table_cols_name
)

# # 单个商品售卖表
# target_conn.check_table_exists_and_create(
#     db_name=conf.target_db,
#     tb_name=conf.target_singleproduct_sold_table_name,
#     tb_cols=conf.target_singleproduct_sold_table_cols_name
# )

# 对json文件进行采集
start_time = time.time()
for json_file in new_json_list:
    count_lines = 0
    # 开启事务
    target_conn.start_transaction()
    try:
        for row in open(json_file,'r',encoding='utf8'):
            
            count_lines += 1
            # 创建数据模型
            retailmodel = RetailOriginJsonModel(row)
            
            # 生成插入数据的sql
            order_sql = retailmodel.order_model.generate_insert_sql()
            order_detail_sql = retailmodel.order_detail_model.generate_insert_sql()
            # singleproduct_sold_sql = retailmodel.generate_insert_sql()
            
            # 执行插入sql语句
            target_conn.insert_single_sql_without_commit(order_sql)
            target_conn.insert_single_sql_without_commit(order_detail_sql)
            # target_conn.insert_single_sql_without_commit(singleproduct_sold_sql)
            
            # 生成插入CSV语句
            order_to_csv = retailmodel.order_model.generate_csv_str()
            order_detail_to_csv = retailmodel.order_detail_model.generate_csv_str()
            # singleproduct_sold_to_csv = retailmodel.order_model.generate_csv_str()
            
            # 插入csv目标表中
            csv_orders_file.write(order_to_csv)
            csv_orders_detail_file.write(order_detail_to_csv)
            # csv_single_product_sold_file.write(singleproduct_sold_to_csv)
        
    except Exception as e:
        # 添加日志
        logger.error(f"目标json文件{json_file}任务执行失败，事务回滚了！")
        # 回滚事务
        target_conn.rollback_transaction()
        raise e
    else:
        # 提交事务
        target_conn.commit_transaction()
        
        # 添加日志
        logger.info(f"目标json文件{json_file}已经采集完毕！")
        
    # 将已处理的文件插入元数据表中，进行标记，防止重复采集
    # 定义插入数据sql
    sql = f'insert into {conf.file_monitor_meta_table_name}(file_name,process_lines,process_time) values("{json_file}",{count_lines},"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")'

    # print(sql)
    # 选择数据库
    metadata_util.select_db(conf.metadata_db)

    # 执行sql,插入已处理的数据信息
    metadata_util.insert_single_sql(sql)
    
# 结束时间
end_time = time.time()
logger.info(f'本次总共采集了{len(new_json_list)}个文件，本次采集共消耗了{end_time-start_time}s')

metadata_util.close()
target_conn.close()
csv_orders_file.close()
csv_orders_detail_file.close()  
            
            

