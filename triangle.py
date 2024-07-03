import turtle as t
import math as m
import random

def difference(value1, value2):
    return value1 - value2 if (value1 - value2 > 0) else value2 - value1

wn = t.Screen()
wn.bgcolor('#000000')

drawer = t.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)
drawer.color('#FFFFFF')
drawer.sety(drawer.ycor()-300)
drawer.pendown()
drawer.circle(300)
drawer.pensize(0.1)
drawer.penup()

positions = [(0, 300), (259.8076211353, -150), (-259.8076211353, -150)]


drawer.setposition(random.randint(-100, 100), random.randint(-100, 100))

while True:
    position = positions[random.randint(0, 2)]
    drawer.setheading(drawer.towards(position))
    d = m.sqrt(m.pow(difference(drawer.xcor(), position[0]), 2) + m.pow(difference(drawer.ycor(), position[1]), 2))
    drawer.forward(d/2)
    drawer.dot()
