import turtle
import numpy as np
import math

turtle.shape('turtle')

n = 3
side = 100

for i in range(0, 10):

	corner = 180*(n-2)/n
	r1 = side/(2*np.sin(180/n*(math.pi)/180))
	r2 = (side+20)/(2*np.sin(180/(n+1)*(math.pi)/180))

	turtle.left(180-corner/2)
	turtle.forward(side) 

	for m in range(0, n-1):
		turtle.left(180-corner)
		turtle.forward(side)
	#turtle.left(180-corner)
	#turtle.forward(100)

	turtle.penup()
	turtle.right(corner/2)
	turtle.forward(r2-r1)
	turtle.pendown()

	n = n+1
	side = side+20