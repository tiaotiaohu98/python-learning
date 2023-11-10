# 导入模块
import pymysql

# 创建链接
conn = pymysql.connect(host='localhost', port=33061, user='root', password='402191', database='test_sql', charset='utf8')

# 创建游标
cursor = conn.cursor()

# 定义sql语句
sql = "insert into test(name,AKA) values('李', '法师')"

# 执行sql语句
row_nums = cursor.execute(sql)

if row_nums > 0:
    conn.commit()
    print('插入成功')
else:
    conn.rollback()
cursor.close()
conn.close()
