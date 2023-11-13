'''
    订单详情模型
'''
import json

from config import projrct_config as conf
from model.orders.SingleProductSoldModel import SingleProductSoldModel
from util import str_util,time_util

class OrdersDetailModel(object):
    
    def __init__(self,data):
        
        # 将json转换为字典
        data = json.loads(data)
        products = data['product']
        
        self.orderID = data['orderID'] # 订单ID   关联订单表
        self.products_barcode_list = []  # 记录本次订单卖出商品条码列表
        self.product_detail_list = []   # 产品销售详细
    
        for x in products:
            product = SingleProductSoldModel(x)
            self.product_detail_list.append(product)   
            
    # 生成插入一条数据的sql方法
    def generate_insert_sql(self):
        
        sql = f"insert into {conf.target_orders_detail_table_name} values"
        
        for single in self.product_detail_list:
            # single_product_model = SingleProductSoldModel(single)
            sql += f"('{self.orderID}'," + single.generate_segment_sql() + ","
        
        sql = sql[:-1]
        return sql
        
            

    # 生成表头方法
    @staticmethod
    def generate_csv_header(sep=','):
        return f"orderID{sep}" \
            f"barcode{sep}" \
            f"categoryID{sep}" \
            f"name{sep}" \
            f"pricePer{sep}" \
            f"retailPrice{sep}" \
            f"tradePrice{sep}" \
            f"unitID{sep}" \
            f"count\n"

    # 生成表内容方法
    def generate_csv_str(self):
        """生成添加csv的数据行"""
        csv_lines = ""
        
        for single in self.product_detail_list:
            csv_lines += f"{self.orderID}," + single.generate_csv_str()
            
        return csv_lines
        
    
if __name__ == '__main__':
    orederDetails = OrdersDetailModel('{"discountRate": 1, "storeShopNo": "None", "dayOrderSeq": 20, "storeDistrict": "鼎城区", "isSigned": 0, "storeProvince": "湖南省", "origin": 0, "storeGPSLongitude": "111.6968", "discount": 0, "storeID": 1102, "productCount": 5, "operatorName": "OperatorName", "operator": "NameStr", "storeStatus": "open", "storeOwnUserTel": 12345678910, "payType": "wechat", "discountType": 2, "storeName": "蔚然锦和德宏商行", "storeOwnUserName": "OwnUserNameStr", "dateTS": 1542436495000, "smallChange": 0, "storeGPSName": "None", "erase": 0, "product": [{"count": 2, "name": "鱼仙贝辣味0g", "unitID": 0, "barcode": "6927018499357", "pricePer": 1, "retailPrice": 1, "tradePrice": 0, "categoryID": 1}, {"count": 1, "name": "达利园熊字饼15g", "unitID": 7, "barcode": "6911988005205", "pricePer": 3, "retailPrice": 3, "tradePrice": 2, "categoryID": 1}, {"count": 1, "name": "周氏香油条198g辣熟食南特产典辣条0包", "unitID": 7, "barcode": "6948930800014", "pricePer": 3, "retailPrice": 3, "tradePrice": 2.2, "categoryID": 1}, {"count": 2, "name": "笋尖", "unitID": 4, "barcode": "6942483999652", "pricePer": 4, "retailPrice": 4, "tradePrice": 0, "categoryID": 1}, {"count": 1, "name": "脆皮香干90g", "unitID": 8, "barcode": "6936158286437", "pricePer": 3.5, "retailPrice": 3.5, "tradePrice": 2.8, "categoryID": 1}], "storeGPSAddress": "None", "orderID": "154243648350611021331", "moneyBeforeWholeDiscount": 19.5, "storeCategory": "normal", "receivable": 19.5, "faceID": "", "storeOwnUserId": 981, "paymentChannel": 0, "paymentScenarios": "PASV", "storeAddress": "StoreAddress", "totalNoDiscount": 19.5, "payedTotal": 19.5, "storeGPSLatitude": "29.008802", "storeCreateDateTS": 1537496115000, "storeCity": "常德市", "memberID": "0"}')
    
    print(orederDetails.generate_insert_sql())
    # print(orederDetails.generate_csv_header())
    # print(orederDetails.generate_csv_str())