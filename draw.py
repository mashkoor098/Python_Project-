import turtle

my_turtle = turtle.Turtle()

my_turtle.forward(100)

my_turtle.speed(300)


def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)


for i in range(100):
    square(100, 90)
    my_turtle.right(6)
