import turtle
turtle.shape('turtle')
turtle.color('red')
n = 200
def cir(n, k):
	for i in range(1, n, 1):
		turtle.forward(3)
		turtle.left(360/n)	
	for r in range(1, n, 1):
		turtle.forward(3)
		turtle.right(360/n)

k = 5
for v in range(1, k, 1):
	cir(n, v)
	turtle.left(180/k)