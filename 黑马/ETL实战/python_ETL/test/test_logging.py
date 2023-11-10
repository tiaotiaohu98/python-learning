# 第一步：导包
import unittest
import logging
from util import logging_util
# 第二步：创建一个类继承自TestCase

# 测试日志工具类
class TestLoggingUtil(unittest.TestCase):
    # 第三步：编写setUp 以及tearDown
    def setUp(self):
        pass

    def tearDown(self):
        pass
    # 第四步：针对工具类的方法进行单元测试

    def test_init_logger(self):
        # 创建一个日志对象
        logger = logging_util.init_logger()
        # 判断logger产生的是不是logging日志对象
        self.assertIsInstance(logger, logging.RootLogger)
