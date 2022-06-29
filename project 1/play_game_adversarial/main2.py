from audioop import minmax
from json.encoder import INFINITY
from msilib.schema import tables
from matplotlib.pyplot import table
from numpy import argmin
import pygame
from sympy import false

pygame.init()

# Tao ban co
def createTable(size):
    # mouse = pygame.mouse.get_pos()

    count = 0

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
    
    # for i in range(n):
    #     x, y = pointList[i]
    #     if x < mouse[0] <= x + 90 and y < mouse[1] <= y + 90:
    #         pygame.draw.rect(screen, (224, 255, 0), [x,y,90,90])

    return pointList

# Danh dau o (di)
def markSquare(row, col, type):
    if type == 'X':
        screen.blit(Ximg, (originalX + row * 90 + 0.5, originalY + col * 90 + 0.95))
    elif type == 'O':
        screen.blit(Oimg, (originalX + row * 90 + 0.5, originalY + col * 90 + 0.95))

# Chuyen tu vi tri cua con tro chuot sang vi tri cua tung o trong ban co
def convertToPos(mouse, pointList):
    i = 0
    for i in range(tableSize * tableSize):
        x, y = pointList[i]
        if x < mouse[0] <= x + 90 and y < mouse[1] <= y + 90:
            break
    return i % tableSize, int(i / tableSize)
    
def minimax(tableMatrix, isMax):
    winning = winCheck()
 
    # If Maximizer has won the game return his/her
    # evaluated score
    if (winning == playerSymbol) :
        return 10
 
    # If Minimizer has won the game return his/her
    # evaluated score
    if (winning == botSymbol) :
        return -10
 
    # If there are no more moves and no winner then
    # it is a tie
    if (isEmptyTable() == False) :
        return 0
 
    # If this maximizer's move
    if (isMax) :    
        best = -1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (tableMatrix[i][j]=='.') :
                 
                    # Make the move
                    tableMatrix[i][j] = botSymbol
 
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimax(tableMatrix, not isMax) )
 
                    # Undo the move
                    tableMatrix[i][j] = '.'
        return best
 
    # If this minimizer's move
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (tableMatrix[i][j] == '.') :
                 
                    # Make the move
                    tableMatrix[i][j] = playerSymbol
 
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(tableMatrix, not isMax))
 
                    # Undo the move
                    tableMatrix[i][j] = '.'
        return best

def isEmptyTable():
    for i in range(tableSize):
        for j in range(tableSize):
            if tableMatrix[i][j] == '.':
                return 1
    return 0

def winCheck():
    # Doi voi ma tran 3x3
    # if tableSize == 3:
        # Kiem tra theo tung dong
    for i in range(3):
        if tableMatrix[i][0] != '.' and tableMatrix[i][0] == tableMatrix[i][1] and tableMatrix[i][1] == tableMatrix[i][2]:
            return tableMatrix[i][0]
    
    # Kiem tra theo tung cot
    for i in range(3):
        if tableMatrix[0][i] != '.' and tableMatrix[0][i] == tableMatrix[1][i] and tableMatrix[1][i] == tableMatrix[2][i]:
            return tableMatrix[0][i]

    # Kiem tra theo 2 duong cheo
    if tableMatrix[1][1] != '.' and ((tableMatrix[0][0] == tableMatrix[1][1] and tableMatrix[1][1] == tableMatrix[2][2]) or (tableMatrix[0][2] == tableMatrix[1][1] and tableMatrix[1][1] == tableMatrix[2][0])):
        return tableMatrix[1][1]
    
    # if tableSize == 5:
    #     # Kiem tra theo tung cot
    #     for i in range(tableSize):
    #         # if tableMatrix[0][i] == tableMatrix[1][i]:
    #         #     return tableMatrix[0][i]
    #         for j in range(tableSize):
    #             if tableMatrix[i][j] != '.':
    #                 if j + 1 < tableSize and j + 2 < tableSize and j + 3 < tableSize and j + 4 < tableSize:
    #                     if tableMatrix[i][j] == tableMatrix[i][j + 1] and tableMatrix[i][j] == tableMatrix[i][j + 2] and tableMatrix[i][j] == tableMatrix[i][j + 3] and tableMatrix[i][j] == tableMatrix[i][j + 4]:
    #                         return tableMatrix[i][j]
                    
        # Kiem tra theo tung cot
        # for i in range(tableSize):
        #     for j in range(tableSize):
        #         if tableMatrix[j][i] != '.':
        #             if j + 1 < tableSize and j + 2 < tableSize and j + 3 < tableSize and j + 4 < tableSize:
        #                 if tableMatrix[j][i] == tableMatrix[j + 1][i] and tableMatrix[j][i] == tableMatrix[j + 2][i] and tableMatrix[j][i] == tableMatrix[j + 3][i] and tableMatrix[j][i] == tableMatrix[j + 4][i]:
        #                     return tableMatrix[j][i]

    return '0'

