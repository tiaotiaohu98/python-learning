def sum_num(num1 , num2):
    return num1 + num2
'''
    __name__ 在当前页面执行，则返回__main__
    被其他.py文件引用时，返回模块名
'''
print(__name__)

if __name__ == '__main__':
    print(sum_num(10,100))
    