import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

def tree(branch_len):
    if branch_len > 20:
       
        t.color("brown")
        t.width(branch_len / 10)
        t.forward(branch_len)

      
        t.left(30)
        tree(branch_len - 20)

      
        t.right(60)
        tree(branch_len - 20)

      
        t.left(30)
        t.backward(branch_len)
    else:
      
        t.color("green")
        t.begin_fill()
        t.circle(8)
        t.end_fill()

      
        if random.randint(1, 3) == 1:
            t.color("red")
            t.begin_fill()
            t.circle(5)
            t.end_fill()

tree(100)
turtle.done()