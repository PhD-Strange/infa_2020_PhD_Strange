import turtle
turtle.shape('turtle')
turtle.color('red')
def star(n):
	for i in range(n):
		turtle.forward(150)
		angel = n//2*360/n
		turtle.right(angel)

star(5)
turtle.color('blue')
star(11)