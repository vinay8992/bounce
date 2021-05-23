import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
s=Screen()
s.bgcolor("black")
s.title("game")
s.setup(width=800,height=400)
s.tracer(0)
l_paddle=Paddle((780, 0))
r_paddle=Paddle((-780, 0))
ball=Ball()
score=Score()
s.listen()
s.onkeypress(l_paddle.go_up,"Up")
s.onkeypress(l_paddle.go_down,"Down")
s.onkeypress(r_paddle.go_up,"w")
s.onkeypress(r_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor()>380 or ball.ycor()<-380:
        ball.bounce_y()
    if ball.distance(l_paddle)<50 and ball.xcor()>340 or ball.distance(r_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()
    if ball.xcor()>780:
        ball.reset_position()
        score.r_point()
    if ball.xcor()<-780:
        ball.reset_position()
        score.l_point()
s.exitonclick()