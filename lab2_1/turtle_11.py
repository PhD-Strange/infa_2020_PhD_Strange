import turtle
turtle.shape('turtle')
turtle.color('red')
turtle.left(90)
def cir(n):
	for i in range(1, n+1, 1):
		turtle.forward(2)
		turtle.left(360/n)	
	for r in range(1, n+1, 1):
		turtle.forward(2)
		turtle.right(360/n)

n = 210
for v in range(70, n, 20):
	cir(v)