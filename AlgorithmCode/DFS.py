"""
    迷宫问题：（深度优先搜索）DFS方法求解
    思路：定义两个数组，
        a[x][y]一个表示是否为障碍物或墙    0表示非障碍物 1表示障碍物
        b[x][y]一个表示是否已经探索过     0表示未探索  1表示已探索
        按右下左上四个方向的顺序依次探索，若路不通则回退到上一个位置，换一个方向探索，若还是不通，则继续回退
        直到找到一条路径；然后回退看是否有其他路径，直到所有的路径都找到
        最后返回最短路径
"""


#   (x,y)表示当前结点， step表示步长  (p,q)表示目标点
def DFS(x, y, step):
    # 如果到达目标点，则回溯
    if x == p and y == q:
        global min_path
        if step <= min_path:
            min_path = step
            print(min_path)
            return

    if x + 1 < 5 and y + 1 < 5:
        # 顺时针探索
        # 第一种方式
        # 右
        # 如果不是障碍物且未探索，则进行探索
        if a[x][y + 1] == 0 and b[x][y + 1] == 0:
            # 将该位置设置为已探索
            b[x][y + 1] = 1
            # 无路可走时，才会回溯
            DFS(x, y + 1, step + 1)
            print(step)
            # 探索完后，将当前位置设置为未探索，防止其他路径经过该位置时无法探索
            b[x][y + 1] = 0
        # 上
        if a[x + 1][y] == 0 and b[x + 1][y] == 0:
            # 将该位置设置为已探索
            b[x + 1][y] = 1
            # 无路可走时，才会回溯
            DFS(x + 1, y, step + 1)
            # 探索完后，将当前位置设置为未探索，防止其他路径经过该位置时无法探索
            b[x + 1][y] = 0
        # 左
        if a[x][y - 1] == 0 and b[x][y - 1] == 0:
            # 将该位置设置为已探索
            b[x][y - 1] = 1
            # 无路可走时，才会回溯
            DFS(x, y - 1, step + 1)
            # 探索完后，将当前位置设置为未探索，防止其他路径经过该位置时无法探索
            b[x][y + 1] = 0
        # 下
        if a[x - 1][y] == 0 and b[x - 1][y] == 0:
            # 将该位置设置为已探索
            b[x - 1][y] = 1
            # 无路可走时，才会回溯
            DFS(x - 1, y, step + 1)
            # 探索完后，将当前位置设置为未探索，防止其他路径经过该位置时无法探索
            b[x - 1][y] = 0


# 起点坐标
start_x, start_y = 0, 0
# 终点坐标
p, q = 4, 3
# 最短路径
min_path = 9999999999

a = [ [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
b = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]

a[start_x][start_y] = 1
# 进行深度优先搜索
DFS(start_x, start_y, 0)
# 打印最短路径长度
print(min_path)