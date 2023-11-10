class Student(object):

    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f'姓名：{self.name}, 年龄：{self.age}, 电话：{self.mobile}'


# if __name__ == '__main__':
#     s1 = Student('Tom', 23, '10086')
#     print(s1)
