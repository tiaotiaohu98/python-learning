'''
    面向对象的三大特性
        1、封装：将属性和方法写到类里面，可以添加私有属性和方法
        2、继承：子类继承父类的属性和方法，也可以重写父类的属性和方法
        3、多态：同一事物具有不同的形态
'''

class Girl(object):
    def __init__(self,name):
        self.name = name
        self.__age = 18
    
    def set_age(self,age):
        
        if not isinstance(age, int):
            exit('抱歉，年龄应设置为一个整数')
        
        if 18 < age < 120:
            self.__age = age
        else:
            exit('抱歉，年龄设置不合理，请重试！')
    
    def get_age(self):
        return self.__age
        
# 创建对象
gl = Girl('小美')
print(gl.name)

# 类的外部不能直接访问私有属性或方法
# print(gl.__age)

# gl.set_age('绝对加速度')
# gl.set_age(2000)
gl.set_age(20)
print(gl.get_age())


