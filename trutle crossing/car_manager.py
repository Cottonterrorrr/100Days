from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.shape("square")
        self.start_car()
        self.speedo = 0

    def start_car(self):
        random_pos = random.randint(-250, 250)
        self.goto(300, random_pos)

    def move_car(self):
        self.goto(self.xcor() - MOVE_INCREMENT - self.speedo, self.ycor())

    def speed_up(self):
        self.speedo += MOVE_INCREMENT

