'''
    1、表名--类名
    2、字段名--属性
    3、记录--对象
'''

class Person(object):
    def __init__(self,id,name,age) -> None:
        self.id = id
        self.name = name
        self.age = age
        
p1 = Person(1,'宝强',32)
p2 = Person(2,'乃亮',35)
p3 = Person(3,'羽凡',37)

