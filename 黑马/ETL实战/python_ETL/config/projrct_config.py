'''
    Project Configuration File
    @Time: 2023/11/09
    
'''
from enum import auto
import os
import time

src_path = os.path.dirname(os.path.abspath(__file__))
log_root_path = os.path.dirname(src_path) + '\\logs\\'                        
# print(log_root_path)
log_name = f'pyetl-{time.strftime("%Y-%m-%d %H", time.localtime())}.log'

host = '127.0.0.1'
port = 3306
user = 'root'
password = '402191'
charset = 'utf8'