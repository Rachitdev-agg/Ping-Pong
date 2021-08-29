from turtle import Turtle
class paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def go_up(self):
        newy = self.ycor() + 50
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 50
        self.goto(self.xcor(), newy)