import turtle
turtle.shape('circle')

dt = 0.05
g = 10
y = 0
x = 0
vx = 10
vy = 80
dx = vx*dt


def dy():

	if vy >= 0:

		y = vy*dt - g*(dt)**2/2


	else :

		y = vy*dt - g*(dt)**2/2

	return y


for i in range(0,1210):

	y = y + dy()

	vy = vy - g*dt

	x = x + dx 

	vx = vx-2

	if y <= 0:

		y = 0

		vy = -vy-10

	turtle.goto(x, y)

	


turtle.done()









