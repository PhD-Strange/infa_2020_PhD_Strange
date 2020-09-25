import turtle

t = turtle.Turtle()

font = {
    0: [[0,0], [1,0]],
    1: [[0,0], [0,1]],
    2: [[1,0], [0,1]],
    3: [[1,0], [1,1]],
    4: [[0,1], [1,1]],
    5: [[0,1], [0,2]],
    6: [[1,1], [0,2]],
    7: [[1,1], [1,2]],
    8: [[0,2], [1,2]],
    9: [[.6,1.8], [.4,2.2]],
}

digits = {
        #[0,1,2,3,4,5,6,7,8,9]
    '0': [1,1,0,1,0,1,0,1,1,0],
    '1': [0,0,1,1,0,0,0,1,0,0],
    '2': [1,0,0,1,0,0,1,0,1,0],
    '3': [1,0,1,0,1,0,1,0,0,0],
    '4': [0,1,0,1,1,0,0,1,0,0],
    '5': [1,1,0,0,1,0,0,1,1,0],
    '6': [0,0,1,0,1,1,0,1,1,0],
    '7': [1,0,1,0,0,1,0,0,0,0],
    '8': [1,1,0,1,1,1,0,1,1,0],
    '9': [1,1,0,1,1,0,1,0,0,0],
    '.': [0,0,0,0,0,0,0,0,0,1]
}

def move(x,y):
	t.up()
	t.goto(x,y)
	t.down()
	
def go_stick(pos0, l, pos1, pos2):
    move(pos0[0] + pos1[0] * l, pos0[1] - pos1[1] * l)
    t.goto(pos0[0] + pos2[0] * l, pos0[1] - pos2[1] * l)
    
def drawdigit(pos, n, l):
    for i in range(len(font)):
        if digits[n][i]>0:
            go_stick(pos, l, font[i][0], font[i][1])

def drawnumber(n, pos, l, dl):
    for i in range(len(str(n))):
        drawdigit([(l + dl)*(i - 1) + pos[0], 0 + pos[1]], str(n)[i], l)

turtle.clearscreen()
t = turtle.Turtle()
t.reset()

tmp = {}
with open("font.txt") as f:
    for i,line in enumerate(f):
        a,b,c,d = [float(num) for num in line.split()]
        tmp[i] = [[a,b],[c,d]]
font = tmp

drawnumber("141700", [0,0], 20, 5)
