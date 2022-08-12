from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.forward(20)

    def down(self):
        if self.ycor() >= -270:
            self.backward(20)

    def reset_level(self):
        self.goto(0, -280)
