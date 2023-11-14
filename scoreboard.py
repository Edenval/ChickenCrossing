from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.levnum = 0
        self.level = f"Level: {self.levnum}"

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(self.level, align="left", font=("Courier", 20, "bold"))

    def increase(self):
        self.levnum += 1
        self.level = f"Level: {self.levnum}"
        self.update_score()

    def game_over(self):
        self.goto(-0, 0)

        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

