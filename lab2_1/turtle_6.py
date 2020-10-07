import turtle
turtle.shape('turtle')
turtle.color('red')
def spider(n):
	for i in range(n):
		turtle.forward(100)
		turtle.stamp()
		turtle.backward(100)
		turtle.left(360/n)
	
spider(15)
	