import turtle
turtle.shape('turtle')
r = 0.005
count = 0

for step in range(0,500):
	turtle.forward(r)
	turtle.left(3.6)
	r = r+0.005

