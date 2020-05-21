import pygame
import random

Handgun1Img = pygame.image.load("Handgun1.png")
Handgun2Img = pygame.image.load("Handgun2.png")
Handgun3Img = pygame.image.load("Handgun3.png")


demonImg = pygame.image.load("Demon.png")
wallImg = pygame.image.load("stoneWall.png")
scifiWallImg = pygame.image.load("scifiWallSprite.png")

entities = []

fireToggle = 0
gunX = 600 
gunY = 500
playerOrientation = 1
playerPos = 25
#Generic Start Map
length = 10
levelMap = [0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,4,0,4,0,
			0,0,0,0,0,0,4,0,4,0,
			0,0,0,0,0,0,4,0,4,0,
			0,0,0,0,0,0,4,0,4,0,
			4,4,4,4,4,0,4,0,5,0,
			4,0,0,5,5,5,5,0,5,5,
			4,0,0,0,0,0,0,0,5,5,
			4,4,0,5,5,5,5,0,5,5,
			4,0,0,4,0,0,5,0,5,0,
			4,1,0,4,5,5,5,0,5,0,
			4,0,0,4,5,5,0,0,5,5,
			4,0,0,4,5,5,0,0,0,5,
			4,0,0,4,5,0,0,0,0,5,
			4,4,4,4,5,5,5,5,5,5,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0]
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def findPlayerPos(): 
	for i in range(len(levelMap)):
		if(levelMap[i] == 1):
			global playerPos
			playerPos = i
def drawView():
	count = 0
	global entities
	entities = entities[::-1]
	for i in entities:
		if(i["View"]==0):
			if(i["Scale"] == 0):
				i["Img"] = pygame.transform.scale(i["Img"], (400, 600))
				i["Y"] = 0
			elif(i["Scale"] == 1):
				i["Img"] = pygame.transform.scale(i["Img"], (400, 500))
				i["Y"] = 0
			elif(i["Scale"] == 2):
				i["Img"] = pygame.transform.scale(i["Img"], (400, 400))
				i["Y"] = 0
			elif(i["Scale"] == 3):
				i["Img"] = pygame.transform.scale(i["Img"], (400, 300))
				i["Y"] = 0
			elif(i["Scale"] > 3):
				i["Img"] = pygame.transform.scale(i["Img"], (400, 100))
				i["Y"] = 200
			else:
				i["Img"] = pygame.transform.scale(i["Img"], (0,0))
				

		if(i["View"]==1):
			if(i["Scale"] == 0):
				i["Img"] = pygame.transform.scale(i["Img"], (20, 600))
				i["Y"] = 0
			else:
				pos = i["Pos"]
				drawAsWall = False
				for j in range(1,3):
					if(playerOrientation == 1):
						if(levelMap[pos + 1 * j] > 1):
							drawAsWall = True
					if(playerOrientation == 2):
						if(levelMap[pos + length * j] > 1):
							drawAsWall = True
					if(playerOrientation == -2):
						if(levelMap[pos - (length*j)] > 1):
							drawAsWall = True
					if(playerOrientation == -1):
						if(levelMap[pos - (1*j)] > 1):
							drawAsWall = True

				if(drawAsWall):
					if(i["Scale"] == 1):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 500))
						i["Y"] = 0
					elif(i["Scale"] == 2):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 400))
						i["Y"] = 0
					elif(i["Scale"] == 3):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 300))
						i["Y"] = 0
					elif(i["Scale"] > 3):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 100))
						i["Y"] = 200
					else:
						i["Img"] = pygame.transform.scale(i["Img"], (0,0))
				else:
					if(i["Scale"] == 0):
						i["Img"] = pygame.transform.scale(i["Img"], (20, 600))
						i["Y"] = 0
					else:
						i["Img"] = pygame.transform.scale(i["Img"], (0,0))
				
		if(i["View"]==2):
			if(i["Scale"] == 0):
				i["Img"] = pygame.transform.scale(i["Img"], (20, 600))
				i["X"] = 780
				i["Y"] = 0
			else:
				pos = i["Pos"]
				drawAsWall = False
				for j in range(1,3):
					if(playerOrientation == 1):
						if(levelMap[pos - (1*j)] > 1):
							drawAsWall = True
					if(playerOrientation == 2):
						if(levelMap[pos - (length*j)] > 1):
							drawAsWall = True
					if(playerOrientation == -2):
						if(levelMap[pos + length*j] > 1):
							drawAsWall = True
					if(playerOrientation == -1):
						if(levelMap[pos + 1*j] > 1):
							drawAsWall = True

				if(drawAsWall):
					if(i[
						"Scale"] == 1):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 500))
						i["Y"] = 0
					elif(i["Scale"] == 2):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 400))
						i["Y"] = 0
					elif(i["Scale"] == 3):
						i["Img"] = pygame.transform.scale(i["Img"], (200, 300))
						i["Y"] = 0
					elif(i["Scale"] > 3):

						i["Img"] = pygame.transform.scale(i["Img"], (200, 100))
						i["Y"] = 200
					else:
						i["Img"] = pygame.transform.scale(i["Img"], (0,0))
				else:
					if(i["Scale"] == 0):
						i["Img"] = pygame.transform.scale(i["Img"], (20, 600))
						i["Y"] = 0
						i["X"] = 780
					else:
						i["Img"] = pygame.transform.scale(i["Img"], (0,0))

		screen.blit(i["Img"],(i["X"],i["Y"]))

