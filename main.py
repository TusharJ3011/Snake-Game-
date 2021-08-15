import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('red')
my_screen.title('Snake Game')
my_screen.listen()
my_screen.tracer(0)

snake = Snake()

food = Food()
food.new_loc()

score_board = ScoreBoard()


def food_collision():
    if snake.head.distance(food) < 15:
        food.new_loc()
        snake.add_new_tail()
        score_board.score += 1
        score_board.high_score()


def body_collision(game_is_on):
    length = len(snake.snake_parts)
    for i in range(1, length):
        if snake.head.distance(snake.snake_parts[i]) < 10:
            return True
    return False


def wall_collision(game_is_on):
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 280 or snake.head.ycor() <= -290:
        return True
    return False


game_is_on = True
body_col = False
wall_col = False
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_screen.onkey(key='Up', fun=snake.up)
    my_screen.onkey(key='Down', fun=snake.down)
    my_screen.onkey(key='Left', fun=snake.left)
    my_screen.onkey(key='Right', fun=snake.right)
    snake.move()
    food_collision()
    score_board.update()
    body_col = body_collision(game_is_on)
    wall_col = wall_collision(game_is_on)
    if body_col or wall_col:
        game_is_on = False
    else:
        game_is_on = True

score_board.game_over()


my_screen.exitonclick()
