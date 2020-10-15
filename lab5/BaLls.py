#import pygame as pg
#import random as rnd
#import sys
import os


#size = width, height = 1000, 600

#white = 255, 255, 255

#screen = pg.display.set_mode(size)

#game_folder = os.path.dirname(__file__)
#img_folder = os.path.join(game_folder, 'images')
#ball = pg.image.load(os.path.join(img_folder, 'ball.png'))

#ball_1 = ball.get_rect(center=(rnd.randint(200, 400), rnd.randint(200, 400)))
#ball_2 = ball.get_rect(center=(rnd.randint(90, 180), rnd.randint(90, 180)))

#speed_1 = [2, 2]
#speed_2 = [2, 2]

#clock = pg.time.Clock()

#while 1:
    #for event in pg.event.get():
        #if event.type == pg.QUIT:
            #sys.exit()

####
    #ball_1 = ball_1.move(speed_1)
    #if ball_1.left < 0 or ball_1.right > width:
        #speed_1[0] = -speed_1[0]

    #if ball_1.top < 0 or ball_1.bottom > height:
        #speed_1[1] = -speed_1[1]

####
    #ball_2 = ball_2.move(speed_2)
    #if ball_2.left < 0 or ball_2.right > width:
        #speed_2[0] = -speed_2[0]

    #if ball_2.top < 0 or ball_2.bottom > height:
        #speed_2[1] = -speed_2[1]

####
    #screen.fill(white)
    #screen.blit(ball, ball_1)
    #screen.blit(ball, ball_2)
    #pg.display.flip()
    #clock.tick(50)
    
    
#####################
import pygame as pg
import random as rnd
import sys


class Ball:
    def __init__(self, x, y, dx, dy, image):
        #print(x, y, dx, dy)
        self.img = pg.transform.scale(image, (150, 150))
        self.dx = dx
        self.dy = dy
        self.rect = screen.blit(self.img, (x, y))
        return

    def show(self):
        screen.blit(self.img, self.rect)

    def move(self):
        self.rect = self.rect.move([self.dx, self.dy])
        self.show()
        return

    def check_collide_with_walls(self, left_x, right_x, top_y, bottom_y):
        if self.rect.left < left_x or self.rect.right > right_x:
            self.dx *= -1

        if self.rect.top < top_y or self.rect.bottom > bottom_y:
            self.dy *= -1
        return

    def check_click(self, coords):
        if self.rect.left < coords[0] and self.rect.right > coords[0] and self.rect.top < coords[1]\
                and self.rect.bottom > coords[1]:
            return True
        return False


size = width, height = 1000, 600
white = 255, 255, 255

screen = pg.display.set_mode(size)

circles = ("intro_ball.gif", "football_new.png", "basketball.png")

balls_array = []
balls_n = 5

#!!!!!!!!!!!!!
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
#!!!!!!!!!!!!!!
for i in range(balls_n):
    balls_array.append(Ball(rnd.randint(100, width-100),
                            rnd.randint(100, height-100),
                            rnd.randint(1, 6),
                            rnd.randint(1, 6), pg.image.load(os.path.join(img_folder, 'ball.jpg'))))

    #!!!!!!!!!!!!!!!!!pg.image.load(rnd.choice(circles))))


clock = pg.time.Clock()

FLAAAG = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            for ball in balls_array:
                if ball.check_click(event.pos):
                    FLAAAG += 1
                    break

            print(FLAAAG)

    #check_exit_event()
    screen.fill(white)

    for ball in balls_array:
        ball.move()
        ball.check_collide_with_walls(0, width, 0, height)

    pg.display.flip()
    clock.tick(30)
