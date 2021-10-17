from random import randint
import turtle
turtle.shape('turtle')

for i in range(0, 10000):

	turtle.forward(randint(0,50))
	turtle.left(randint(0,360))
