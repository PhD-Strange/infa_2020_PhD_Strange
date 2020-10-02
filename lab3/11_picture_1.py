import pygame
from pygame.draw import *
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 700))

#screen
rect(screen, (255, 255, 255), (0, 300, 400, 400))
rect(screen, (211, 211, 211), (0, 0, 400, 300))

#igloo with radius equals r and coordinats of center is (x, y)
def igloo(r, x, y) :
    n = round(r / 4)
    arc(screen, (211, 211, 211), [x-r, y-r, 2*r, 2*r], 0, pi, r)#filling
    arc(screen, (0, 0, 0), [x-r, y-r, 2*r, 2*r], 0, pi)#Contour
    for i in range(0, r, n):
        t = r * (1 - (i / r)**2 )**(1/2)
        line(screen, (0, 0, 0), (x - t, y - i), (x + t, y - i))
        for g in range(4, 0, -1):
            line(screen, (0, 0, 0), (x - t + t/5, y - i), (x - t + t/5, y - i - n))
  
 
        
#eskimo with height equals h and coordinats of head is (x, y)
def eskimo(h, x, y):
    circle(screen, (211, 211, 211), (x, y), round(h/3))
    #body
    arc(screen, (139, 121, 94), [x - round(h/3), y, 2*round(h/3), 2*h], 0, pi, round(h/3))#filling
    arc(screen, (0, 0, 0), [x - round(h/3), y, 2*round(h/3), 2*h], 0, pi)#Contour   
    
    #face
    circle(screen, (105, 105, 105), (x, y), round(h/4))
    circle(screen, (211, 211, 211), (x, y), round(h/5))    
    



#cat with coordinats equal (x, y)
#def cat(x, y):
    



pi = np.pi
igloo(100, 170, 350)

eskimo(100, 250, 450)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()