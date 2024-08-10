from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()

image = "blank_states_img.gif"

screen.title("U.S states")

screen.addshape(image)
turtle.shape(image)

file = pandas.read_csv("50_states.csv")
all = file.state.to_list()
state_list = file.state.to_list()
guessed = []

while(len(guessed)<50):
    user_input = screen.textinput(title=f"{len(guessed)}/50",prompt="Enter the State:").title()

    if user_input == "Exit":
        break

    if user_input in all:
        a=(file[file["state"] == user_input])
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(a.x.item(),a.y.item())
        tim.write(user_input)
        guessed.append(user_input)
        state_list.remove(user_input)

csv = pandas.DataFrame(state_list)
file_csv = csv.to_csv("States You Missed")



screen.exitonclick()