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
Shotgun1Img = pygame.image.load("shotgun1.png")
Shotgun2Img = pygame.image.load("shotgun2.png")
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
gunShotShotgunEffect = pygame.mixer.Sound('shotgun.wav')
impactEffect = pygame.mixer.Sound("bulletImpact.wav")
wallsprite = pygame.image.load("WallLeft.png")
wallsprite2 = pygame.image.load("stoneWall.png")
wallsprite3 = pygame.image.load('WallRight.png')
cityimg = pygame.image.load("buildings-bg.png")
cityimg2 = pygame.image.load("near-buildings-bg.png")
tableimg = pygame.image.load("table.png")
drawEntitites = []
drawBuildings = []
done = False
renderDis = 4
fireToggle = 0
PlayerOrientation = 1
PlayerPos = 28
levelD = 14
enemyPos = 27
enemyPos2 = 21
enemyPos3 = 29
enemyPos4 = 0
levelMap = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,
			4,5,5,5,5,5,0,0,0,0,0,0,0,4,
			4,5,0,7,0,5,0,0,0,0,0,0,0,4,
			4,6,0,0,0,5,0,0,0,0,0,0,0,4,
			4,6,6,6,0,6,0,0,0,0,0,0,0,4,
			4,6,6,6,0,6,0,0,0,0,0,0,0,4,
			4,0,0,6,0,6,6,0,0,0,0,0,0,4,
			4,0,0,6,0,0,6,0,0,0,3,0,3,4,
			4,0,0,6,3,7,5,5,0,0,3,0,3,4,
			4,0,0,0,3,1,0,3,5,5,5,0,3,4,
			4,0,0,0,5,0,0,0,0,0,0,0,3,4,
			4,0,0,0,5,5,3,3,0,0,0,0,3,4,
			4,0,0,0,0,0,0,3,3,3,3,3,3,4,
			4,4,4,4,4,4,4,4,4,4,4,4,4,4,]
found = 0

weaponToggle = True
for i in range(len(levelMap)):
	if levelMap[i] == 1:
		PlayerPos = i
	elif(levelMap[i] == 2):
		if(found == 0):
			enemyPos = i
		elif(found == 1):
			enemyPos2 = i
		elif(found == 2):
			enemyPos3 = i
		elif(found == 3):
			enemyPos4 = i
		found+=1


count = 0
for i in levelMap: 
	if(i == 1):
		PlayerPos = count

	count +=1
gunX = 600 
gunY = 500

movementCount = 0


playerScale = 1

def collisionDetection(pos,movement):
	global PlayerPos
	if(levelMap[pos] == 4):
		PlayerPos += movement
		print("Collision")
	elif(levelMap[pos] == 3):
		PlayerPos += movement
		print("Collision")
	elif(levelMap[pos] == 6):
		PlayerPos += movement
		print("Collision")
	elif(levelMap[pos] == 5):
		PlayerPos += movement
		print("Collision")



