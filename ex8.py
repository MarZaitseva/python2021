import turtle
turtle.shape('turtle')

step = 0
v = 2
turtle.right(90)

for i in range(0,10):

	for step in range(0,100):
		turtle.forward(v)
		turtle.left(3.6)

	for step in range(0,100):
		turtle.forward(v)
		turtle.right(3.6)

	v = v + 0.5

