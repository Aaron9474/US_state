from turtle import Turtle,Screen
import pandas
from wrtie_name import Pen

turtle = Turtle()
screen = Screen()
w_state = Pen()
df = pandas.read_csv("50_states.csv")
screen.title("U.S. Sate Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
play_time = df.count().iloc[0]
Lis = []

while len(Lis) < play_time:
    u_answer = screen.textinput(title=f"{len(Lis)}/50 State Correct", prompt="What's the next state?").title()
    if u_answer == "Exit":
        break
    if df["state"].isin([u_answer]).any():
        d_state =df[df["state"]== u_answer]
        x_state_v = d_state["x"].iloc[0]
        y_state_v = d_state["y"].iloc[0]
        w_state.write_state(x_state_v,y_state_v,u_answer)
    else:
        pass
gues_state = pandas.DataFrame(Lis, columns=["State"])
mis_state = pandas.concat([df["state"],gues_state]).drop_duplicates(keep=False)
mis_state.to_csv("Missing State.csv", index = False)

screen.exitonclick()