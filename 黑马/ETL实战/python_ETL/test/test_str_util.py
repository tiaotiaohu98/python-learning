from re import T
import unittest
from unittest import result

from sqlalchemy import true
from util import str_util

class TestStrUtil(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_check_null(self):
        data = None
        result = str_util.check_null(data)
        self.assertEqual(result,True)
        
    def test_check_str_null_and_transform_to_sql_null(self):
        data = None
        result = str_util.check_str_null_and_transform_to_sql_null(data)
        self.assertEqual(result, 'null')