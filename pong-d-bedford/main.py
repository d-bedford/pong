from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
screen = Screen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
score = Score()
ball = Ball()
screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.move_speed /= 1.5

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed /= 1.5

    if ball.xcor() > 340:
        score.clear()
        score.increase_score("p1")
        if score.player_1_score == 11 or score.player_2_score == 11:
            score.check_win()
            game_is_on = False
        else:
            ball.refresh()

    elif ball.xcor() < -340:
        score.clear()
        score.increase_score("p2")
        if score.player_1_score == 11 or score.player_2_score == 11:
            score.check_win()
            game_is_on = False
        else:
            ball.refresh()


screen.exitonclick()
