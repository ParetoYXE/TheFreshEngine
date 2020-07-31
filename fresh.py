import pygame
import random


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

Handgun1Img = pygame.image.load("Handgun1.png")
Handgun2Img = pygame.image.load("Handgun2.png")
Handgun3Img = pygame.image.load("Handgun3.png")
BackGround3 = Background('HandGun3.png',[0,0])
demonImg = pygame.image.load("Demon.png")
demonDeath = pygame.image.load("demonDeath.png")
BackGround = Background('Background.png', [0,0])


pygame.init()
clock = pygame.time.Clock()
FPS = 60  # This variable will define how many frames we update per second.
pygame.font.init() # you have to call this at the start, 
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
gunShot1Effect = pygame.mixer.Sound('gunShot.wav')
gunShot2Effect = pygame.mixer.Sound('gunShot_2.wav')
impactEffect = pygame.mixer.Sound("bulletImpact.wav")
wallsprite = pygame.image.load("WallLeft.png")
wallsprite2 = pygame.image.load("WallRight.png")
cityimg = pygame.image.load("buildings-bg.png")
cityimg2 = pygame.image.load("near-buildings-bg.png")
drawEntitites = []
drawBuildings = []
done = False
renderDis = 4
fireToggle = 0
PlayerOrientation = 2
PlayerPos = 27
levelD = 5
enemyPos = 21
enemyPos2 = 22
enemyPos3 = 23
levelMap = [0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,
			0,0,0,0,0,0,0]

levelMap[PlayerPos] = 1
levelMap[enemyPos] = 2
levelMap[enemyPos2] = 2
levelMap[enemyPos3] = 2


count = 0
for i in levelMap: 
	if(i == 1):
		PlayerPos = count

	count +=1
gunX = 600 
gunY = 500

movementCount = 0


playerScale = 1

def viewRender():
	global demonImg
	global PlayerOrientation
	if(PlayerOrientation == 1): 
		for i in range(1,renderDis):
			if(PlayerPos - i*levelD > 0):
				tile = levelMap[PlayerPos - (i*levelD)]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(width/2 - 50,height/2))
			if(((PlayerPos - i*levelD) - 1) > 0):
				tile = levelMap[PlayerPos - (i*levelD) - 1]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(0,height/2))
			if(((PlayerPos - i*levelD) + 1) > 0):
				tile = levelMap[PlayerPos - (i*levelD) + 1]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(width*0.75,height/2))
	if(PlayerOrientation == 2): 
		for i in range(1,renderDis):
			if(PlayerPos + i > 0):
				tile = levelMap[PlayerPos + i]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(width/2 - 50,height/2))
			if(((PlayerPos + i) - levelD) > 0):
				tile = levelMap[PlayerPos + i - levelD]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(0,height/2))
			if(((PlayerPos + i) + levelD) > 0):
				tile = levelMap[PlayerPos + i + levelD]
				if(tile > 0):
					x = round(300 / i)
					y = round(200 / i)
					demonImg = pygame.transform.scale(demonImg,(x,y))
					screen.blit(demonImg,(width*0.75,height/2))




timer = pygame.time.get_ticks()
while not done:
	clock.tick(FPS)
	screen.fill([255, 255, 255])
	screen.blit(BackGround.image, BackGround.rect)
	movementCount +=1
	#oldPlayerPos = PlayerPos


	if pygame.time.get_ticks()-timer > 1000:
	    timer = pygame.time.get_ticks()
	    #do something every 1.0 seconds
	    levelMap[enemyPos] = 0
	    enemyPos+=levelD
	    levelMap[enemyPos] = 2

	    levelMap[enemyPos2] = 0
	    enemyPos2+=levelD
	    levelMap[enemyPos2] = 2

	    levelMap[enemyPos3] = 0
	    enemyPos3+=levelD
	    levelMap[enemyPos3] = 2
	for event in pygame.event.get():

			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					if(PlayerOrientation == 1):
						PlayerPos -= levelD
						print(PlayerPos)
				if event.key == pygame.K_a:
					PlayerOrientation = 1
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if(pos[0] < gunX):
					gunX -= 10
				elif(pos[1] < gunX):
					gunX += 10
				if(fireToggle == 0):
					fireToggle = 1
					gunShot2Effect.play()
			if event.type == pygame.MOUSEBUTTONUP:
				fireToggle = 0
	

	
	movementCount = 0
	screen.blit(cityimg,(0,200))
	screen.blit(cityimg2,(150,130))
	screen.blit(cityimg,(670,200))
	

	viewRender()

	if(fireToggle == 0):
		screen.blit(Handgun1Img,(gunX,gunY))
	elif(fireToggle == 1):
		screen.blit(Handgun2Img,(gunX,gunY))
		screen.blit(Handgun3Img,(gunX,gunY))



	pygame.display.flip()
