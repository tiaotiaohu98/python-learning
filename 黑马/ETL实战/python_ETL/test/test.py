'''
    导入unittest模块
'''

from unittest import TestCase

class TestDemo(TestCase):
    
    # 测试前执行方法
    def setUp(self) -> None:
        print('测试前执行方法, 用于实现初始化操作')
    
    # 测试后执行方法  
    def tearDown(self) -> None:
        print('测试后执行方法, 用于实现清理操作')
        
    # 自定义测试方法
    def test_func1(self):
        print('func1函数的单元测试')
        
    def test_func2(self):
        print('func2函数的单元测试')
