import pygame
pygame.init()

DIMENSIONS = (1100, 1100)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()
TARGET_FPS = 30


pvacant = False

dvacant = False

piece_active = False

legal_move = False
legal_jump = False

pcoord = [0, -1]
dcoord = [0, 0]

is_running = True

start_game = True

boardData = [[0, 1, 0, 1, 0, 1, 0, 1], #0
			 [1, 0, 1, 0, 1, 0, 1, 0], #1
			 [0, 1, 0, 1, 0, 1, 0, 1], #2
			 [0, 0, 0, 0, 0, 0, 0, 0], #3
			 [0, 0, 0, 0, 0, 0, 0, 0], #4
			 [2, 0, 2, 0, 2, 0, 2, 0], #5
			 [0, 2, 0, 2, 0, 2, 0, 2], #6
			 [2, 0, 2, 0, 2, 0, 2, 0]] #7
			 #0  1  2  3  4  5  6  7
pos = (0,0)
piece = {
	"empty":0,
	"white":1,
	"red":2,
	"wking":3,
	"rking":4
}	

def check_square():
	global pvacant
	pvacant = False
	global dvacant
	dvacant = False
	for y in range(0, len(boardData)):
		for x in range(0, len(boardData[y])):
			n=boardData[y][x]

			if piece["empty"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y:
				pvacant = True
			if piece["empty"] == n and dcoord[0] - 1 == x and dcoord[1] - 1 == y:
				dvacant = True

def rules():
	global legal_move
	legal_move = False
	for y in range(0, len(boardData)):
		for x in range(0, len(boardData[y])):
			n=boardData[y][x]

			if piece["white"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 1 or dcoord[0] - pcoord[0] == -1)\
			 and dcoord[1] - pcoord[1] == 1 and dvacant == True:
				legal_move = True
			if piece["white"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 1 or dcoord[0] - pcoord[0] == -1)\
			 and dcoord[1] - pcoord[1] == 1 and dvacant == True and dcoord[1] == 7:
			 	boardData[dcoord[1]-1][dcoord[0]-1] = piece["wking"]

			if piece["red"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 1 or dcoord[0] - pcoord[0] == -1)\
			 and dcoord[1] - pcoord[1] == -1 and dvacant == True:
				legal_move = True
			if piece["red"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 1 or dcoord[0] - pcoord[0] == -1)\
			 and dcoord[1] - pcoord[1] == -1 and dvacant == True and dcoord[1] == 0:
			 	boardData[dcoord[1]-1][dcoord[0]-1] = piece["rking"]

			if (piece["wking"] == n or piece["rking"] == n) and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 1 or dcoord[0] - pcoord[0] == -1)\
			 and (dcoord[1] - pcoord[1] == 1 or dcoord[1] - pcoord[1] == -1) and dvacant == True:
			 	legal_move = True	

