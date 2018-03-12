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

coord = [0, 0]
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
			coord[0] = (pos[0]-50)/100
			coord[1] = (pos[1]+20)/100
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

		
				if n == 1:
					pygame.draw.circle(SCREEN, (225, 225, 225), (x*100+xOffset+50, y*100+yOffset+50), 45)
				if n == 2:
					pygame.draw.circle(SCREEN, (25, 25, 25), (x*100+xOffset+50, y*100+yOffset+50), 45)

		pygame.draw.circle(SCREEN, (176, 224, 255), (coord[0]*100+xOffset-50, coord[1]*100+yOffset-50),46)

	pygame.display.update()

	CLOCK.tick(TARGET_FPS)



pygame.quit()