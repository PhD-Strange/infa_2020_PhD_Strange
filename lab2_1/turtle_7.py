import turtle
import numpy as np
pi = np.pi
turtle.shape('turtle')
turtle.color('red')
turtle.speed(0)

def arh(n, dfi, k):
	fi = 0
	for i in range(n):
		turtle.forward(k*dfi*(1 + (fi)**2)**(0.5))
		turtle.left(dfi*(180/pi))
		fi+=dfi

arh(1000, 0.1, 20)