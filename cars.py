from turtle import Turtle
import random

colors = ["red", "orange", "blue", "black", "brown", "yellow", "green"]
move_increment = 1


class Car:
    def __init__(self):
        self.all_cars = []
        self.distance_move = 5

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.distance_move)

    def speed_increase(self):
        self.distance_move += move_increment
