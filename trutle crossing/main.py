import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

cars = [CarManager()]

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for c in cars:
        c.move_car()
        if player.distance(c) < 10:
            scoreboard.game_over()

    if counter == 6:
        cars.append(CarManager())
        counter = 1

    if player.ycor() > 260:
        player.refresh()
        scoreboard.increase_score()
        for c in cars:
            c.speedo += 5
    counter += 1

