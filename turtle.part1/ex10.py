import turtle
turtle.shape('turtle')

step = 0
turtle.fillcolor('yellow')
turtle.begin_fill()
#turtle.color('black' ,'yellow')

for step in range(0,100):
	turtle.forward(10)
	turtle.left(3.6)
	
#turtle.color('black' ,'yellow')

turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()

for step in range(0,100):
	turtle.forward(2)
	turtle.left(3.6)

turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(40)
turtle.left(90)

turtle.fillcolor('blue')
turtle.begin_fill()

for step in range(0,100):
	turtle.forward(2)
	turtle.right(3.6)

turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(70)

turtle.pendown()
turtle.pensize(5)
turtle.forward(30)

turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(90)

turtle.pendown()
turtle.pensize(5)
turtle.pencolor('red')

for step in range(0,50):
	turtle.forward(3.5)
	turtle.left(3.6)

