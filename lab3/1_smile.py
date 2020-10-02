import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))#white display

circle(screen, (255, 255, 0), (200, 175), 100)#yellow face

circle(screen, (255, 0, 0), (150, 140), 17)#left eye
circle(screen, (0, 0, 0), (150, 140), 6)#left pupil
circle(screen, (255, 0, 0), (245, 140), 15)#right eye
circle(screen, (0, 0, 0), (245, 140), 6)#right pupil

rect(screen, (0, 0, 0), (150, 200, 100, 20))#mouth
polygon(screen, (0, 0, 0), [(180,135), (183,125),(113,115), (110,125)])#left eyebrow
polygon(screen, (0, 0, 0), [(215,140), (275,120),(273,110), (213,130)])#right eyebrow

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()