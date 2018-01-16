'''
import turtle

def rectangle():
 turtle.penup()
 turtle.goto(x1, y1)
 turtle.goto(x1, y2)
 turtle.pendown()
 turtle.goto(x1, y2 - h)
 turtle.goto(x1, y2 + h)
 turtle.goto(x1 - w, y2 + h)
 turtle.goto(x1 - w, y2 - h)
 turtle.goto(x1, y2 - h)
 turtle.done()

x1, y1 = eval(input("Enter centre co-ordinates of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
height = eval(input("Enter the height of the rectangle: "))
h = height // 2
w = width // 2
x2 = x1 + w
y2 = y1 + h
rectangle()
'''

import turtle

x1, y1 = eval(input("Enter centre co-ordinates of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
height = eval(input("Enter the height of the rectangle: "))
h = height // 2
w = width // 2
x2 = x1 + w
y2 = y1 + h

turtle.penup()
turtle.goto(x1, y1)
turtle.goto(x1, y2)
turtle.pendown()
turtle.goto(x1, y2 - h)
turtle.goto(x1, y2 + h)
turtle.goto(x1 - w, y2 + h)
turtle.goto(x1 - w, y2 - h)
turtle.goto(x1, y2 - h)
turtle.done()

