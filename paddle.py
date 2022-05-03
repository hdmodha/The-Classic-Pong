from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x, y=y)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_ycor)