def jump():
	global legal_jump
	legal_jump = False
	for y in range(0, len(boardData)):
		for x in range(0, len(boardData[y])):
			n=boardData[y][x]

			if piece["white"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 2 or dcoord[0] - pcoord[0] == -2)\
			 and dcoord[1] - pcoord[1] == 2 and dvacant == True and boardData[((dcoord[1]-1) + (pcoord[1]-1))/2][((dcoord[0]-1) + (pcoord[0]-1))/2] == piece["red"]:
				legal_jump = True 
			if piece["white"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 2 or dcoord[0] - pcoord[0] == -2)\
			 and dcoord[1] - pcoord[1] == 2 and dvacant == True and boardData[((dcoord[1]-1) + (pcoord[1]-1))/2][((dcoord[0]-1) + (pcoord[0]-1))/2] == piece["red"] and dcoord[1] == 7:
				 boardData[dcoord[1]-1][dcoord[0]-1] = piece["wking"]

			if piece["red"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 2 or dcoord[0] - pcoord[0] == -2)\
			 and dcoord[1] - pcoord[1] == -2 and dvacant == True and boardData[((dcoord[1]-1) + (pcoord[1]-1))/2][((dcoord[0]-1) + (pcoord[0]-1))/2] == piece["white"]:
				legal_jump = True
			if piece["red"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and (dcoord[0] - pcoord[0] == 2 or dcoord[0] - pcoord[0] == -2)\
			 and dcoord[1] - pcoord[1] == 2 and dvacant == True and boardData[((dcoord[1]-1) + (pcoord[1]-1))/2][((dcoord[0]-1) + (pcoord[0]-1))/2] == piece["white"] and dcoord[1] == 0:
				 boardData[dcoord[1]-1][dcoord[0]-1] = piece["rking"]


while is_running:
	for event in pygame.event.get():

		if start_game:	
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_ESCAPE:
					is_running = False
		if event.type == pygame.QUIT:
			is_running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if piece_active:
				pos = pygame.mouse.get_pos()
				dcoord[0] = (pos[0]-50)/100
				dcoord[1] = (pos[1]+20)/100
				check_square()
				rules()
				jump()
				if legal_move == True and event.button == 1:												#destination is vacant
					temp = boardData[pcoord[1]-1][pcoord[0]-1]				#value of piece stored
					boardData[pcoord[1]-1][pcoord[0]-1] = piece["empty"]	#old space emptied
					boardData[dcoord[1]-1][dcoord[0]-1] = temp				#new space filled with proper piece
					piece_active = False
					legal_move = False
				if legal_move == False and legal_jump == False and event.button == 1:						#destination is not vacant
					print "Illegal move"
				if legal_jump == True and event.button == 1:
					temp = boardData[pcoord[1]-1][pcoord[0]-1]
					boardData[pcoord[1]-1][pcoord[0]-1] = piece["empty"]
					boardData[dcoord[1]-1][dcoord[0]-1] = temp
					boardData[((dcoord[1]-1) + (pcoord[1]-1))/2][((dcoord[0]-1) + (pcoord[0]-1))/2] = piece["empty"]
					piece_active = False
					legal_jump = False
				if event.button == 3:
					piece_active = False

			else:
				pos = pygame.mouse.get_pos()
				pcoord[0] = (pos[0]-50)/100
				pcoord[1] = (pos[1]+20)/100	
				check_square()
				if pvacant == True and event.button == 1:													#location is vacant
					pass
				if pvacant == False and event.button == 1:													#location is not vacant
					piece_active = True	


	SCREEN.fill ((1, 1, 101))

	xOffset = 150
	yOffset = 80
	black_tile = False
	
	if start_game:
		for y in range(0, len(boardData)):
			for x in range(0, len(boardData[y])):
				n=boardData[y][x]

				if y%2==0:
					if x%2==0:
						pygame.draw.rect(SCREEN, (200, 30, 30), (x*100+xOffset, y*100+yOffset, 100, 100))					#draw red squares, even rows
						black_tile = False
					else:
						pygame.draw.rect(SCREEN, (0, 0, 0), (x*100+xOffset, y*100+yOffset, 100, 100))						#draw black squares, even rows
						black_tile = True

				if y%2==1:
					if x%2==1:
						pygame.draw.rect(SCREEN, (200, 30, 30), (x*100+xOffset, y*100+yOffset, 100, 100))					#draw red squares, odd rows
						black_tile = False
					else:
						pygame.draw.rect(SCREEN, (0, 0, 0), (x*100+xOffset, y*100+yOffset, 100, 100))						#draw black squares, odd rows
						black_tile = True
		
				if piece["white"] == n:
					pygame.draw.circle(SCREEN, (225, 225, 225), (x*100+xOffset+50, y*100+yOffset+50), 45)					#draw white pieces
				if piece["red"] == n:
					pygame.draw.circle(SCREEN, (200, 30, 30), (x*100+xOffset+50, y*100+yOffset+50), 45)						#draw black pieces

				if piece["white"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and piece_active == True:
					pygame.draw.circle(SCREEN, (160, 210, 255), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 50, 5)	#draw white piece outline
				if piece["red"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and piece_active == True:
					pygame.draw.circle(SCREEN, (150, 40, 60), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 50, 5)	#draw red piece outline
				if piece["wking"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and piece_active == True:
					pygame.draw.circle(SCREEN, (160, 210, 255), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 50, 5)
					pygame.draw.circle(SCREEN, (255, 215, 0), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 20, 5)
				if piece["rking"] == n and pcoord[0] - 1 == x and pcoord[1] - 1 == y and piece_active == True:
					pygame.draw.circle(SCREEN, (150, 40, 60), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 50, 5)
					pygame.draw.circle(SCREEN, (255, 215, 0), (pcoord[0]*100+xOffset-50, pcoord[1]*100+yOffset-50), 20, 5)

	pygame.display.update()

	CLOCK.tick(TARGET_FPS)



pygame.quit()