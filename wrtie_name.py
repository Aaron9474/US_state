from turtle import Turtle

class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    def write_state(self,x_cor,y_cor,state):
        self.goto(x_cor,y_cor)
        self.write(f"{state}", font=('Arial', 6, 'bold'))