def updateView():
	#Draw entities based on View
	global entities
	entities = []
	for i in range(0,10):
		view = 0
		if(playerOrientation==1):
			view = (playerPos) - (length*i)
		if(playerOrientation == -1):
			view = (playerPos) + (length*i)
		if(playerOrientation == 2):
			view = (playerPos) + (1*i)
		if(playerOrientation == -2):
			view = (playerPos) - (1*i)
		#Use for setting obj into the enviroment. Repeat for more.
		if(view <= len(levelMap) and playerOrientation == 1):
			if levelMap[view] == 3:
				entities.append({"X":200,"Y":200,"Img":demonImg,"Pos": view,"Scale": i,"View":0})
			if levelMap[view-1] == 3:
				entities.append({"X":0,"Y":200,"Img":demonImg,"Pos": view - 1,"Scale": i,"View":1})
			if levelMap[view+1] == 3:
				entities.append({"X":600,"Y":200,"Img":demonImg,"Pos":view + 1,"Scale": i,"View":2})

			if levelMap[view] == 4:
				entities.append({"X":200,"Y":200,"Img":wallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-1] == 4:
				entities.append({"X":0,"Y":200,"Img":wallImg,"Pos":view - 1,"Scale": i,"View":1})
			if levelMap[view+1] == 4:
				entities.append({"X":600,"Y":200,"Img":wallImg,"Pos":view + 1,"Scale": i,"View":2})

			if levelMap[view] == 5:
				entities.append({"X":200,"Y":200,"Img":scifiWallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 5:
				entities.append({"X":0,"Y":200,"Img":scifiWallImg,"Pos":view - length,"Scale": i,"View":1})
			if levelMap[view+length] == 5:
				entities.append({"X":600,"Y":200,"Img":scifiWallImg,"Pos":view + length,"Scale": i,"View":2})
		if(view <= len(levelMap) and playerOrientation == -1):
			if levelMap[view] == 3:
				entities.append({"X":200,"Y":200,"Img":demonImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-1] == 3:
				entities.append({"X":600,"Y":200,"Img":demonImg,"Pos":view - 1,"Scale": i,"View":2})
			if levelMap[view+1] == 3:
				entities.append({"X":0,"Y":200,"Img":demonImg,"Pos":view + 1,"Scale": i,"View":1})

			if levelMap[view] == 4:
				entities.append({"X":200,"Y":200,"Img":wallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-1] == 4:
				entities.append({"X":600,"Y":200,"Img":wallImg,"Pos":view - 1,"Scale": i,"View":2})
			if levelMap[view+1] == 4:
				entities.append({"X":0,"Y":200,"Img":wallImg,"Pos":view + 1,"Scale": i,"View":1})

			if levelMap[view] == 5:
				entities.append({"X":200,"Y":200,"Img":scifiWallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 5:
				entities.append({"X":0,"Y":200,"Img":scifiWallImg,"Pos":view - length,"Scale": i,"View":1})

			print(len(levelMap))
			print(view+length)
			if levelMap[view+length] == 5:
				entities.append({"X":600,"Y":200,"Img":scifiWallImg,"Pos":view + length,"Scale": i,"View":2})
		if(view <= len(levelMap) and playerOrientation == 2):
			if levelMap[view] == 3:
				entities.append({"X":200,"Y":200,"Img":demonImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 3:
				entities.append({"X":0,"Y":200,"Img":demonImg,"Pos":view - length,"Scale": i,"View":1})
			if levelMap[view+length] == 3:
				entities.append({"X":600,"Y":200,"Img":demonImg,"Pos":view + length,"Scale": i,"View":2})

			if levelMap[view] == 4:
				entities.append({"X":200,"Y":200,"Img":wallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 4:
				entities.append({"X":0,"Y":200,"Img":wallImg,"Pos":view - length,"Scale": i,"View":1})
			if levelMap[view+length] == 4:
				entities.append({"X":600,"Y":200,"Img":wallImg,"Pos":view + length,"Scale": i,"View":2})

			if levelMap[view] == 5:
				entities.append({"X":200,"Y":200,"Img":scifiWallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 5:
				entities.append({"X":0,"Y":200,"Img":scifiWallImg,"Pos":view - length,"Scale": i,"View":1})
			if levelMap[view+length] == 5:
				entities.append({"X":600,"Y":200,"Img":scifiWallImg,"Pos":view + length,"Scale": i,"View":2})
		if(view <= len(levelMap) and playerOrientation == -2):
			if levelMap[view] == 3:
				entities.append({"X":200,"Y":200,"Img":demonImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 3:
				entities.append({"X":600,"Y":200,"Img":demonImg,"Pos":view - length,"Scale": i,"View":2})
			if levelMap[view+length] == 3:
				entities.append({"X":0,"Y":200,"Img":demonImg,"Pos":view + length,"Scale": i,"View":1})

			if levelMap[view] == 4:
				entities.append({"X":200,"Y":200,"Img":wallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 4:
				entities.append({"X":600,"Y":200,"Img":wallImg,"Pos":view - length,"Scale": i,"View":2})
			if levelMap[view+length] == 4:
				entities.append({"X":0,"Y":200,"Img":wallImg,"Pos":view + length,"Scale": i,"View":1})

			if levelMap[view] == 5:
				entities.append({"X":200,"Y":200,"Img":scifiWallImg,"Pos":view,"Scale": i,"View":0})
			if levelMap[view-length] == 5:
				entities.append({"X":0,"Y":200,"Img":scifiWallImg,"Pos":view - length,"Scale": i,"View":1})
			if levelMap[view+length] == 5:
				entities.append({"X":600,"Y":200,"Img":scifiWallImg,"Pos":view + length,"Scale": i,"View":2})

pygame.init()
clock = pygame.time.Clock()
FPS = 60  # This variable will define how many frames we update per second.
pygame.font.init() # you have to call this at the start, 
screen = pygame.display.set_mode((800, 600))
BackGround = Background('Background.png', [0,0])
findPlayerPos()


done = False
while not done:
	findPlayerPos()
	clock.tick(FPS)
	screen.fill([255, 255, 255])
	screen.blit(BackGround.image, BackGround.rect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				oldPlayerPos = playerPos
				levelMap[oldPlayerPos] = 0
				if(playerOrientation == 1):
					if(levelMap[playerPos-length] != 4 and levelMap[playerPos-length] != 5):
						playerPos -=length
				elif(playerOrientation == -1):
					if(levelMap[playerPos+length] != 4 and levelMap[playerPos+length] != 5):
						playerPos +=length
				elif(playerOrientation == 2):
					if(levelMap[playerPos+1] != 4  and levelMap[playerPos+1] != 5):
						playerPos +=1
				elif(playerOrientation == -2):
					if(levelMap[playerPos-1] != 4 and levelMap[playerPos-1] != 5 ):
						playerPos -=1
			if event.key == pygame.K_s:
				playerOrientation = playerOrientation * -1
			if event.key == pygame.K_d:
				print(entities)
				if(playerOrientation == 1):
					playerOrientation = 2
				elif(playerOrientation == 2):
					playerOrientation = -1
				elif(playerOrientation == -1):
					playerOrientation = -2
				elif(playerOrientation == -2):
					playerOrientation = 1
			if event.key == pygame.K_a:
				print(entities)
				if(playerOrientation == 1):
					playerOrientation = -2
				elif(playerOrientation == -2):
					playerOrientation = -1
				elif(playerOrientation == -1):
					playerOrientation = 2
				elif(playerOrientation == 2):
					playerOrientation = 1
				print(playerOrientation)

		if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()






				#Should be handled last. Player Hand bob and fire
				if(fireToggle == 0):
					fireToggle = 1
				if(pos[0]-gunX < 0 and abs(pos[0]-gunX) > 20):
					if(gunX >=300):
						gunX -=20
				if(pos[0]-gunX > 0 and abs(pos[0]-gunX) > 20):
					if(gunX<=600):
						gunX+=20

		if event.type == pygame.MOUSEBUTTONUP:
				fireToggle = 0

	
	updateView()
	drawView()
	print("playerOrientation:" + str(playerOrientation))
	print("Player Position: " + str(playerPos))
	print("Entities:")
	for i in entities:
		print(i)
	#This should always occur last
	if(fireToggle == 0):
		screen.blit(Handgun1Img,(gunX,gunY))
	elif(fireToggle == 1):
		screen.blit(Handgun2Img,(gunX,gunY))
		screen.blit(Handgun3Img,(gunX,gunY))
	pygame.display.flip()
