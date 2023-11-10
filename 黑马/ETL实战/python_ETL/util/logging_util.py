'''
    logging工具模块
    @Time: 2023/11/07
    @Description:
        1、创建一个Logging类管理日志器对象
        2、创建init_logger函数，用于快速获取logger日志器对象，以及绑定日志管理器和输出格式
'''

# 导入模块
import logging
from config import projrct_config as conf


# 定义一个工具类，用于创建日志对象，并设置日志级别
class LoggingUtil(object):

    def __init__(self, level=logging.INFO):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)


def init_logger():
    # 获取logger日志器对象，以及绑定日志管理器和输出格式
    # 1、创建日志对象
    logger = LoggingUtil().logger

    # 2、创建一个日志处理器对象
    file_handler = logging.FileHandler(
        filename=conf.log_root_path + conf.log_name,
        mode='a',
        encoding='utf-8')

    # 3、创建一个日志格式对象
    fmt = logging.Formatter(
        '[%(asctime)s] - %(levelname)s - %(filename)s[%(lineno)d] : %(message)s')

    # 4、将日志格式添加到日志处理器中
    file_handler.setFormatter(fmt)

    # 5、将日志处理器添加到日志对象中
    logger.addHandler(file_handler)

    # 6、返回logger日志器对象
    return logger


# if __name__ == '__main__':
#     logger = init_logger()
#     logger.info('test')
