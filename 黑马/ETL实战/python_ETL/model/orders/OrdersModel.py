'''
    订单模型
    order_id, store_id, store_name, store_status, store_own_user_id, store_own_user_name, store_own_user_tel,
    store_category, store_address, store_shop_no, store_province, store_city, store_district, store_gps_name, store_gps_address,
    store_gps_longitude, store_gps_latitude, is_signed, operator, operator_name, face_id, member_id, store_create_date_ts, origin,
    day_order_seq, discount_rate, discount_type, discount, money_before_whole_discount, receivable, erase, small_change, total_no_discount,
    pay_total, pay_type, payment_channel, payment_scenarios, product_count, date_ts
'''

import json
from config import projrct_config as conf
from util import str_util, time_util


class OrdersModel(object):
    def __init__(self, data):
        
        # 将json转换为字典
        data = json.loads(data)
        
        self.order_id = data['orderID']                       # PRIMARY KEY
        self.store_id = data['storeID']                       # '店铺ID'
        self.store_name = data['storeName']                    # '店铺名称'
        self.store_status = data['storeStatus']                # '店铺状态(open,close)'
        self.store_own_user_id = data['storeOwnUserId']     # '店主id'
        self.store_own_user_name = data['storeOwnUserName']  # '店主名称'
        self.store_own_user_tel = data['storeOwnUserTel']   # '店主手机号'
        self.store_category = data['storeCategory']           # '店铺类型(normal,test)'
        self.store_address = data['storeAddress']              # '店铺地址'
        self.store_shop_no = data['storeShopNo']             # '店铺第三方支付id号'
        self.store_province = data['storeProvince']           # '店铺所在省'
        self.store_city = data['storeCity']                    # '店铺所在市'
        self.store_district = data['storeDistrict']           # '店铺所在行政区'
        self.store_gps_name = data['storeGPSName']           # '店铺gps名称'
        self.store_gps_address = data['storeGPSAddress']     # '店铺gps地址'
        self.store_gps_longitude = data['storeGPSLongitude']  # '店铺gps经度'
        self.store_gps_latitude = data['storeGPSLatitude']  # '店铺gps纬度'
        self.is_signed = data['isSigned']          # '是否第三方支付签约(0,1)'
        self.operator = data['operator']  # '操作员'
        self.operator_name = data['operatorName']  # '操作员名称'
        self.face_id = data['faceID']       # '顾客面部识别ID'
        self.member_id = data['memberID']      # '顾客会员ID'
        self.store_create_date_ts = data['storeCreateDateTS']    # '店铺创建时间'
        self.origin = data['origin']    # '原始信息(无用)'
        self.day_order_seq = data['dayOrderSeq']  # '本订单是当日第几单'
        self.discount_rate = data['discountRate']  # '折扣率'
        self.discount_type = data['discountType']  # '折扣类型'
        self.discount = data['discount']     # '折扣金额'
        self.money_before_whole_discount = data['moneyBeforeWholeDiscount']   # '折扣前总金额'
        self.receivable = data['receivable']    # '应收金额'
        self.erase = data['erase']   # '抹零金额'
        self.small_change = data['smallChange']     # '找零金额'
        self.total_no_discount = data['totalNoDiscount']   # '总价格(无折扣'
        self.pay_total = data['payedTotal']   # '付款金额'
        self.pay_type = data['payType']    # '付款类型'
        self.payment_channel = data['paymentChannel']  # '付款通道'
        self.payment_scenarios = data['paymentScenarios']   # '付款描述(无用)'
        self.product_count = data['productCount']   # '本单卖出多少商品'
        self.date_ts = data['dateTS']        # '订单时间'
        
    # 生成插入一条数据的sql方法 
    # 检查空内容，并修改为null
    def generate_insert_sql(self,sep=','):
        return f"insert into {conf.target_orders_table_name} values (" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.order_id)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.store_id)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_name)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_status)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.store_own_user_id)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_name)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_tel)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_category)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_address)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_shop_no)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_province)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_city)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_district)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_name)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_address)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_longitude)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_latitude)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.is_signed)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.operator)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.operator_name)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.face_id)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.member_id)}{sep}" \
            f"'{time_util.ts13_to_data_str(self.store_create_date_ts)}'{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.origin)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.day_order_seq)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.discount_rate)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.discount_type)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.discount)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.money_before_whole_discount)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.receivable)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.erase)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.small_change)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.total_no_discount)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.pay_total)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.pay_type)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.payment_channel)}{sep}" \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.payment_scenarios)}{sep}" \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.product_count)}{sep}" \
            f"'{time_util.ts13_to_data_str(self.date_ts)}'" \
            f")"

    # 生成表头方法
    @staticmethod
    def generate_csv_header(sep=','):
        return f"order_id{sep}" \
            f"store_id{sep}" \
            f"store_name{sep}" \
            f"store_status{sep}" \
            f"store_own_user_id{sep}" \
            f"store_own_user_name{sep}" \
            f"store_own_user_tel{sep}" \
            f"store_category{sep}" \
            f"store_address{sep}" \
            f"store_shop_no{sep}" \
            f"store_province{sep}" \
            f"store_city{sep}" \
            f"store_district{sep}" \
            f"store_gps_name{sep}" \
            f"store_gps_address{sep}" \
            f"store_gps_longitude{sep}" \
            f"store_gps_latitude{sep}" \
            f"is_signed{sep}" \
            f"operator{sep}" \
            f"operator_name{sep}" \
            f"face_id{sep}" \
            f"member_id{sep}" \
            f"store_create_date_ts{sep}" \
            f"origin{sep}" \
            f"day_order_seq{sep}" \
            f"discount_rate{sep}" \
            f"discount_type{sep}" \
            f"discount{sep}" \
            f"money_before_whole_discount{sep}" \
            f"receivable{sep}" \
            f"erase{sep}" \
            f"small_change{sep}" \
            f"total_no_discount{sep}" \
            f"pay_total{sep}" \
            f"pay_type{sep}" \
            f"payment_channel{sep}" \
            f"payment_scenarios{sep}" \
            f"product_count{sep}" \
            f"date_ts\n"

    # 生成表内容方法
    def generate_csv_str(self,sep=','):
        return f"" \
            f"{self.order_id}{sep}" \
            f"{self.store_id}{sep}" \
            f"{self.store_name}{sep}" \
            f"{self.store_status}{sep}" \
            f"{self.store_own_user_id}{sep}" \
            f"{self.store_own_user_name}{sep}" \
            f"{self.store_own_user_tel}{sep}" \
            f"{self.store_category}{sep}" \
            f"{self.store_address}{sep}" \
            f"{self.store_shop_no}{sep}" \
            f"{self.store_province}{sep}" \
            f"{self.store_city}{sep}" \
            f"{self.store_district}{sep}" \
            f"{self.store_gps_name}{sep}" \
            f"{self.store_gps_address}{sep}" \
            f"{self.store_gps_longitude}{sep}" \
            f"{self.store_gps_latitude}{sep}" \
            f"{self.is_signed}{sep}" \
            f"{self.operator}{sep}" \
            f"{self.operator_name}{sep}" \
            f"{self.face_id}{sep}" \
            f"{self.member_id}{sep}" \
            f"{time_util.ts13_to_data_str(self.store_create_date_ts)}{sep}" \
            f"{self.origin}{sep}" \
            f"{self.day_order_seq}{sep}" \
            f"{self.discount_rate}{sep}" \
            f"{self.discount_type}{sep}" \
            f"{self.discount}{sep}" \
            f"{self.money_before_whole_discount}{sep}" \
            f"{self.receivable}{sep}" \
            f"{self.erase}{sep}" \
            f"{self.small_change}{sep}" \
            f"{self.total_no_discount}{sep}" \
            f"{self.pay_total}{sep}" \
            f"{self.pay_type}{sep}" \
            f"{self.payment_channel}{sep}" \
            f"{self.payment_scenarios}{sep}" \
            f"{self.product_count}{sep}" \
            f"{time_util.ts13_to_data_str(self.date_ts)}\n"
        
if __name__=='__main__':
    
    # for row in open("../../source/students.json",'r',encoding='utf8'):
    for row in open("../../source/ord_json/x02",'r',encoding='utf8'):
        Orders = OrdersModel(row)
    
        print(Orders.generate_insert_sql())
        print(Orders.generate_csv_header())
        print(Orders.generate_csv_str())
        