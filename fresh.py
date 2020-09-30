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



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN: 
			done = True


	screen.fill([255,255,255])
	pygame.display.update()
