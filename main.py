from turtle import Turtle, Screen
from paddle import paddle
from ball import ball
from scoreboard import scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = paddle((350, 0))
paddle2 = paddle((-350, 0))
ball = ball()
scoreboard = scoreboard()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.delay)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.play_again()
        scoreboard.r_point()
        scoreboard.update_score()
    elif ball.xcor() < -380:
        ball.play_again()
        scoreboard.l_point()
        scoreboard.update_score()








screen.exitonclick()