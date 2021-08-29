from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.delay = 0.1
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    def bounce_y(self):
        self.y_move *= -1
        self.delay *= 0.9
    def bounce_x(self):
        self.x_move *= -1
        self.delay *= 0.9
    def play_again(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.delay = 0.1