import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("skyblue")
screen.title("Rainbow 🌈 with Rain Animation 🌧️")

screen.tracer(0)

rainbow = turtle.Turtle()
rainbow.hideturtle()
rainbow.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
radius = 300
width = 30

rainbow.penup()
rainbow.goto(0, -250)

for color in colors:
    rainbow.color(color)
    rainbow.width(width)
    rainbow.setheading(90)
    rainbow.penup()
    rainbow.goto(0, -230)
    rainbow.forward(radius)
    rainbow.setheading(187)
    rainbow.pendown()
    rainbow.circle(radius, 185)
    radius -= width


raindrops = []

for _ in range(60):
    drop = turtle.Turtle()
    drop.hideturtle()
    drop.speed(0)
    drop.color("white")
    drop.penup()
    drop.goto(random.randint(-500, 500), random.randint(0, 300))
    drop.showturtle()
    raindrops.append(drop)


def rain_animation():
    for drop in raindrops:
        y = drop.ycor()
        y -= random.randint(10, 25)
        if y < -300:
            y = random.randint(200, 400)
            drop.setx(random.randint(-500, 500))
        drop.sety(y)

    screen.update()
    screen.ontimer(rain_animation, 50)

rain_animation()


text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -290)
text.color("black")
text.write(" Rainbow with Rain Animation using Python 🐍", align="center",
           font=("Arial", 18, "bold"))

turtle.done()