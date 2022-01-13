from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(left_paddle.go_up, "a")
screen.onkey(left_paddle.go_down, "z")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect  collision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset()

    if ball.xcor() < -380:
        ball.reset()

screen.exitonclick()
