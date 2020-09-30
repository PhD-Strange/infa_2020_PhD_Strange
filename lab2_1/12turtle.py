import turtle
turtle.shape('turtle')
turtle.color('red')
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)
def round(n):
	for i in range(n):
		turtle.forward(3)
		turtle.right(180/n)

k = 10#число витков
for g in range(k):
	round(50)
	round(10)
	