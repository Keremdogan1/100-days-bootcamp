from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

        file =  open("high_score.txt", mode="r")
        self.high_score = int(file.read())
        file.close()

        self.goto(0, 280)

    def score_update(self, food):
        self.clear()
        self.write(f"Score: {food.score} High Score: {self.high_score}", False, align="center", font=('Arial', 14, 'normal'))

    def score_reset(self, food):
        if food.score > self.high_score:
            self.high_score = food.score
            file = open("high_score.txt", mode="w")
            file.write(str(self.high_score))
        food.score = 0
        self.score_update(food)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!",align="center",  font=('Arial', 28, 'normal'))