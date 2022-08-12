from turtle import Turtle , Screen
import time
from level import Level
from player import Player
from cars import Car
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.title("The Turtle Game")
screen.listen()

player = Player()
score_level = Level()
car = Car()

screen.onkeypress(player.up,"Up")
screen.onkeypress(player.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    car.create_cars()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(player)<20:
            score_level.end_game()
            game_is_on = False
    if player.ycor()>=280:
        score_level.next_level()
        player.reset_level()
        car.speed_increase()









screen.exitonclick()