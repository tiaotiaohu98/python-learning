'''
    魔法方法：
        __init__
    作用：进行初始化操作，类被实例化时，自动触发
        __str__
    作用：打印对象自身信息
    __str__ 只能返回字符串类型的数据，否则会报错
        __del__
    作用：用于清理和回收工作
        当对象被删除时，会自动调用该方法
'''

class Person(object):
    """docstring for Person."""
    def __init__(self, name, age):
        self.name = name
        self.age =age
    
    # 定义成员方法
    def speak(self):
        print('I can speak Chinese!')
        
    # 打印对象自身信息
    # __str__ 只能返回字符串类型的数据，否则会报错
    def __str__(self) -> str:
        return f'我的姓名叫：{self.name}, 今年{self.age}岁了！'
    
    '''
        方式一：手动删除：del 对象名
        方式二：自动删除
    '''
    def __del__(self):
        print('当对象被删除时，此方法会自动被调用！')
        print('在工作中，__del__方法用于清理和回收工作')
        
    
# 实例化类，创建对象
p1 = Person('张三', 23)
# print(p1.name)

# print(p1.age)
# p1.speak()

# p2 = Person('李四', 24)
# print(p2.name)
# print(p2.age)

# 打印对象自身信息
print(p1)


    