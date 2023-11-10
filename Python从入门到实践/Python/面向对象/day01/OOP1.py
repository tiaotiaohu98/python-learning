'''
    面向对象编程：
        1、编程思想
        2、类和对象
'''


class Person(object):
   # 定义属性
   # 定义方法
    def eat(self):
        print('我喜欢吃零食！')

    def speak(self):
        # print('我会说普通话！')
        print(self)
        print(type(self))

# 实例化
p1 = Person()

print(p1)
print(type(p1))

p1.eat()
p1.speak()

p2 = Person()
p2.eat()


# self表示对象, 谁调用了成员方法，self就指向谁
print('-' * 40)
p1.speak()

p2.speak()

# 添加和获取对象属性

