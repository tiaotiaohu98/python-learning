from random import *
from tkinter import *
from math import *
import time


class Ball:

    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas  # 创建画布
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 创建小球对象
        self.canvas.move(self.id, winW / 2, winH / 2)  # 创建小球初始位置
        start_pos = [-4. - 3, -2, -1, 0, 1, 2, 3, 4]  # 球最初x轴位移的随机数
        shuffle(start_pos)
        self.x = start_pos[0]
        self.y = -step
        self.notTouchButton = True

    # 击球函数
    def hitRacket(self, ballPos):
        racketPos = self.canvas.coords(self.racket.id)  # 获取球的位置
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False

    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)
        ballPos = self.canvas.coords(self.id)

        # 球不能超过画布范围
        if ballPos[0] <= 0:
            self.x = step
        if ballPos[1] <= 0:
            self.y = step
        if ballPos[2] >= winW:
            self.x = -step
        if ballPos[3] >= winH:
            self.y = -step

        # 判断球是否碰到了球拍
        if self.hitRacket(ballPos) == True:
            self.y = -step
        if ballPos[3] >= winH:
            self.notTouchButton == False


class Racket:

    def __init__(self, canvas, color):
        self.canvas = canvas
        # 获取球拍对象id
        self.id = canvas.create_rectangle(0, 0, 100, 15, fill=color)

        # 获取球拍位置
        self.canvas.move(self.id, 270, 400)
        self.x = 0

        # 绑定球拍,通过键盘上下左右键控制球拍的移动
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)

    # 球拍移动
    def racketMove(self):
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:
            self.x = 0
        elif racketPos[2] >= winW:
            self.x = 0

    # 球拍向左移动
    def moveLeft(self, event):
        self.x = -5

    # 球拍向右移动
    def moveRight(self, event):
        self.x = 5


winW, winH = 640, 480
step, speed = 3, 0.03

# 创建一个TKinter对象
tk = Tk()
# 设定游戏标题窗口
tk.title('蛋球游戏')

# 设定游戏窗口在屏幕最上层
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')
ball = Ball(canvas, 'yellow', winW, winH, racket)

while True:
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)
