import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")

score = 0
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{score}/29 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()

        state_data = data[data.state == answer_state]
        xcor = int(state_data.x.item())
        ycor = int(state_data.y.item())

        writer.goto(xcor, ycor)
        writer.write(answer_state, align="center", font=("Arial", 8, "bold"))

        guessed_states.append(answer_state)
        score += 1
