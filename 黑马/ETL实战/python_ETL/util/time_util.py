import time

def ts13_to_ts10(ts):
    # 将13位的时间戳转换为10位的
    return ts // 1000

def ts10_to_data_str(ts, format_str='%Y-%m-%d %H:%M:%S'):
    # 将10位的时间戳转换为日期字符串
    time_array = time.localtime(ts)
    return time.strftime(format_str, time_array)

def ts13_to_data_str(ts, format_str='%Y-%m-%d %H:%M:%S'):
    # 将13位的时间戳转换为日期字符串
    ts = ts13_to_ts10(ts)
    return ts10_to_data_str(ts, format_str)