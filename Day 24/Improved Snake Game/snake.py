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
        self.let_rotate = True

    def create_snake(self):
        for i in range(3):
            snake_part = Turtle(shape="square")
            snake_part.shapesize(0.8, 0.8)
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(STARTING_POSITIONS[i])
            self.parts.append(snake_part)

    def add_part(self):
        snake_part = Turtle(shape="square")
        snake_part.shapesize(0.8, 0.8)
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(self.parts[len(self.parts)- 1].xcor(), self.parts[len(self.parts)- 1].ycor())
        self.parts.append(snake_part)

    def is_collusion(self):
        for i in range(1, len(self.parts)):
            if self.parts[0].pos() == self.parts[i].pos():
                return True
        return False

    def check(self):
        if self.parts[0].xcor() >= 300 or self.parts[0].xcor() <= -300 or self.parts[0].ycor() >= 300 or self.parts[0].ycor() <= -300:
            return False
        elif self.is_collusion():
            return False
        else:
            return True

    def right(self):
        if self.parts[0].heading() != LEFT and self.let_rotate:
            self.parts[0].setheading(RIGHT)
            self.let_rotate = False


    def up(self):
        if self.parts[0].heading() != DOWN and self.let_rotate:
            self.parts[0].setheading(UP)
            self.let_rotate = False

    def left(self):
        if self.parts[0].heading() != RIGHT and self.let_rotate:
            self.parts[0].setheading(LEFT)
            self.let_rotate = False

    def down(self):
        if self.parts[0].heading() != UP and self.let_rotate:
            self.parts[0].setheading(DOWN)
            self.let_rotate = False

    def move(self):
        for index in range(len(self.parts) - 1, 0, -1):
            new_pos = self.parts[index - 1].pos()
            self.parts[index].goto(new_pos)

        self.parts[0].forward(MOVE_DISTANCE)
        self.let_rotate = True

    def snake_reset(self):
        for part in self.parts:
            part.goto(1000,1000)
        self.parts.clear()
        self.create_snake()
        self.let_rotate = True
