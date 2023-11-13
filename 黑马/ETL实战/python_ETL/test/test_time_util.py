import unittest
from util import time_util

class TestTimeUtil(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_ts13_to_ts10(self):
        ts13 = 1645539742000
        ts10 = time_util.ts13_to_ts10(ts13)
        self.assertEqual(ts10, 1645539742)
        
    def test_ts10_to_datastr(self):
        ts10 = 1645539742
        data_str = time_util.ts10_to_data_str(ts10)
        self.assertEqual(data_str, '2022-02-22 22:22:22')