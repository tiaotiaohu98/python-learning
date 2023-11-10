# 导入模块
import os

print(__file__) # 输出当前文件路径

print(os.getcwd()) # 输出当前工作目录

print(os.listdir()) # 输出指定工作目录下的文件列表

print(os.listdir('D:\\AnacondaProjectsRepo\\python-learning\\黑马\\ETL实战'))
print(os.listdir('D:/AnacondaProjectsRepo/python-learning/黑马/ETL实战'))

# 返回指定路径的绝对路径
print(os.path.abspath('./os_learn.py'))



