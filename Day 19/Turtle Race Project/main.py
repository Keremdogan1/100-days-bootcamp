import random
from turtle import Turtle, Screen

def forward_randomly(turtle):
    number = random.randint(0, 10)
    turtle.forward(number)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles =[]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    turtles[i].penup()
    turtles[i].color(colors[i])

y = -100

for i in range(6):
    turtles[i].goto(x=-230, y=y)
    y += 40

maxx = -230
winner = -1

while maxx <220:
    for i in range(6):
        forward_randomly(turtles[i])
        if turtles[i].xcor() > maxx:
            maxx = turtles[i].xcor()
            winner = i

print(f"Winner is {colors[winner]}!\n")

if user_bet == colors[winner]:
    print("You bet correctly!")
else:
    print("You bet wrongly!")


screen.listen()
screen.exitonclick()
