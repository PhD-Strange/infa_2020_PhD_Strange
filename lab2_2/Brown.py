import turtle
from random import *
turtle.shape('turtle')
turtle.color('red')
n = randint(1,100)
for i in range(n):
    fi = random()
    r = random()
    k = random()
    if k>0.5:
        turtle.forward(100*r)
        turtle.left(180*fi)
    else:
        turtle.forward(100*r)
        turtle.right(180*fi)
