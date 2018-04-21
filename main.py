from pygame.locals import *
import pygame, sys, random, math, time
pygame.init()

FPS=60
fpsClock=pygame.time.Clock()

winW=1000
winH=700
surface = pygame.display.set_mode((winW, winH), RESIZABLE)
pygame.display.set_caption('Tank')

black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
grey=(147, 147, 147)

font = pygame.font.Font(None, 36)
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])
def triadd(a, b, c):
    return (a[0] + math.cos(c)*b[0], a[1] + math.cos(c)*b[1])
class tank:
    class red:
        spd = 0
        angle = 0
        angSpd = 0
        vel = (0, 0)
        pos = (winW/2, winH/2)
        picture='red.png'
        redimage = pygame.image.load(picture)
        redf = pygame.transform.scale(redimage, (124, 180))
        def update():
            tank.red.angle += tank.red.angSpd
            tank.red.pos = triadd(tank.red.pos, tank.red.vel, tank.red.angle)
            surface.blit(tank.red.redf, tank.red.pos) 
    class blue:
        spd = 0
        angle = 0
        angSpd = 0
        vel = (0, 0)
        pos = (winW/2, winH/2)
        picture='blue.png'
        blueimage = pygame.image.load(picture)
        bluef = pygame.transform.scale(blueimage, (124, 180))
        def update():
            tank.blue.pos = add(tank.blue.pos, tank.blue.vel)
            surface.blit(tank.blue.bluef, tank.blue.pos) 

def main():
    global surface
    surface.fill((white))
    while 1:
        events = pygame.event.get
        for event in events():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    tank.red.vel = (0, -1)
                if event.key == K_DOWN:
                    tank.red.vel = (0, 1)
                if event.key == K_RIGHT:
                    pass
                if event.key == K_LEFT:
                    pass
                
            if event.type == KEYUP:
                if event.key == K_UP:
                    tank.red.vel = (0, 0)
                if event.key == K_DOWN:
                    tank.red.vel = (0, 0)
                if event.key == K_RIGHT:
                    pass
                if event.key == K_LEFT:
                    pass
            if event.type == VIDEORESIZE:
                        winH = event.h
                        winW = event.w
                        surface = pygame.display.set_mode((winW, winH), RESIZABLE)
        surface.fill((white))
        tank.blue.update()
        tank.red.update()
        pygame.display.update()
        fpsClock.tick(FPS)
main()
