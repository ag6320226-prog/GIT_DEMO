import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")


t.color("orange")
for i in range(36):
    t.circle(100)
    t.left(170)


t.penup()
t.goto(0, -20)
t.pendown()
t.color("brown")

t.begin_fill()
t.circle(28)
t.end_fill()


t.penup()
t.goto(0, -60)
t.setheading(-90)
t.pendown()
t.color("green")
t.pensize(8)
t.forward(200)


t.pensize(3)
t.left(45)
t.circle(60, 90)
t.penup()
t.goto(0, -140)
t.setheading(-135)
t.pendown()
t.circle(60, 90)

t.hideturtle()
turtle.done()