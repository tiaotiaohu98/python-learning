'''
    1、导入pymysql模块
    2、创建数据库连接(IP、端口、用户名、密码、数据库、编码方式)
    3、创建游标
    4、定义sql语句
    5、执行sql语句
    6、提交事务(commit)/回滚事务(rollback)
    7、关闭游标
    8、关闭数据库连接
'''
import pymysql

conn = pymysql.connect(host='localhost', port=33061, user='root', passwd='402191', db='test_sql', charset='utf8')

curster = conn.cursor()

sql = "delete from test where birthday is null"

row_nums = curster.execute(sql)

if row_nums > 0:
    conn.commit()
    print("删除成功")
    print(row_nums)
else:
    conn.rollback()
    print("删除失败")
    
curster.close()
conn.close()
