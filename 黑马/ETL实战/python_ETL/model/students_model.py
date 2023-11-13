
import json

class StudentModel(object):
    
    def __init__(self,json_str):
        data = json.loads(json_str)
        self.name =data['name']
        self.age = data['age']
        self.gender = data['gender']
        self.register_date = data['register_date']
        
        
    # 定义一个方法上传CSV表头
    def generate_csv_header(self,sep=','):
        return f'name{sep}' \
                f'age{sep}' \
                f'gender{sep}' \
                f'register_date\n'
    
    
    # 定义一个方法生成csv文件内容
    def generate_csv_str(self,sep=','):
        return f"{self.name}," \
                f"{self.age}," \
                f"{self.gender}," \
                f"{self.register_date}"
                
    # 定义一个方法，生成插入SQL语句
    def generate_insert_sql(self):
        return f"insert into students(name,age,gender,register_date) values(" \
                f"'{self.name}'," \
                f"'{self.age}'," \
                f"'{self.gender}',"\
                f"'{self.register_date}'" \
                f")"
                
if __name__ == '__main__':
    f = open('../source/students.txt','r',encoding='utf-8')
    content = f.read()
    s = StudentModel(content)
    
    print(s.generate_insert_sql())
    print(s.generate_csv_header())
    print(s.generate_csv_str())