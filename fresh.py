#DESIGN#

#MAIN LOGIC LOOP#
	#UPDATE PLAYER POS & STATE
	#UPDATE NPC POS & STATE
	#RENDER WALLS
		#DETERMINE ORIENTATION
		#DETERMINE VIEWMATRIX
		#CHECK VALUES
		#SCALE IMAGES
		#DRAW IMAGES
	#WAIT FOR INPUT





import pygame
import random

pygame.init()
pygame.font.init() # you have to call this at the start, 
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

done = False

demonImg = pygame.image.load("demon.png")
w, h = pygame.display.get_surface().get_size()

demonX = round(w / 5)
demonY = round(h / 5)
demonXScale = 100
demonYScale = 100



def renderEntity():
	global demonImg
	demonImgNew = pygame.transform.scale(demonImg,(demonXScale,demonYScale))
	screen.blit(demonImgNew,(demonX,demonY))

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_w:
				demonXScale +=10
				demonYScale +=10
			elif event.key == pygame.K_d:
				demonX +=10
			elif event.key == pygame.K_a:
				demonX -=10
			elif event.key == pygame.K_ESCAPE:
				done = True



	screen.fill([255,255,255])
	renderEntity()
	pygame.display.update()