def envRender():
	global wallsprite, wallsprite2
	renderStack = []
	count = 0
	if(PlayerOrientation == 1):
		for i in range(1,renderDis):
			pos = [0,1,-1]
			for j in pos:
				index = (PlayerPos - (i*levelD)) + j
				if(index < len(levelMap)):
					if(index > 0):
						tile = levelMap[index]
						if(tile == 3 or tile == 5):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							if(tile == 3):
								sprite = pygame.transform.scale(wallsprite,(x,y))
							elif(tile == 5):
								sprite = pygame.transform.scale(wallsprite3,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 6):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							sprite = pygame.transform.scale(wallsprite2,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 7):
							x = 300
							y = round((300/i)+50*i)
							sprite = pygame.transform.scale(tableimg,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":200})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":200})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":0,"y":200})
			if(count == 1):
				k = len(renderStack)
				print(renderStack[k-1]["sprite"])
				if(renderStack[k-1]["x"] == width /3):
					print("center no change")
				elif(renderStack[k-1]["x"] == 2*(width/3)):
					renderStack[k-1]["x"] = width - 10
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
				elif(renderStack[k-1]["x"]==0):
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
			print("Count: " + str(count))
			count = 0

	if(PlayerOrientation == 2):
		for i in range(1,renderDis):
			pos = [0,levelD,-levelD]
			for j in pos:
				index = (PlayerPos + 1 * i) + j
				if(index < len(levelMap)):
					if(index > 0):
						tile = levelMap[index]
						if(tile == 3 or tile == 5):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							if(tile == 3):
								sprite = pygame.transform.scale(wallsprite,(x,y))
							elif(tile == 5):
								sprite = pygame.transform.scale(wallsprite3,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 6):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							sprite = pygame.transform.scale(wallsprite2,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 7):
							x = 300
							y = round((300/i)+50*i)
							sprite = pygame.transform.scale(tableimg,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":200})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":200})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":200})
			if(count == 1):
				k = len(renderStack)
				print(renderStack[k-1]["sprite"])
				if(renderStack[k-1]["x"] == width /3):
					print("center no change")
				elif(renderStack[k-1]["x"] == 2*(width/3)):
					renderStack[k-1]["x"] = width - 10
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
				elif(renderStack[k-1]["x"]==0):
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
			print("Count: " + str(count))
			count = 0
	if(PlayerOrientation == 3):
		for i in range(1,renderDis):
			pos = [0,1,-1]
			for j in pos:
				index = (PlayerPos + (i*levelD)) + j
				if(index < len(levelMap)):
					if(index > 0):
						tile = levelMap[index]
						if(tile == 3 or tile == 5):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							if(tile == 3):
								sprite = pygame.transform.scale(wallsprite,(x,y))
							elif(tile == 5):
								sprite = pygame.transform.scale(wallsprite3,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 6):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							sprite = pygame.transform.scale(wallsprite2,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 7):
							x = 300
							y = round((300/i)+50*i)
							sprite = pygame.transform.scale(tableimg,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":200})
							elif(j == -1):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":200})
							elif(j == 1):
								renderStack.append({"sprite":sprite,"x":0,"y":200})
			if(count == 1):
				k = len(renderStack)
				print(renderStack[k-1]["sprite"])
				if(renderStack[k-1]["x"] == width /3):
					print("center no change")
				elif(renderStack[k-1]["x"] == 2*(width/3)):
					renderStack[k-1]["x"] = width - 10
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
				elif(renderStack[k-1]["x"]==0):
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
			print("Count: " + str(count))
			count = 0
	if(PlayerOrientation == 4):
		for i in range(1,renderDis):
			pos = [0,levelD,-levelD]
			for j in pos:
				index = (PlayerPos - 1 * i) + j
				if(index < len(levelMap)):
					if(index > 0):
						tile = levelMap[index]
						if(tile == 3 or tile == 5):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							if(tile == 3):
								sprite = pygame.transform.scale(wallsprite,(x,y))
							elif(tile == 5):
								sprite = pygame.transform.scale(wallsprite3,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 6):
							count +=1
							x = 300
							y = round((500/i)+50*i)
							sprite = pygame.transform.scale(wallsprite2,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":0+i*25})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":0+i*25})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":0+i*25})
						elif(tile == 7):
							x = 300
							y = round((300/i)+50*i)
							sprite = pygame.transform.scale(tableimg,(x,y))
							if(j == 0):
								renderStack.append({"sprite":sprite,"x":width/3,"y":200})
							elif(j == -levelD):
								renderStack.append({"sprite":sprite,"x":2*(width/3),"y":200})
							elif(j == levelD):
								renderStack.append({"sprite":sprite,"x":0,"y":200})
			if(count == 1):
				k = len(renderStack)
				print(renderStack[k-1]["sprite"])
				if(renderStack[k-1]["x"] == width /3):
					print("center no change")
				elif(renderStack[k-1]["x"] == 2*(width/3)):
					renderStack[k-1]["x"] = width - 10
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
				elif(renderStack[k-1]["x"]==0):
					renderStack[k-1]["sprite"] =  pygame.transform.scale(sprite,(10,y))
			print("Count: " + str(count))
			count = 0
	renderStack = renderStack[::-1]
	for i in renderStack:
		screen.blit(i["sprite"],(i["x"],i["y"]))
						


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
	    #levelMap[enemyPos] = 0
	    #enemyPos+=levelD
	    #levelMap[enemyPos] = 2

	    #levelMap[enemyPos2] = 0
	    #enemyPos2+=levelD
	    #levelMap[enemyPos2] = 2

	    #levelMap[enemyPos3] = 0
	    #enemyPos3+=levelD
	    #levelMap[enemyPos3] = 2
	for event in pygame.event.get():

			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					if(PlayerOrientation == 1):
						PlayerPos -= levelD
						collisionDetection(PlayerPos,levelD)
					elif(PlayerOrientation == 2):
						PlayerPos +=1
						collisionDetection(PlayerPos,-1)
					elif(PlayerOrientation == 3):
						PlayerPos += levelD
						collisionDetection(PlayerPos,-levelD)
					elif(PlayerOrientation == 4):
						PlayerPos -= 1
						collisionDetection(PlayerPos,1)

					print("PlayerPos: " + str(PlayerPos))
				if event.key == pygame.K_a:
					if(PlayerOrientation == 1):
						PlayerOrientation = 4
					elif(PlayerOrientation == 4):
						PlayerOrientation = 3
					elif(PlayerOrientation == 3):
						PlayerOrientation = 2
					elif(PlayerOrientation == 2):
						PlayerOrientation = 1
				if event.key == pygame.K_d:
					if(PlayerOrientation == 1):
						PlayerOrientation = 2
					elif(PlayerOrientation == 2):
						PlayerOrientation = 3
					elif(PlayerOrientation == 3):
						PlayerOrientation = 4
					elif(PlayerOrientation == 4):
						PlayerOrientation = 1
				if event.key == pygame.K_TAB:
					weaponToggle = not weaponToggle
				print(PlayerOrientation)
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if(pos[0] < gunX):
					gunX -= 10
				elif(pos[1] < gunX):
					gunX += 10
				if(fireToggle == 0):
					fireToggle = 1
					if(weaponToggle):
						gunShotShotgunEffect.play()
					else:
						gunShot2Effect.play()

			if event.type == pygame.MOUSEBUTTONUP:
				fireToggle = 0
	

	
	movementCount = 0
	screen.blit(cityimg,(0,200))
	screen.blit(cityimg2,(150,130))
	screen.blit(cityimg,(670,200))
	

		
	envRender()

	if(fireToggle == 0):
		if(weaponToggle):
			screen.blit(Shotgun1Img,(gunX,gunY))
		else:
			screen.blit(Handgun1Img,(gunX,gunY))
	elif(fireToggle == 1):
		if(weaponToggle):
			screen.blit(Shotgun2Img,(gunX,gunY))
		else:
			screen.blit(Handgun2Img,(gunX,gunY))
			screen.blit(Handgun3Img,(gunX,gunY))



	pygame.display.flip()
