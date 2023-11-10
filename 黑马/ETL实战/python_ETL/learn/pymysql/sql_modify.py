import pymysql

conn = pymysql.connect(host='localhost',port=33061, user='root', passwd='402191', db='test_sql', charset='utf8')

cursor = conn.cursor()

sql = "update test set AKA = '大力' where name = '于谦'"

row_nums = cursor.execute(sql)

if row_nums > 0:
    conn.commit()
    print('修改成功')
else:
    conn.rollback()
    print('修改失败')

cursor.close()
conn.close()

