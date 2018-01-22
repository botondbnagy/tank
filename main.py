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
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_RIGHT:
                    pass
                if event.key == K_LEFT:
                    pass
                
            if event.type == KEYUP:
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_RIGHT:
                    pass
                if event.key == K_LEFT:
                    pass
            if event.type == VIDEORESIZE:
                        winH = event.h
                        winW = event.w
                        surface = pygame.display.set_mode((winW, winH), RESIZABLE)
        surface.fill((white))
        pygame.display.update()
        fpsClock.tick(FPS)
main()
