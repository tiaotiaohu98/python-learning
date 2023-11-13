
import pymysql
from sqlalchemy import null
from util import str_util
from config import projrct_config as conf
from util import str_util

class BarcodeModel(object):

    # 初始化方法，将表名映射成属性名
    # def __init__(self, code=None, name=None, spec=None, trademark=None, addr=None,
    #              units=None, factory_name=None, trade_price=None, retail_price=None, updateAt=None,
    #              wholeunit=None, wholenum=None, img=None, src=None):
    #     self.code = code
    #     self.name = str_util.clear_str(name)
    #     self.spec = str_util.clear_str(spec)
    #     self.trademark = str_util.clear_str(trademark)
    #     self.addr = str_util.clear_str(addr)
    #     self.units = str_util.clear_str(units)
    #     self.factory_name = str_util.clear_str(factory_name)
    #     self.trade_price = trade_price
    #     self.retail_price = retail_price
    #     self.updateAt = updateAt
    #     self.wholeunit = wholeunit
    #     self.wholenum = wholenum
    #     self.img = img
    #     self.src = src

    # 优化参数
    # pymysql 中cursor.fetchall() 方法返回数据格式及类型为  ((1条记录),(2条记录),(3条记录),......)
    def __init__(self, data_tuple: tuple):  # data_tuple参数，冒号后面代表期待的值类型
        self.code = data_tuple[0]
        self.name = str_util.clear_str(data_tuple[1])
        self.spec = str_util.clear_str(data_tuple[2])
        self.trademark = str_util.clear_str(data_tuple[3])
        self.addr = str_util.clear_str(data_tuple[4])
        self.units = str_util.clear_str(data_tuple[5])
        self.factory_name = str_util.clear_str(data_tuple[6])
        self.trade_price = data_tuple[7]
        self.retail_price = data_tuple[8]
        self.updateAt = data_tuple[9]
        self.wholeunit = str_util.clear_str(data_tuple[10])
        self.wholenum = data_tuple[11]
        self.img = str_util.clear_str(data_tuple[12])
        self.src = str_util.clear_str(data_tuple[13])


    # 生成插入sql语句
    def generate_insert_sql(self):
        return f"insert into {conf.target_barcode_table_name} values('{self.code}'," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.spec)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.trademark)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.addr)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.units)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.factory_name)}," \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.trade_price)}," \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.retail_price)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.updateAt)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.wholeunit)}," \
            f"{str_util.check_number_null_and_transform_to_sql_null(self.wholenum)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.img)}," \
            f"{str_util.check_str_null_and_transform_to_sql_null(self.src)}" \
            f")"

    # 生成表头信息
    @staticmethod
    def generate_csv_header(sep=','):
        return f"code{sep}" \
            f"name{sep}" \
            f"spec{sep}" \
            f"trademark{sep}" \
            f"addr{sep}" \
            f"units{sep}" \
            f"factory_name{sep}" \
            f"trade_price{sep}" \
            f"retail_price{sep}" \
            f"updateAt{sep}" \
            f"wholeunit{sep}" \
            f"wholenum{sep}" \
            f"img{sep}" \
            f"src\n"

    # 生成csv内容信息
    def generate_csv_str(self,sep=","):
        return f"{self.code}{sep}" \
            f"{self.name}{sep}" \
            f"{self.spec}{sep}" \
            f"{self.trademark}{sep}" \
            f"{self.addr}{sep}" \
            f"{self.units}{sep}" \
            f"{self.factory_name}{sep}" \
            f"{self.trade_price}{sep}" \
            f"{self.retail_price}{sep}" \
            f"{self.updateAt}{sep}" \
            f"{self.wholeunit}{sep}" \
            f"{self.wholenum}{sep}" \
            f"{self.img}{sep}" \
            f"{self.src}\n"
            
# if __name__ == '__main__':
#     # a = BarcodeModel(6900000014288,"MT428-430铁线相架","MT428-430","","","个","",0.0000,0.0000,"2017-07-10 16:56:44","",0,"","")
#     # a = BarcodeModel(690000,"伪造","","默认","","默认","",1,10,"2017-07-10 19:09:09","","","","")
#     print(a.generate_insert_sql())
#     print(a.generate_csv_header())
#     print(a.generate_csv_str())








