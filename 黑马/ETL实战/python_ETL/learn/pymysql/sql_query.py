import pymysql

conn = pymysql.connect(host='localhost', port=33061, user='root', password='402191', db='test_sql', charset='utf8')

cursor = conn.cursor()

sql = "select * from test"

row_nums = cursor.execute(sql)

# query_set = cursor.fetchall() # 获取全部数据
# query_set1 = cursor.fetchone() # 获取一条数据
query_set1 = cursor.fetchmany(3) # 获取3条数据

if row_nums > 0:
    conn.commit()
    print(query_set1)
else:
    conn.rollback()
    print("查询失败")

cursor.close()
conn.close()
