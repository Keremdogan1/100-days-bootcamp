import random
from turtle import Turtle


def set_position(snake):
    while True :
        x = float(random.randint(-14,14) * 20)
        y = float(random.randint(-14,14) * 20)
        position = (x, y)
        for part in snake.parts:
            if x == round(part.xcor(), 2) and y == round(part.ycor(), 2):
                position = set_position(snake)
        return position

class Food:
    def create_food(self, snake):
        self.position = set_position(snake)
        food = Turtle("circle")
        food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        food.penup()
        food.color("blue")
        food.goto(self.position)
        return food

    def check(self, snake):
        if round(snake.parts[0].xcor(), 2) == self.position[0] and round(snake.parts[0].ycor(), 2) == self.position[1]:
            self.food.hideturtle()
            snake.add_part()
            self.score += 1
            self.food = self.create_food(snake)
            return True
        return False

    def __init__(self, snake):
        self.position = (0, 0)
        self.food = self.create_food(snake)
        self.score = 0
