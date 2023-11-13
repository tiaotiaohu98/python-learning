'''
    原始数据模型
'''
from model.orders.OrdersModel import OrdersModel
from model.orders.OrdersDetailModel import OrdersDetailModel
from model.orders.SingleProductSoldModel import SingleProductSoldModel


class RetailOriginJsonModel(object):
    """
    原始订单JSON数据模型
    """
    def __init__(self, data):
        self.order_model = OrdersModel(data)
        self.order_detail_model = OrdersDetailModel(data)
        # self.singleproduct_sold_model = SingleProductSoldModel(data)

    def get_order_model(self):
        return self.order_model

    def get_order_detail_model(self):
        return self.order_detail_model
    
    # def get_singleproduct_sold_model(self):
    #     return self.singleproduct_sold_model

    def get_order_id(self):
        return self.order_model.order_id

    def get_products_list(self):
        return self.order_detail_model.product_detail_list