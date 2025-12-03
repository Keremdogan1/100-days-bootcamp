from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(STARTING_POSITIONS[i])
            self.parts.append(snake_part)

    def right(self):
        if self.parts[0].heading() != LEFT:
            self.parts[0].setheading(RIGHT)

    def up(self):
        if self.parts[0].heading() != DOWN:
            self.parts[0].setheading(UP)

    def left(self):
        if self.parts[0].heading() != RIGHT:
            self.parts[0].setheading(LEFT)

    def down(self):
        if self.parts[0].heading() != UP:
            self.parts[0].setheading(DOWN)

    def move(self):
        for index in range(len(self.parts) - 1, 0, -1):
            new_pos = self.parts[index - 1].pos()
            self.parts[index].goto(new_pos)

        self.parts[0].forward(MOVE_DISTANCE)

