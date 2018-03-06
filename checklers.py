import pygame
pygame.init()

DIMENSIONS = (1100, 1100)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()
TARGET_FPS = 30


is_running = True

start_game = True

boardData = [[0, 1, 0, 1, 0, 1, 0, 1], 
			 [1, 0, 1, 0, 1, 0, 1, 0], 
			 [0, 1, 0, 1, 0, 1, 0, 1], 
			 [0, 0, 0, 0, 0, 0, 0, 0], 
			 [0, 0, 0, 0, 0, 0, 0, 0], 
			 [2, 0, 2, 0, 2, 0, 2, 0], 
			 [0, 2, 0, 2, 0, 2, 0, 2], 
			 [2, 0, 2, 0, 2, 0, 2, 0]]
pos = (0,0)
piece = {
	"empty":0,
	"white":1,
	"black":2
}

while is_running:
	for event in pygame.event.get():

		if start_game:	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					is_running = False
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			coord = ((pos[0]-50)/100, (pos[1]+20)/100)
			print coord				

	SCREEN.fill ((1, 1, 101))

	xOffset = 150
	yOffset = 80
	
	if start_game:
		for y in range(0, len(boardData)):
			for x in range(0, len(boardData[y])):
				n=boardData[y][x]

				if y%2==0:
					if x%2==0:
						pygame.draw.rect(SCREEN, (200, 30, 30), (x*100+xOffset, y*100+yOffset, 100, 100))
					else:
						pygame.draw.rect(SCREEN, (0, 0, 0), (x*100+xOffset, y*100+yOffset, 100, 100))

				if y%2==1:
					if x%2==1:
						pygame.draw.rect(SCREEN, (200, 30, 30), (x*100+xOffset, y*100+yOffset, 100, 100))
					else:
						pygame.draw.rect(SCREEN, (0, 0, 0), (x*100+xOffset, y*100+yOffset, 100, 100))

		for i in range(0, len(boardData)):
			#piece = boardData[i]
			if boardData[i] == 1:
				pygame.draw.circle(SCREEN, (225, 225, 225), (x*100, y*100), 45)

		'''for x in range(xOffset+150, xOffset+950, 200):
			pygame.draw.circle(SCREEN, (225, 225, 225), (x, 130), 45)
			pygame.draw.circle(SCREEN, (50, 50, 50), (x, 730), 45)
			pygame.draw.circle(SCREEN, (225, 225, 225), (x, 330), 45)
		for x in range(xOffset+50, xOffset+850, 200):
			pygame.draw.circle(SCREEN, (225, 225, 225), (x, 230), 45)
			pygame.draw.circle(SCREEN, (50, 50, 50), (x, 630), 45)
			pygame.draw.circle(SCREEN, (50, 50, 50), (x, 830), 45)'''

	pygame.display.update()

	CLOCK.tick(TARGET_FPS)



pygame.quit()