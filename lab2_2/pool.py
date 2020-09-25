from random import randint, random
import turtle

x_max, y_max = 300, 300
def box(t):
    t.goto(0, 0)
    t.penup()
    t.forward(x_max)
    t.pendown()
    t.right(90)
    t.forward(y_max)
    t.right(90)
    t.forward(x_max*2)
    t.right(90)
    t.forward(y_max*2)
    t.right(90)
    t.forward(x_max*2)
    t.right(90)
    t.forward(y_max)
    t.penup()
    t.left(90)
    t.goto(0, 0)


number_of_turtles = 20
dt = 0.5

pool = [[turtle.Turtle(shape='circle'), randint(-290, 290), randint(-290, 290), 
         randint(-10, 10), randint(-10, 10)]   for i in range(number_of_turtles)]

box(pool[0][0])

for unit in pool:
    unit[0].penup()
    unit[0].speed(0)
    unit[0].goto(unit[1], unit[2])
    
while True:
    for unit in pool:
        unit[1] += unit[3]*dt
        unit[2] += unit[4]*dt
        unit[0].goto(unit[1], unit[2])
        
        if abs(unit[2]) >= y_max:
            unit[4] *= -1
        if abs(unit[1]) >= x_max:
            unit[3] *= -1
            
