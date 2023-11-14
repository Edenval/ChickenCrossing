import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
scoreboard = Scoreboard()

# I NEED TO MAKE A CAR OBJECT EVERY 6TH TIME THE LOOP RUNS
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 300:
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.increase()

    # for i in range (0, 6):
    #     time.sleep(0.1)
    #     screen.update()
screen.exitonclick()