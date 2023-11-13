from isort import file
from util import file_util
import unittest
import os

# 测试文件工具类
class TestFileUtil(unittest.TestCase):
    
    # 定义setUp方法，在每个测试方法执行之前执行
    def setUp(self) -> None:
        return super().setUp()
    # 定义tearDown方法，在每个测试方法执行之后执行
    def tearDown(self) -> None:
        return super().tearDown()
    
    # 测试获取目录下所有文件列表
    def test_get_dir_files_list(self):
        # 定义一个空列表，用于接收所有文件名称
        file_list = []
        # 获取指定目录下的所有文件
        path_list = file_util.get_dir_files_list('./test/test_dir')
        # 遍历path_list
        for file_path in path_list:
            # 获取文件名称
            filename = os.path.basename(file_path)
            # 将文件名称添加到file_list列表中
            file_list.append(filename)
        
        # 对文件列表进行排序
        path_list.sort()
        
        # 对列表进行比对，看是否与期待一致
        self.assertListEqual(file_list,['1','2'])
        
        # 定义一个空列表
        file_name_list = []
        path_list = file_util.get_dir_files_list('./test/test_dir',True)
        for file_path in path_list:
            file_name = os.path.basename(file_path)
            file_name_list.append(file_name)
        
        # 对列表进行排序
        file_name_list.sort()
        self.assertListEqual(file_name_list,['1','2','3','4','5'])
        
    def test_get_new_by_compare_lists(self):
        
        # 存储已经采集的文件列表
        processed_list = ['1.log','2.log','3.log']
        
        # 所有要采集的文件
        all_list = ['1.log','2.log','3.log','4.log','5.log']
        
        # 
        new_list = file_util.get_new_by_compare_lists(processed_list,all_list)
        self.assertListEqual(new_list,['4.log','5.log'])