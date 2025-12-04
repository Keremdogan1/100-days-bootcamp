from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, food):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def score_update(self, food):
        self.clear()
        self.write(f"Score = {food.score}", False, align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!",align="center",  font=('Arial', 28, 'normal'))