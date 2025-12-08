import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()

state_data = pandas.read_csv("50_states.csv")
list_of_states = state_data["state"].to_list()

remained_states = list_of_states
answered_states = []
correct_answers = 0

while correct_answers < 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in list_of_states and answer_state not in answered_states:
        x = state_data[state_data["state"] == answer_state].x.item()
        y = state_data[state_data["state"] == answer_state].y.item()
        writer_turtle.goto(x, y)
        writer_turtle.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))
        correct_answers += 1
        answered_states.append(answer_state)
        remained_states.remove(answer_state)
    elif answer_state.lower() == "exit":
        unknown_states = {"state": remained_states}
        data = pandas.DataFrame(unknown_states)
        data.to_csv("unknown_states.csv")
        break
    
    turtle.mainloop
    