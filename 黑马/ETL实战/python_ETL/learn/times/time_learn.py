'''
    1、导入time模块
'''

import time

# 获取当前时间戳，以秒为单位
print(time.time())

# 获取当前时间戳，以纳秒为单位
print(time.time_ns())

# 获取本地时间
time1 = time.localtime()
print(time1)
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)

# 时间戳与struct_time的转换
date_time = time.localtime(1699326693.055388)
print(date_time)
date_float = time.mktime(date_time)
print(date_float)

# 日期格式化
date_str = time.strftime('%Y-%m-%d %H:%M:%S', date_time)
print(date_str)
# 将格式化后的日期字符串转换为struct_time

date_time1 = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
print(date_time1)