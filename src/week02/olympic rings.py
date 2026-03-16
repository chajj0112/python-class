# 과제 3

import turtle

t = turtle.Turtle()
t.width(5)

# blue
t.color("blue")
t.penup()
t.goto(-110, -25)
t.pendown()
t.circle(45)

# black
t.color("black")
t.penup()
t.goto(0, -25)
t.pendown()
t.circle(45)

# red
t.color("red")
t.penup()
t.goto(110, -25)
t.pendown()
t.circle(45)

# yellow
t.color("yellow")
t.penup()
t.goto(-55, -70)
t.pendown()
t.circle(45)

# green
t.color("green")
t.penup()
t.goto(55, -70)
t.pendown()
t.circle(45)

turtle.done()