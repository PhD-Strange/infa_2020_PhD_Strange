import turtle
import numpy as np
pi = np.pi
turtle.shape('turtle')
turtle.color('red')
n = 3
r = 10
def angel(n, m):
	fi = 360/n
	while n > 0:
		turtle.left(fi)
		turtle.forward(m)
		n-=1

while n < 13:
		m = 2*r*np.sin(pi/n)
		x = (180 - 360/n)/2
		turtle.left(x)
		angel(n, m)
		turtle.right(x)
		turtle.penup()
		turtle.forward(10)
		turtle.pendown()
		n+=1
		r+=10
