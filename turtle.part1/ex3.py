import turtle

turtle.shape('turtle')

number = 0
step = 20
n = 5
k = 2

for number in range(0, 10):
	if number == 0:
		turtle.forward(step)
		turtle.left(90)
		turtle.forward(step)
		turtle.left(90)
		turtle.forward(step)
		turtle.left(90)
		turtle.forward(step)
	else :	
		turtle.forward(step + n*k)
		turtle.left(90)
		turtle.forward(step + n*k)
		turtle.left(90)
		turtle.forward(step + n*k)
		turtle.left(90)
		turtle.forward(step + n*k)
		k = k+2
	turtle.penup()
	turtle.forward(n)
	turtle.right(90)
	turtle.forward(n)
	turtle.right(90)
	turtle.right(90)
	turtle.right(90)
	turtle.right(90)
	turtle.right(90)
	turtle.right(90)

	turtle.pendown()

	number = number + 1
	 
	 

turtle.done()
