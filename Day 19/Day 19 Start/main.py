from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def counter_clockwise():
    my_turtle.setheading(my_turtle.heading() + 15)

def clockwise():
    my_turtle.setheading(my_turtle.heading() - 15)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
