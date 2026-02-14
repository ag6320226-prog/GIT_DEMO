import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("white")

t.penup()
t.goto(-250, -50)
t.setheading(0)
t.pendown()

t.color("#8B4513", "#D2691E") 
t.begin_fill()
for _ in range(2):
    t.forward(500)
    t.left(90)
    t.forward(30)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-180, -35)
t.color("black")
for _ in range(8):
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.forward(50)

t.goto(-260, -40)
t.color("#5A2D0C")
t.begin_fill()
t.circle(15)
t.end_fill()

t.goto(-230, 4)
t.setheading(80)
t.color("darkgreen")
t.pensize(4)

for i in range(3):
    t.circle(60, 60)

t.goto(-210, 80)
t.color("green", "green")
t.begin_fill()
t.circle(30)
t.end_fill()

t.goto(-210, 90)
t.color("blue", "blue")
t.begin_fill()
t.circle(15)
t.end_fill()

t.goto(-210, 95)
t.color("navy", "navy")
t.begin_fill()
t.circle(7)
t.end_fill()

t.goto(-100, -120)
t.color("darkgreen")
t.write(" Jay Shri Krishna", align="center",
        font=("Arial", 18, "bold"))

turtle.done()






