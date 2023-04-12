from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-225, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level :{self.score}", align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center",font=FONT)
