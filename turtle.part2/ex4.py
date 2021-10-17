from random import randint
import turtle
import math


turtle.penup()
turtle.right(90)
turtle.forward(225)
turtle.right(90)
turtle.forward(225)
turtle.left(180)
turtle.pendown()

t = turtle.Pen()
t.pencolor('black')
turtle.forward(450)
turtle.left(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(450)

wn = turtle.Screen()
leftBound = -wn.window_width() / 200
rightBound = wn.window_width() / 200
topBound = wn.window_width() / 200
bottomBound = -wn.window_width() / 200




number_of_turtles = 80
steps_of_time_number = 100


pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_turtles)]

for unit in pool:
	unit.penup()
	unit.speed(0)
	unit.goto(randint(-200,200), randint(-200,200))

for i in range(steps_of_time_number):
	for unit in pool:

		if unit.xcor() >= 200 and math.fabs(unit.ycor()) < 200:

			unit.goto(150, unit.ycor())

		if unit.xcor() <= -200 and math.fabs(unit.ycor()) < 200:

			unit.goto(-150, unit.ycor())

		if unit.ycor() >= 200 and math.fabs(unit.xcor()) < 200:

			unit.goto(unit.xcor(), 150)

		if unit.ycor() <= -200 and math.fabs(unit.xcor()) < 200:

			unit.goto(unit.xcor(), -150)

		unit.forward(10)
		unit.left(randint(0,360))
		unit.forward(10)

turtle.tracer(5, 0)