import turtle as t


y_max = 300
x_max = 300

ay = -10
dt = 0.1

x, y, Vx, Vy = 0, 0, 10, 0

while True:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2 
    Vy += ay*dt
    t.goto(x, y)
    if abs(y) >= y_max and Vy<0:
        Vy *= -0.9
        print(y, Vy)
    if abs(x) >= x_max:
        Vx *= -1
