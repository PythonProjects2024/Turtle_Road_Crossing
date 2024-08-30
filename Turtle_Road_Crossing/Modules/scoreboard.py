from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.update_score()


    def update_score(self):
        self.goto(-210, 250)
        self.write(f"Level: {self.level}" , align='center', font=(FONT))

    def increase_score(self):
        self.score += 1
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=(FONT))





