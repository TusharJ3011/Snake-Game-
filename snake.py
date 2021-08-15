from turtle import Turtle

MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        for i in range(0,3):
            xcor = -20 * i
            self.snake_parts.append(self.snake_part_create(xloc=xcor, yloc=0))
        self.head = self.snake_parts[0]

    def snake_part_create(self, xloc, yloc):
        snake = Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        snake.goto(x=xloc, y=yloc)
        return snake

    def move(self):
        for num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[num - 1].xcor()
            new_y = self.snake_parts[num - 1].ycor()
            self.snake_parts[num].goto(x=new_x, y=new_y)
        self.head.forward(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_new_tail(self):
        index = len(self.snake_parts) - 1
        new_xcor = self.snake_parts[index].xcor()
        new_ycor = self.snake_parts[index].ycor()
        self.snake_parts.append(self.snake_part_create(xloc=new_xcor, yloc=new_ycor))



