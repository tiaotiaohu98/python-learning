'''
    with 实现文件读取，它带有上下文管理器，不需要人为关闭
'''
# with方式
with open('../logs/pyetl.log','r') as f:
    while True:
        content = f.readline()
        if not content:
            break
        print(content,end='')

# for循环方式
for row in open('../logs/pyetl.log','r',encoding='utf-8'):
    print(row,end='')