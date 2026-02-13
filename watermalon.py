import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

t.penup()
t.goto(0, -120)
t.pendown()

t.color("darkgreen", "red")
t.begin_fill()
t.left(140)
t.forward(180)

t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)

t.forward(180)
t.end_fill()

t.penup()
t.goto(0, -110)
t.setheading(0)
t.pendown()

t.color("white")
t.pensize(6)
t.left(140)
t.forward(165)
t.circle(-80, 200)
t.left(120)
t.circle(-80, 200)
t.forward(165)

t.penup()
t.color("black")
for _ in range(12):
    x = random.randint(-60, 60)
    y = random.randint(-20, 80)
    t.goto(x, y)
    t.dot(8)


t.goto(0, -200)
t.color("green")
t.write("Watermelon Love", align="center",
        font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()
