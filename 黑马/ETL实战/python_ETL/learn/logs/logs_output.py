import logging
from math import log
from venv import logger
'''
    1、导入日志模块
    2、创建日志管理对象
    3、创建日志处理器
    4、日志格式
    5、绑定日志处理器到日志对象
    6、设置日志级别
    7、打印输出日志信息
'''
# 创建日志管理对象
logger = logging.getLogger()

# 创建日志处理器
# stream_handler = logging.StreamHandler()
# 导出到指定文件
file_handler= logging.FileHandler(
    filename="./learn/logs/pyetl.log",
    mode='a',
    encoding='utf-8')


# 设置日志格式
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(filename)s[%(lineno)d] : %(message)s")
# stream_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

# 设置日志对象的日志级别
logger.setLevel(logging.INFO)  # DEBUG < INFO < WARNING < ERROR < CRITICAL

# 绑定日志处理器到日志对象
# logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# 输出日志信息
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

