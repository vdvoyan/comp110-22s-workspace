from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color("Blue")
leo.fillcolor("Blue")
leo.pencolor("Blue")

leo.speed(50)
leo.hideturtle()

leo.up()
leo.goto(-100, -100)
leo.down()

leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()

bob.up()
bob.goto(-100, -100)
bob.down()

bob.speed(100)
bob.hideturtle()

side_length: int = 300

i: int = 0
while (i < 3):
    side_length = side_length * 2
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

done()