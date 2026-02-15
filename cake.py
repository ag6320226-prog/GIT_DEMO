import turtle

t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("lightyellow")


t.penup()
t.goto(-150, -100)
t.pendown()

t.color("brown", "pink")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.left(90)
    t.forward(120)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-120, 20)
t.pendown()

t.color("brown", "white")
t.begin_fill()
for i in range(2):
    t.forward(240)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

x = -80
for i in range(5):
    t.penup()
    t.goto(x, 100)
    t.pendown()
    t.color("blue")
    t.setheading(90)
    t.forward(40)

    t.penup()
    t.goto(x, 140)
    t.pendown()
    t.color("orange")
    t.circle(6)
    x += 40


t.penup()
t.goto(-90, -40)
t.color("black")
t.write("HAPPY BIRTHDAY ", font=("Arial", 18, "bold"))

t.hideturtle()
turtle.done()