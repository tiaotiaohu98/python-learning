from os import name


class Person(object):

    def __init__(self,name,age) -> None:
        self.name =name
        self.age = age

    def speak(self):
        print(f'姓名：{self.name}, 年龄：{self.age}')


class Student(Person):
    pass

s1 = Student('张三',23)
s1.speak()

