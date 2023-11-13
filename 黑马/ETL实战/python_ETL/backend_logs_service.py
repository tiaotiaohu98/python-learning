from datetime import datetime
from venv import logger
from model.backend_logs_model import BackendLogModel
from util import file_util
from util import mysql_util
from config import projrct_config as conf
import time
from util import logging_util

# 创建日志对象
logger = logging_util.init_logger('backend_logs')

# 1、获取后台访问日志文件夹下有哪些日志文件
all_file_list = file_util.get_dir_files_list(conf.backend_logs_data_root_path)

# 2、查询元数据库表中已经采集的日志文件，用来对比要采集的新的访问日志文件

# 创建元数据库连接
metadata_util = mysql_util.get_mysql_util()

# 获取已经被采集的日志文件
processed_file_list = mysql_util.get_processed_files(
    util=metadata_util,
    db_name=conf.metadata_db,
    tb_name=conf.logs_monitor_meta_table_name,
    tb_cols=conf.logs_monitor_meta_table_create_cols
)

# 对比要采集的日志文件
new_file_list = file_util.get_new_by_compare_lists(processed_file_list,all_file_list)

# 3、进行日志数据采集
csv_file = open(conf.logs_output_csv_root_path + conf.logs_output_csv_file_name, 'a')
# 向csv文件中写入表头
csv_file.write(BackendLogModel.generate_csv_header())

# 创建数据库连接
target_util = mysql_util.get_mysql_util()
target_util.check_table_exists_and_create(
    db_name=conf.target_db,
    tb_name=conf.target_logs_table_name,
    tb_cols=conf.target_logs_table_create_cols
)


if len(new_file_list)>0:
    # 遍历要采集的日志文件
    start_time = time.time()
    for file_name in new_file_list:
        # 开启事务
        target_util.start_transaction()
        
        try:
            count_lines = 0
            for row in open(file_name,'r',encoding='utf-8'):
                # 逐行写入到数据库中
                backend_logs_model = BackendLogModel(row)
                target_util.insert_single_sql_without_commit(backend_logs_model.generate_insert_sql())
                
                # 逐行写入到CSV文件中
                csv_file.write(backend_logs_model.generate_csv_str())
                # 每处理一行，记录加一
                count_lines += 1
   
            # 将已处理的文件插入元数据表中，进行标记，防止重复采集
            mysql_util.process_file_insert_matedata_sql(file_name,count_lines,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            target_util.rollback_transaction()   # 执行异常，回滚事务
            print('事务已经回滚！')
            raise e
        else:
            target_util.commit_transaction()    # 正常执行，提交事务
            print(f'日志{file_name}已经采集完毕!')
    # 记录日志信息
    end_time = time.time()
    logger.info(f'本次总共采集了{len(new_file_list)}个文件，本次采集共消耗了{end_time-start_time}s')
    
else:
    print('日志已经全部采集完毕!')

# 关闭连接
csv_file.close()
target_util.close()
metadata_util.close()
