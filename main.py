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
bulletpic = "bullet.png"
images = ["red.png", "blue.png", "green.png"]
def add(a, b):
	return (a[0] + b[0], a[1] + b[1])

def load(picture, size):
	image = pygame.image.load(picture)
	final = pygame.transform.scale(image, size)
	final.set_colorkey([255,255,255])
	return final
	
#tank = [speed, angle, angular speed, velocity, position, image to blit]
tanklist = []

def newtank():
	tanklist.append([0, 0, 0, [0, 0], [winW/2, winH/2], load(images[len(tanklist)], (50, 50))])

def update(tank):
	tank[1] += tank[2]
	tank[3] = (math.sin(math.radians(tank[1]))*tank[0], math.cos(math.radians(tank[1]))*tank[0])
	tank[4][0] += tank[3][0]
	tank[4][1] += tank[3][1]
	

def draw(tank):
	blitted = pygame.transform.rotate(tank[5], tank[1])
	tank_rect = blitted.get_rect(center=tank[4])
	surface.blit(blitted, tank_rect)


newtank()
newtank()

#bullet = [speed, angle, velocity, position, image to blit, lifespan, owner]
bulletlist = []

def updatebullet(bullet):
	bullet[2] = (math.sin(math.radians(bullet[1]))*bullet[0], math.cos(math.radians(bullet[1]))*bullet[0])
	bullet[3] = add(bullet[3], bullet[2])

def drawbullet(bullet):
	blitted = pygame.transform.rotate(bullet[4], bullet[1])
	bullet_rect = blitted.get_rect(center=bullet[3])
	surface.blit(blitted, bullet_rect)

def shoot(tank):
	bulletlist.append([-8, tank[1], 0, tank[4], load(bulletpic, (20, 20)), 0])

def constrain(bullet):
	if bullet[3][0] <= 10:
		bullet[1] = bullet[1]*-1
	elif bullet[3][1] <= 10:
		bullet[1] = 180 - bullet[1]
	elif bullet[3][0] >= winW-10:
		bullet[1] = bullet[1]*-1
	elif bullet[3][1] >= winH-10:
		bullet[1] = 180 - bullet[1]


def constrainTank(tank):
	if tank[4][0] <= 20:
		tank[4][0]=20
	if tank[4][1] <= 20:
		tank[4][1]=20
	if tank[4][0] >= winW-20:
		tank[4][0]=winW-20
	if tank[4][1] >= winH-20:
		tank[4][1]=winH-20
	

	
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
					tanklist[0][0] = -5
				if event.key == K_DOWN:
					tanklist[0][0] = 5
				if event.key == K_RIGHT:
					tanklist[0][2] = -4
				if event.key == K_LEFT:
					tanklist[0][2] = 4
				if event.key == K_m:
					shoot(tanklist[0])
				if event.key == K_w:
					tanklist[1][0] = -5
				if event.key == K_s:
					tanklist[1][0] = 5
				if event.key == K_d:
					tanklist[1][2] = -4
				if event.key == K_a:
					tanklist[1][2] = 4
				if event.key == K_m:
					shoot(tanklist[0])
				if event.key == K_q:
					shoot(tanklist[1])
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

			if event.type == KEYUP:
				if event.key == K_UP:
					tanklist[0][0] = 0
				if event.key == K_DOWN:
					tanklist[0][0] = 0
				if event.key == K_RIGHT:
					tanklist[0][2] = 0
				if event.key == K_LEFT:
					tanklist[0][2] = 0
				if event.key == K_w:
					tanklist[1][0] = 0
				if event.key == K_s:
					tanklist[1][0] = 0
				if event.key == K_d:
					tanklist[1][2] = 0
				if event.key == K_a:
					tanklist[1][2] = 0
			if event.type == VIDEORESIZE:
						winH = event.h
						winW = event.w
						surface = pygame.display.set_mode((winW, winH), RESIZABLE)
		surface.fill((white))
		for tank in tanklist:
			constrainTank(tank)
			update(tank)
			draw(tank)
			
		for bullet in bulletlist:
			constrain(bullet)
			updatebullet(bullet)
			bullet[5] += 1
			drawbullet(bullet)
			if bullet[5] > 500:
				bulletlist.remove(bullet)
		pygame.display.update()
		fpsClock.tick(FPS)
main()
