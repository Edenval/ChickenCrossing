from turtle import Turtle, Screen
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#from 300x to -300x
#generate random from 300 y to -300y

class CarManager():
    def __init__(self):
        self.all_cars = []
        # self.move_speed = MOVE_INCREMENT
        self.move_speed = STARTING_MOVE_DISTANCE
    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.random_y = random.randint(-250, 250)
            new_car.goto(300, new_car.random_y)
            self.all_cars.append(new_car)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT