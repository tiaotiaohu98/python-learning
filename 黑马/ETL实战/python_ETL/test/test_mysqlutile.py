import unittest
from unittest import result
from urllib import request
from util import mysql_util
from config import projrct_config as conf

# 定义一个测试类
class TestMysqlUtil(unittest.TestCase):
    # 定义setUp()进行初始化操作
    '''
        1、创建连接
        2、创建数据库
        3、执行sql
        4、切换数据库
        5、创建表
    '''
    def setUp(self) -> None:
        self.util = mysql_util.get_mysql_util()
        self.util.excute('create database test default charset=utf8')
        self.util.select_db('test')
        self.util.excute('create table unit_test(id int, name varchar(20))')
        
    def tearDown(self)->None:
        self.util.excute('drop table unit_test')
        self.util.excute('drop database test')
        
    def test_insert_single_sql(self):
        self.util.insert_single_sql('insert into unit_test values(1,"Tom")')
        sql = "select * from unit_test"
        result = self.util.query(sql)
        
        self.assertEqual(result,((1,'Tom'), ))
    