'''
    递归函数：
        1、结束条件
        2、递归调用(通项公式)
        3、返回值（函数要求的是什么，返回什么）
    基本语法：
        def func(x):
            if 递归结束条件:
                return 终止条件的值
            func(x)
    实例：求1到10的累加结果
        func(1) = 1
        func(2) = func(1) + 2
        func(3) = func(2) + 3
        func(4) = func(3) + 4
        ...
        func(n) = func(n-1) + n
'''

def func(n):
    if n == 1:
        return 1
    return func(n-1) + n
        
print(func(10))
print(func(998))      # 递归深度太深，会导致栈溢出