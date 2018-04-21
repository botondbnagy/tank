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
class tank:
    class red:
        spd = 0
        angle = 0
        angSpd = 0
        vel = (0, 0)
        pos = (winW/2, winH/2)
        picture='red.png'
        redimage = pygame.image.load(picture)
        redf = pygame.transform.scale(redimage, (100, 100))
        def update():
            tank.red.angle += tank.red.angSpd
            tank.red.vel = (math.sin(math.radians(tank.red.angle))*tank.red.spd, math.cos(math.radians(tank.red.angle))*tank.red.spd)
            tank.red.pos = add(tank.red.pos, tank.red.vel)
        def draw():
            blitted = pygame.transform.rotate(tank.red.redf, tank.red.angle)
            tank_rect = blitted.get_rect(center=tank.red.pos)
            surface.blit(blitted, tank_rect)
    class blue:
        spd = 0
        angle = 0
        angSpd = 0
        vel = (0, 0)
        pos = (winW/2, winH/2)
        picture='blue.png'
        blueimage = pygame.image.load(picture)
        bluef = pygame.transform.scale(blueimage, (100, 100))
        def update():
            tank.blue.angle += tank.blue.angSpd
            tank.blue.vel = (math.sin(math.radians(tank.blue.angle))*tank.blue.spd, math.cos(math.radians(tank.blue.angle))*tank.blue.spd)
            tank.blue.pos = add(tank.blue.pos, tank.blue.vel)
        def draw():
            blitted = pygame.transform.rotate(tank.blue.bluef, tank.blue.angle)
            tank_rect = blitted.get_rect(center=tank.blue.pos)
            surface.blit(blitted, tank_rect)

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
                    tank.red.spd = -2
                if event.key == K_DOWN:
                    tank.red.spd = 2
                if event.key == K_RIGHT:
                    tank.red.angSpd = -4
                if event.key == K_LEFT:
                    tank.red.angSpd = 4
                if event.key == K_w:
                    tank.blue.spd = -2
                if event.key == K_s:
                    tank.blue.spd = 2
                if event.key == K_d:
                    tank.blue.angSpd = -4
                if event.key == K_a:
                    tank.blue.angSpd = 4
                
            if event.type == KEYUP:
                if event.key == K_UP:
                    tank.red.spd = 0
                if event.key == K_DOWN:
                    tank.red.spd = 0
                if event.key == K_RIGHT:
                    tank.red.angSpd = 0
                if event.key == K_LEFT:
                    tank.red.angSpd = 0
                if event.key == K_w:
                    tank.blue.spd = 0
                if event.key == K_s:
                    tank.blue.spd = 0
                if event.key == K_d:
                    tank.blue.angSpd = 0
                if event.key == K_a:
                    tank.blue.angSpd = 0
            if event.type == VIDEORESIZE:
                        winH = event.h
                        winW = event.w
                        surface = pygame.display.set_mode((winW, winH), RESIZABLE)
        surface.fill((white))
        tank.blue.update()
        tank.blue.draw()
        tank.red.update()
        tank.red.draw()
        pygame.display.update()
        fpsClock.tick(FPS)
main()
