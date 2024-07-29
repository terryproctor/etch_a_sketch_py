from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear():
    timmy.clear()
    home()

def home():
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen = Screen()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear, "c")
screen.onkeypress(home, "h")

screen.exitonclick()



