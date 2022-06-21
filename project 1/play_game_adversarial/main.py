import pygame
from sympy import false

pygame.init()

def createTable(size):
    mouse = pygame.mouse.get_pos()

    count = 0
    # (height - tableSize * rectSize) / 2
    if size == 3:
        originalX = 377
        originalY = 265
    elif size == 5:
        originalX = 287
        originalY = 175
    elif size == 7:
        originalX = 197
        originalY = 85

    x, y, n  = originalX, originalY, size * size
    pointList = [[0 for i in range(2)] for j in range(size * size)]
    for i in range(n):
        if count == size:
            y += 90
            x = originalX
            count = 0
        pygame.draw.rect(screen, (0,0,0), [x,y,90,90], 1)
        pointList[i] = x, y
        
        x += 90
        count += 1

    count = 0
    for i in range(n):
        x, y = pointList[i]
        if x < mouse[0] <= x + 90 and y < mouse[1] <= y + 90:
            pygame.draw.rect(screen, (224, 255, 0), [x,y,90,90])

screenWidth = 1024
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

run = True
runGame = True

while run:
    screen.fill((255,255,255))

    while runGame:
        screen.fill((255,255,255))
        createTable(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                runGame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
        pygame.display.update()
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false

    pygame.display.update()


pygame.quit()