screenWidth = 1024
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

Ximg = pygame.image.load('X.png')
Ximg = pygame.transform.scale(Ximg, (90, 89.5))

Oimg = pygame.image.load('O.png')
Oimg = pygame.transform.scale(Oimg, (90, 89.5))

run = True
playGame = False

tableSize = 3
tableMatrix = [['.' for i in range(tableSize)] for j in range(tableSize)]
turn = 0
playerSymbol = 'X'
botSymbol = 'O'

while run:
    screen.fill((255,255,255))

    pygame.draw.rect(screen, (0,0,0), [300,690,90,90], 1)
    
    if tableSize == 3:
        originalX = 377
        originalY = 265
    elif tableSize == 5:
        originalX = 287
        originalY = 175
    elif tableSize == 7:
        originalX = 197
        originalY = 85
    
    while playGame:
        screen.fill((255,255,255))
        pointList = createTable(tableSize)
        # Ve nut back
        pygame.draw.rect(screen, (0,0,0), [840,690,90,90], 1)
        
        for i in range(tableSize):
            for j in range(tableSize):
                if tableMatrix[i][j] == 'X':
                    markSquare(i, j, 'X')
                elif tableMatrix[i][j] == 'O':
                    markSquare(i, j, 'O')

        # for i in tableMatrix:
        #     print(i)

        # Truong hop van co chua ket thuc
        # Dieu khien bot bang cach dung minimax
        if turn == 1:
            bestMove = (-1,-1)
            bestValue = -1000

            # for a in range(tableSize):
            #     for b in range(tableSize):
            #         # Vi tri dang trong
            #         if tableMatrix[a][b] == '.' and turn == 1:
            #             tableMatrix[a][b] = botSymbol
                        
            #             move = minimax(tableMatrix, 1)

            #             tableMatrix[a][b] = '.'

            #             if move > bestValue:
            #                 bestMove = (a,b)
            #                 bestValue = move

            # tableMatrix[bestMove[0]][bestMove[1]] = botSymbol
            turn = 0
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                playGame = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 840 < mouse[0] <= 840 + 90 and 690 < mouse[1] <= 690 + 90:
                    playGame = False
                    run = False

                # Den luot nguoi choi di
                if turn == 0:
                    # Nam trong ban co
                    if mouse[0] in range(originalX, originalX + tableSize * 90) and mouse[1] in range(originalY, originalY + tableSize * 90):        
                        x, y = convertToPos(mouse, pointList)
                        pri
                        if tableMatrix[x][y] == '.' and turn == 0:
                            tableMatrix[y][x] = playerSymbol
                            turn = 1
                        print(mouse)

        pygame.display.flip()
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 300 < mouse[0] <= 300 + 90 and 690 < mouse[1] <= 690 + 90:
                playGame = True

    pygame.display.update()


pygame.quit()