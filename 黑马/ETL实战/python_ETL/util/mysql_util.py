
import pymysql
from util import logging_util
from config import projrct_config as conf

# 创建日志对象
logger = logging_util.init_logger('mysql_util')


class MysqlUtil(object):

    def __init__(self, autocommit=False):
        self.conn = pymysql.connect(
            host=conf.host,
            port=conf.port,
            user=conf.user,
            password=conf.password,
            charset=conf.charset,
            autocommit=autocommit
        )

        logger.info(f'{conf.host}:{conf.port}数据库已经连接成功')
        

    # 切换数据库
    def select_db(self, db_name):
        self.conn.select_db(db_name)
        logger.info(f'数据库{db_name}已经切换成功！')

    # 执行非查询SQL ==> 增删改
    def execute(self, sql):
        # 获取游标
        cursor = self.conn.cursor()

        # 执行sql
        row_nums = cursor.execute(sql)

        # 事务提交
        if row_nums > 0 and not self.conn.get_autocommit():
            self.commit_transaction()
            # 日志打印
            logger.info(f'非查询语句：{sql}已经执行成功！')
        else:
            self.rollback_transaction()
            # 日志打印
            logger.info(f'非查询语句：{sql}执行失败！')

        # 关闭游标
        cursor.close()

    # 执行查询sql
    def query(self, sql):

        cursor = self.conn.cursor()
        cursor.execute(sql)
        # 返回查询结果
        result = cursor.fetchall()
        # 打印日志
        logger.info(f'查询SQL：{sql}查询成功!')

        cursor.close()

        return result

    # 开启事务

    def start_transaction(self):
        self.conn.begin()
        logger.info(f'事务已经开启！')

    # 提交事务
    def commit_transaction(self):
        self.conn.commit()
        logger.info(f'事务已经提交！')

    # 回滚事务
    def rollback_transaction(self):
        self.conn.rollback()
        logger.info(f'事务回滚了！')

    # 检查表是否存在
    def check_table_exists(self, db_name, tb_name):
        # 切换数据库
        self.select_db(db_name)

        # sql语句
        sql = 'show tables;'
        
        result = self.query(sql)
       
        return (tb_name,) in result

    # 表不存在时，创建表
    def check_table_exists_and_create(self, db_name, tb_name, tb_cols):
        # 检查表是否存在
        if not self.check_table_exists(db_name, tb_name):
            # 创建表
            sql = f'create table {tb_name}({tb_cols})'
            
            # 执行非查询sql
            self.execute(sql)
            # 打印日志
            logger.info(f'数据库{db_name}中的数据表{tb_name}创建成功！')
        else:
            logger.info(f'数据库{db_name}中的{tb_name}表已经存在，无法创建！')

    # 查询指定表数据
    def query_all(self, db_name, tb_name, limit=None):
        self.select_db(db_name)
        
        sql = f'select * from {tb_name}'
        
        if limit is not None:
            sql += f' limit {limit}'
        
        result = self.query(sql)
        
        return result
    
    # 定义一个insert_single_sql(), 用于执行单条SQL插入操作  => 采集数据的时候时一行一行采集的
    def insert_single_sql(self,sql):
        try:
            self.execute(sql)
        except Exception as e:
            logger.error(f'单条语句：{sql}执行异常，错误信息为：{e}')
            raise e  # 抛出异常
        else:
            logger.info(f'{sql} 执行成功！')
    
    # 只执行sql，不提交事务
    def insert_single_sql_without_commit(self,sql):
        try:
            # 获取连接
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            logger.error(f'单条语句：{sql}执行异常，错误信息为：{e}')
            raise e  # 抛出异常
        else:
            logger.info(f'{sql} 执行成功！')
            
    # 关闭数据库连接
    def close(self):
        
        if self.conn.open:
            self.conn.close()
        # else:
        #     print('连接已关闭！不要重复关闭')
        logger.info(f'数据库连接对象已经关闭！')

# if __name__ == '__main__':
#     mysql_util = MysqlUtil()
#     # mysql_util.select_db('demo')
#     # mysql_util.execute('insert into tb_bank values (6,"赵六",12324)')
#     # print(mysql_util.query('select * from tb_bank'))
#     # print(mysql_util.check_table_exists('demo', 'tb_students'))
#     # mysql_util.check_table_exists_and_create('demo', 'tb_bank', 'id int')
#     # mysql_util.check_table_exists_and_create(
#     #     'demo', 'tb_student', 'id int auto_increment primary key, name varchar(50), age int, gender varchar(10)')
#     mysql_util.close()

# 用于获取mysqutil类对象
def get_mysql_util(autocommit=False):
    return MysqlUtil(autocommit)

# 定义一个方法，用于获取元数据表中已经处理过的文件信息
def get_processed_files(util:MysqlUtil,db_name,tb_name,tb_cols):
    # 1.定义一个空列表，用于获取已经采集的文件信息
    new_list = []
    # 2.检查元数据表是否存在，不存在则根据配置文件自动创建该表
    util.check_table_exists_and_create(db_name,tb_name,tb_cols)
    # 3.读取元数据表中的数据
    result = util.query_all(db_name,tb_name)
    # 4.把元数据表中已经采集过的文件名称放入列表中
    for file_name in result:
        new_list.append(file_name[1])
    # 5.返回最终列表
    return new_list

'''
    # 定义一个方法，将已经处理的表信息插入元数据表中
    id 自增
    file_name 处理的文件路径
    process_lines 文件处理行数
    process_time  文件处理时间
'''
def process_file_insert_matedata_sql(file_name, process_lines, process_time):
    # 创建sql对象
    process_file_insert = get_mysql_util()
    
    # 定义插入数据sql
    sql = f'insert into backend_logs_monitor(file_name, process_lines, process_time) values("{file_name}",{process_lines},"{process_time}")'
    
    # print(sql)
    # 选择数据库
    process_file_insert.select_db(conf.metadata_db)
    
    # 执行sql,插入已处理的数据信息
    process_file_insert.insert_single_sql(sql)

    # 关闭连接
    process_file_insert.close()