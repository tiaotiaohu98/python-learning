'''
    单个商品售卖模型
'''

import json
from config import projrct_config as conf
from util import str_util,time_util

class SingleProductSoldModel(object):
    
    def __init__(self,products_detail):
    
        self.barcode = products_detail['barcode']  # 商品条形码 主键
        self.categoryID = products_detail['categoryID']  # 类别ID
        self.name = products_detail['name']    # 商品名称
        self.pricePer = products_detail['pricePer'] # 单价
        self.retailPrice = products_detail['retailPrice'] # 零售价格
        self.tradePrice = products_detail['tradePrice']   # 进货价格
        self.unitID = products_detail['unitID']    # 单位编号
        self.count = products_detail['count']      # 销售数量
        
    # 生成插入一条数据的sql方法
    def generate_insert_sql(self,sep=','):
        return f"insert into {conf.target_singleproduct_sold_table_name} values ({self.barcode}," \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.categoryID)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.pricePer)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.retailPrice)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.tradePrice)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.unitID)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.count)}" \
            f")"
            
    # 生成sql片段以供订单明细模型调用，生成sql
    def generate_segment_sql(self,sep=','):
        return f"{str_util.check_str_null_and_transform_to_sql_null(self.barcode)}," \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.categoryID)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.pricePer)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.retailPrice)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.tradePrice)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.unitID)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.count)}" \
            f")"

    # 生成表头方法
    @staticmethod
    def generate_csv_header(sep=','):
        return f"barcode{sep}" \
            f"categoryID{sep}" \
            f"name{sep}" \
            f"pricePer{sep}" \
            f"retailPrice{sep}" \
            f"tradePrice{sep}" \
            f"unitID{sep}" \
            f"count\n"

    # 生成表内容方法
    def generate_csv_str(self,sep=','):
        return f"{self.barcode}{sep}" \
            f"{self.categoryID}{sep}" \
            f"{self.name}{sep}" \
            f"{self.pricePer}{sep}" \
            f"{self.retailPrice}{sep}" \
            f"{self.tradePrice}{sep}" \
            f"{self.unitID}{sep}" \
            f"{self.count}\n"


if __name__ == '__main__':
    singleProduct = SingleProductSoldModel({'count': 2, 'name': '鱼仙贝辣味0g', 'unitID': 0, 'barcode': '6927018499357', 'pricePer': 1, 'retailPrice': 1, 'tradePrice': 0, 'categoryID': 1})
    
    print(singleProduct.generate_insert_sql())
    print(singleProduct.generate_segment_sql())
    print(singleProduct.generate_csv_header())
    print(singleProduct.generate_csv_str())