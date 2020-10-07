import turtle
turtle.shape('turtle')
def cir(n):#окружность
	for i in range(1, n+1, 1):
		turtle.forward(3)
		turtle.left(360/n)
def pround(n):#полуокружность
	for i in range(n):
		turtle.forward(3)
		turtle.right(180/n)


turtle.penup()
turtle.goto(100, 0)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
cir(200)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
cir(20)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
cir(20)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 40)
turtle.pendown()
turtle.begin_fill()
turtle.color('black')
turtle.left(180)
turtle.width(8)
turtle.forward(30)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 5)
turtle.pendown()
turtle.color('red')
turtle.width(8)
pround(50)

