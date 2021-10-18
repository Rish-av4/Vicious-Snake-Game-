from turtle import Turtle, Screen, color, goto, pen, position, shape, width, write

from snake import STARTING_POSITION, Snake
from food import Food
from scoreCard import Scorecard
import turtle
import time

screen = Screen()

screen.setup(width = 800, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# turtle.speed("fastest")


# x_coordinates = [0, -20, -40]
#  We can also use Tuple here -- we can write coordinates in a tuple form.
# starting_positions = [(0,0),(-20,0),(-40,0)]


# segment = []
#   Below are the objects!
snake = Snake()
food = Food()
score = Scorecard()

#  Controlling the Snake with a keypress and creating a method
#  listen keyword is used whenever we want to give keyboard commands.
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# for i in starting_positions:
#     pen = Turtle("square")
#     pen.color("white")
#     pen.penup()
#     pen.goto(i)
#     segment.append(pen)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)

    snake.move()
    #  Detect collision with food.
    if snake.head.distance(food) < 15:
        # print("nom nom nom ")
        food.refresh()
        snake.extend()
        score.increase_score()

    #  Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        game_is_on = False
        score.game_over()

    #  Detect collison with tail
    #  if head collides with any segment in the tail:
    #       trigger game_over
    
    for sega in snake.segment:
        # if snake.head.distance(sega) < 18:
        if sega == snake.head:
            pass

        elif snake.head.distance(sega) < 10:
            game_is_on = False
            score.game_over()

    # for seg_num in range(len(segment)-1 , 0 , -1):
    #     new_x = segment[seg_num -1].xcor()
    #     new_y = segment[seg_num -1].ycor()
    #     segment[seg_num].goto(new_x, new_y)
    # segment[0].forward(20)
    # Detect collison with food!

screen.exitonclick()