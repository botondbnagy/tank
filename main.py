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

bulletList = []

def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def load(picture, size):
    image = pygame.image.load(picture)
    final = pygame.transform.scale(image, size)
    final.set_colorkey([255,255,255])
    return final

def distance(position1, position2):
    deltaPosX = abs(position1[0] - position2[0])
    deltaPosY = abs(position1[1] - position2[1])
    distance = math.sqrt(deltaPosX ** 2 + deltaPosY ** 2)
    return distance


class Tank:
    speed = 0
    angle = 0
    angularSpeed = 0
    velocity = [0,0]
    position = [winW/2, winH/2]
    
    def  __init__(self, color):
        self.color = color
    
    def update(self):
        self.imageToBlit = load(self.color+".png", (50, 50))
        self.angle += self.angularSpeed
        self.velocity = (math.sin(math.radians(self.angle))*self.speed, math.cos(math.radians(self.angle))*self.speed)
        self.position = add(self.position, self.velocity)
        blitted = pygame.transform.rotate(self.imageToBlit, self.angle)
        tank_rect = blitted.get_rect(center=self.position)
        surface.blit(blitted, tank_rect)
    def constrain(self):
        if self.position[0] <= 20:
            self.position[0]=20
        if self.position[1] <= 20:
            self.position[1]=20
        if self.position[0] >= winW-20:
            self.position[0]=winW-20
        if self.position[1] >= winH-20:
            self.position[1]=winH-20


class Bullet:
    speed = -8
    velocity = 0
    lifeSpan = 500
    
    def __init__(self, color, angle, position, lifespan):
        self.color = color
        self.angle = angle
        self.position = position
        self.lifespan = lifespan

    def update(self):
        self.imageToBlit = load("bullet.png", (20, 20))
        self.velocity = (math.sin(math.radians(self.angle))*self.speed, math.cos(math.radians(self.angle))*self.speed)
        self.position = add(self.position, self.velocity)
        blitted = pygame.transform.rotate(self.imageToBlit, self.angle)
        bullet_rect = blitted.get_rect(center=self.position)
        surface.blit(blitted, bullet_rect)
    def constrain(self):
        if self.position[0] <= 10:
            self.angle = self.angle*-1
        elif self.position[1] <= 10:
            self.angle = 180 - self.angle
        elif self.position[0] >= winW-10:
            self.angle = self.angle*-1
        elif self.position[1] >= winH-10:
            self.angle = 180 - self.angle
    def hitcheck(self, tank):
        if distance(self.position, tank.position) < 30 and self.lifespan < 470:
            bulletList.remove(self)
            print(str(tank) + "just got hit")
    def decreaseLifespan(self):
        self.lifespan -= 1
        if self.lifespan < 0:
            bulletList.remove(self)



redTank=Tank("red")
blueTank=Tank("blue")

def shoot(tank):
    bulletList.append(Bullet(tank.color, tank.angle, tank.position, 500))

#imageToBlit = load(images[color], (50, 50))
def main():
    global surface, winW, winH
    surface.fill((white))
    while 1:
        events = pygame.event.get
        for event in events():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    redTank.speed = -5
                if event.key == K_DOWN:
                    redTank.speed = 5
                if event.key == K_RIGHT:
                    redTank.angularSpeed = -4
                if event.key == K_LEFT:
                    redTank.angularSpeed = 4
                if event.key == K_w:
                    blueTank.speed = -5
                if event.key == K_s:
                    blueTank.speed = 5
                if event.key == K_d:
                    blueTank.angularSpeed = -4
                if event.key == K_a:
                    blueTank.angularSpeed = 4
                if event.key == K_m:
                    shoot(redTank)
                if event.key == K_q:
                    shoot(blueTank)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == KEYUP:
                if event.key == K_UP:
                    redTank.speed = 0
                if event.key == K_DOWN:
                    redTank.speed = 0
                if event.key == K_RIGHT:
                    redTank.angularSpeed = 0
                if event.key == K_LEFT:
                    redTank.angularSpeed = 0
                if event.key == K_w:
                    blueTank.speed = 0
                if event.key == K_s:
                    blueTank.speed = 0
                if event.key == K_d:
                    blueTank.angularSpeed = 0
                if event.key == K_a:
                    blueTank.angularSpeed = 0
            if event.type == VIDEORESIZE:
                        winH = event.h
                        winW = event.w
                        surface = pygame.display.set_mode((winW, winH), RESIZABLE)
        surface.fill((white))
        redTank.update()
        blueTank.update()
        redTank.constrain()
        blueTank.constrain()
            
        for bullet in bulletList:
            bullet.constrain()
            bullet.update()
            bullet.hitcheck(redTank)
            bullet.hitcheck(blueTank)
            bullet.decreaseLifespan()
        pygame.display.update()
        fpsClock.tick(FPS)
main()
