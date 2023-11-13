from util import mysql_util
from config import projrct_config as conf
from model.barcode_model import BarcodeModel
import time
from util import logging_util

# 创建数据库连接对象
metadata_util = mysql_util.get_mysql_util()

# 创建日志对象
logger = logging_util.init_logger('barcode')

# 检查元数据表是否存在，若不存在，则创建
metadata_util.check_table_exists_and_create(
    conf.metadata_db,
    conf.metadata_barcode_table_name,
    conf.metadata_barcode_table_create_cols
)

# 查询商品采集元数据表中，上次采集记录的updateAt 的最大值 
sql = f"select max(time_record) from {conf.metadata_barcode_table_name}"
result = metadata_util.query(sql)

# 判断取到的数据集是否有值，创建变量保存该值
if result[0][0]:
    barcode_max_time = result[0][0]
else:
    barcode_max_time = None

# print(barcode_max_time)

# ======根据上次采集商品数据中 updateAt 的最大值，查询数据源库商品表，继上次采集后，新增的数据======
# 创建数据库连接
source_util = mysql_util.get_mysql_util()

# 判断表是否存在
if not source_util.check_table_exists(conf.source_db, conf.source_barcode_table_name):
    # 如果不存在，则退出程序
    exit('很抱歉，您要采集的数据表不存在，请联系后端管理员！')
    # 如果不存在则退出程序
    logger.critical(f'{conf.source_db}数据库中的{conf.source_barcode_table_name}不存在！！！')

# 查询源数据库表，获取更新的商品信息
if not barcode_max_time:
    # 没有最大采集时间时，进行全量采集
    sql = f"select * from {conf.source_barcode_table_name} order by updateAt"
else:
    # 有最大采集时间时，进行增量采集，仅采集最大采集时间之后的数据
    sql = f"select * from {conf.source_barcode_table_name} where updateAt > '{barcode_max_time}' order by updateAt"

result = source_util.query(sql)

# 判断采集的数据条目数量
if not len(result):
    exit('很抱歉，您要采集的数据条目为0，自动退出程序！')

# print(result)

# ======================将采集到的数据写入数据仓库或CSV文件中========================
# 创建数据库连接
target_util = mysql_util.get_mysql_util()

# 检查目标表是否存在，若不存在则创建
target_util.check_table_exists_and_create(
    conf.target_db,
    conf.target_barcode_table_name,
    conf.target_barcode_table_create_cols
)

# 创建目标csv文件
csv_file = open(conf.barcode_output_csv_root_path + conf.barcode_orders_output_csv_file_name, 'a')
# 写入csv表头信息
csv_file.write(BarcodeModel.generate_csv_header())

target_util.start_transaction()
data_count = 0
start_time = time.time()
# 创建数据采集结果模型
for row in result:
    data_count += 1
    # 开启事务
    try:
        # target_util.start_transaction()
        # 写入数据仓库
        model = BarcodeModel(row)
        target_util.insert_single_sql_without_commit(model.generate_insert_sql())

        # 写入CSV文件
        csv_file.write(model.generate_csv_str())

    except Exception as e:
        # 回滚事务
        target_util.rollback_transaction()
        raise e
    else:
        if data_count % 1000 == 0:
            # 提交事务
            target_util.commit_transaction()
            # 事务提交后，还需要把上一次的最大采集时间写入到元数据表中
            sql = f"insert into {conf.metadata_barcode_table_name}(time_record, gather_line_count) values ('{model.updateAt}',1000)"
            metadata_util.insert_single_sql(sql)
            # 再次开启事务
            target_util.start_transaction()
else:
    target_util.commit_transaction()
    sql = f"insert into {conf.metadata_barcode_table_name}(time_record, gather_line_count) values ('{model.updateAt}',{data_count % 1000})"
    metadata_util.insert_single_sql(sql)

    print('数据已经全部采集完成！')
    
end_time = time.time()
logger.info(f'本次采集一共花费了{end_time - start_time}s时间，总共采集了{data_count}条记录！')

# 关闭连接
csv_file.close()
target_util.close()
source_util.close()
