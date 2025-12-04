import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()

food = Food(snake)

score = Scoreboard(food)

is_game_on = True
food_amount = 1

while is_game_on:
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")

    screen.update()
    score.score_update(food)

    time.sleep(0.1)
    snake.move()
    food.check(snake)

    if not snake.check():
        is_game_on = False
        print("\n" * 20)
        print("Game Over!")
        print(f"Final Score: {food.score}")
        score.game_over()









screen.exitonclick()