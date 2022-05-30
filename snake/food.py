from turtle import Turtle
import numpy as np


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = np.random.random_integers(-280, 280)
        random_y = np.random.random_integers(-280, 280)
        self.goto(random_x, random_y)
