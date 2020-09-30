import turtle
turtle.shape('turtle')
turtle.color('red')
def sarh(n, k):
	for i in range(n):
		turtle.forward(k*i)
		turtle.left(90)
		
sarh(30, 5)