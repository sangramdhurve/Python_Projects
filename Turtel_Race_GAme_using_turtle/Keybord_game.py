from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("green")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_all():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key ="c", fun=clear_all)

screen.exitonclick()
