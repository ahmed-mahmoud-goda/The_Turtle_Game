from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.num_level = 1
        self.high_score = 0
        with open("high score.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.write(f"Level: {self.num_level}", font=("Ariel", 20, "normal"))
        self.goto(80, 260)
        self.write(f"Highest Level: {self.high_score}", font=("Ariel", 20, "normal"))

    def next_level(self):
        self.num_level += 1
        self.clear()
        self.goto(-270, 260)
        self.write(f"Level: {self.num_level}", font=("Ariel", 20, "normal"))
        self.goto(80, 260)
        self.write(f"Highest Level: {self.high_score}", font=("Ariel", 20, "normal"))

    def end_game(self):
        self.goto(-65, 0)
        self.write(f"Game Over", font=("Ariel", 24, "bold"))
        if self.num_level > self.high_score:
            self.high_score = self.num_level
            with open("high score.txt", mode='w') as data:
                data.write(str(self.high_score))
