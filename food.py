from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.speed(10)
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)

    def new_loc(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 260)
        self.goto(x=new_x, y=new_y)
