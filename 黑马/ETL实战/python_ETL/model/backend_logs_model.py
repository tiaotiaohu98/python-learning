'''
    1、定义一个类将日志文件内容转换为模型类，实现可以将日志信息变成结构化数据，使其可以导入mysql中
'''

class BackendLogModel(object):
    
    def __init__(self,log_str):
        data  = log_str.split('\t')
        self.log_time = data[0]
        self.log_level = data[1].strip('[]')
        self.log_module = data[2]
        self.response_time = data[3][5:-2]
        self.province = data[4]
        self.city = data[5]
        self.log_text = data[6]
        
    # 定义一个方法，生成插入SQL语句
    def generate_insert_sql(self):
        return f"insert into backend_logs(log_time,log_level,log_module,response_time,province,city,log_text) values(" \
                f"'{self.log_time}'," \
                f"'{self.log_level}'," \
                f"'{self.log_module}'," \
                f"{self.response_time}," \
                f"'{self.province}'," \
                f"'{self.city}'," \
                f"'{self.log_text}'" \
                f")"
    
    # 定义一个方法，处理表头信息
    @staticmethod
    def generate_csv_header(sep=','):
        return f'log_time{sep}' \
                f'log_level{sep}' \
                f'log_module{sep}' \
                f'response_time{sep}' \
                f'province{sep}' \
                f'city{sep}' \
                f'log_text\n'
                
    # 定义一个方法，处理表内容
    def generate_csv_str(self,sep=','):
        return  f"{self.log_time}{sep}" \
                f"{self.log_level}{sep}" \
                f"{self.log_module}{sep}" \
                f"{self.response_time}{sep}" \
                f"{self.province}{sep}" \
                f"{self.city}{sep}" \
                f"{self.log_text}"


# if __name__ == '__main__':
#     backend_logs = BackendLogModel('2023-11-10 16:02:47.462279	[INFO]	barcode_service.py	响应时间:449ms	安徽省	合肥市	这里是日志信息......')
#     print(backend_logs.log_time,backend_logs.log_level,backend_logs.log_module,
#           backend_logs.response_time,backend_logs.province,backend_logs.city,backend_logs.log_text)
#     print(backend_logs.generate_insert_sql())
#     print(backend_logs.generate_csv_header())
#     print(backend_logs.generate_csv_str())