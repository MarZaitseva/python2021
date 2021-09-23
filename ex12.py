import turtle
import numpy as np
import math

turtle.shape('turtle')

n = 5

turtle.left(90)

#for i in range(0, n):

turtle.right(180/n)
turtle.forward(60)

for i in range(0, n):

	turtle.right(180-180/n)
	turtle.forward(60)

turtle.done()