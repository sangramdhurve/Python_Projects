from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('red')
# drawing a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Drawing the dashed line
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()
#     #timmy_the_turtle.left(45)
# drawing the all angles and triangle
# for _ in range(3):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# for _ in range(5):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)
# for _ in range(6):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
# for _ in range(7):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/7)
# for _ in range(8):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/8)
# for _ in range(9):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/9)
# for _ in range(10):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)


# short code for this with color
# colors = ["blue", "navy", "orange red", "peach puff", "blue violet", "orchid"]
#
#
# def angles(number_of_side):
#     side = 360/number_of_side
#     for _ in range(number_of_side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(side)
#
#
# for number_of_side in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     angles(number_of_side)

# Screen.colormode(cmode=255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
#
#
# directions = [0, 90, 180, 270]
# for _ in range(300):
#     timmy_the_turtle.width(15)
#     timmy_the_turtle.speed(25)
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.color(random_color())

# Drawing a circle:


for _ in range(19):
    timmy_the_turtle.speed(10)
    timmy_the_turtle.circle(70)
    timmy_the_turtle.left(20)







screen = Screen()
screen.exitonclick()
