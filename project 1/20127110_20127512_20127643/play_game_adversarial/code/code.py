import numpy as np
import pygame as pg
from copy import copy

pg.init()
pg.font.init()

# Font's for text
bigFont = pg.font.Font('freesansbold.ttf', 90)
mediumFont = pg.font.Font('freesansbold.ttf', 50)
smallFont = pg.font.Font('freesansbold.ttf', 40)

# bot and player's symbols
player,bot= 'x', 'o'

# Functions for alpha beta algorithm
# Check if there's still empty spot to make a move
def isEmptyTable(board):
    return '' in board

# calculate and return the value of the current state of the board
def cal_state_value(board) :
    size = len(board)

    # Calculate the state's value when size = 3
    if size == 3:
        # Check every row
        for row in range(size) :    
            if board[row][0] != '':
                if board[row][0] == board[row][1] and board[row][0] == board[row][2]:       
                    if board[row][0] == bot:
                        return 1
                    return -1
    
        # Check every column
        for col in range(size) :
            if board[0][col] != '':
                if board[0][col] == board[1][col] and board[0][col] == board[2][col]:
                    if board[0][col] == bot:
                        return 1
                    return -1
    
        # Check main diagonal
        if board[0][0] != '':
            if board[0][0] == board[1][1] and board[1][1] == board[2][2]:    
                if board[0][0] == bot:
                    return 1
                return -1
        
        # check sub-diagonal
        if board[0][2] != '':
            if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                if board[0][2] == bot:
                    return 1
                return -1
    
    # Calculate the state's value when size = 5
    if size == 5:
        # Check every row
        for row in range(size):
            if board[row][0] != '':
                if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][0] == board[row][3] and board[row][0] == board[row][4]:
                    if board[row][0] == bot:
                        return 1
                    return -1
        
        # check every column
        for col in range(size):
            if board[0][col] != '':
                if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] == board[3][col] and  board[0][col] == board[4][col]:
                    if board[0][col] == bot:
                        return 1
                    return -1
        
        # main diagonal
        if board[0][0] != '':
            if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[3][3] == board[4][4]:
                if board[0][0] == bot:
                    return 1
                return -1

        # sub diagonal
        if board[0][4] != '':
            if board[0][4] == board[1][3] and board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[3][1] == board[4][0]:
                if board[0][4] == bot:
                    return 1
                return -1

    if size == 7:
        # Check every row
        for row in range(size):
            for col in range(3):
                if board[row][col] != '':
                    if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and board[row][col] == board[row][col + 3] and board[row][col] == board[row][col + 4]:
                        if board[row][col] == bot:
                            return 1
                        elif board[row][col] == player:
                            return -1

        # Check every column
        for col in range(size):
            for row in range(3):
                if board[row][col] != '':
                    if board[row][col] == board[row + 1][col] and board[row][col] == board[row + 2][col] and board[row][col] == board[row + 3][col] and board[row][col] == board[row + 4][col]:
                        if board[row][col] == bot:
                            return 1
                        elif board[row][col] == player:
                            return -1

        # Check Main diagonal
        for i in range(3):
            if board[i][i] != '':
                if board[i][i] == board[i + 1][i + 1] and board[i + 2][i + 2] == board[i][i] and board[i][i] == board[i + 3][i + 3] and board[i][i] == board[i + 4][i + 4]:
                    if board[i][i] == bot:
                        return 1
                    elif board[i][i] == player:
                        return -1

        # Check Sub diagonal
        row, col = 0, 6
        for i in range(3):
            if board[row][col] != '':
                if board[row][col] == board[row + 1][col - 1] and board[row][col] == board[row + 2][col - 2] and board[row][col] == board[row + 3][col - 3] and board[row][col] == board[row + 4][col - 4]:
                    if board[row][col] == bot:
                        return 1
                    elif board[row][col] == player:
                        return -1
            row += 1
            col -= 1

        # Check all diagonal lines
        if board[0][4] != '':
            if board[0][4] == board[1][3] and board[0][4] == board[2][2] and board[0][4] == board[3][1] and board[0][4] == board[4][0]:
                if board[0][4] == bot:
                    return 1
                elif board[0][4] == player:
                    return -1
        if board[2][6] != '':
            if board[2][6] == board[3][5] and board[2][6] == board[4][4] and board[2][6] == board[5][3] and board[2][6] == board[6][2]:
                if board[2][6] == bot:
                    return 1
                elif board[2][6] == player:
                    return -1

        if board[0][2] != '':
            if board[0][2] == board[1][3] and board[0][2] == board[2][4] and board[0][2] == board[3][5] and board[0][2] == board[4][6]:
                if board[0][2] == bot:
                    return 1
                elif board[0][2] == player:
                    return -1

        if board[2][0] != '':
            if board[2][0] == board[3][1] and board[2][0] == board[4][2] and board[2][0] == board[5][3] and board[2][0] == board[6][4]:
                if board[2][0] == bot:
                    return 1
                elif board[2][0] == player:
                    return -1
    
        row, col = 0, 1
        for i in range(4):
            if board[row][col] != '':
                if board[row][col] == board[row + 1][col + 1] and board[row][col] == board[row + 2][col + 2] and board[row][col] == board[row + 3][col + 3] and board[row][col] == board[row + 4][col + 4]:
                    if board[row][col] == bot:
                        return 1
                    elif board[row][col] == player:
                        return -1
            row += 1
            col += 1
            if i == 1:
                row, col = 1, 0
        
        row, col = 0, 5
        for i in range(4):
            if board[row][col] != '':
                if board[row][col] == board[row + 1][col - 1] and board[row][col] == board[row + 2][col - 2] and board[row][col] == board[row + 3][col - 3] and board[row][col] == board[row + 4][col - 4]:
                    if board[row][col] == bot:
                        return 1
                    elif board[row][col] == player:
                        return -1
            row += 1
            col -= 1
            if i == 1:
                row, col = 1, 6

    return 0

# find max_value function of alpha beta search algorithm
def max_value(board, depth, alpha, beta):
    # Cal the value of current state
    score = cal_state_value(board)
    if depth == 0:
        return score
    if score == 1:
        return score
    if score == -1:
        return score
    if isEmptyTable(board) == 0:
        return 0
    

    size = len(board)
    best = -1000

    for i in range(size) :        
        for j in range(size) :     
            if (board[i][j]=='') :
                
                board[i][j] = bot

                best = max(best, min_value(board, depth - 1, alpha, beta))

                board[i][j] = ''

                if best >= beta:
                    return best
                alpha = max(alpha, best)
    return best

# find min_value function of alpha beta search algorithm
def min_value(board, depth, alpha, beta):
    # Cal current state's value
    score = cal_state_value(board)
    if depth == 0:
        return score
    if score == 1:
        return score
    if score == -1:
        return score
    if isEmptyTable(board) == 0:
        return 0
    
    best = 1000
    size = len(board)

    for i in range(size):        
        for j in range(size):
            if board[i][j] == '':
                
                board[i][j] = player

                best = min(best, max_value(board, depth - 1, alpha, beta))

                board[i][j] = ''

                if best <= alpha:
                    return best
                beta = min(best, beta)
    return best

# alpha beta search algorithm
def alpha_beta_search(board, depth):
    return min_value(board, depth, -1000, 1000)

# return the best move at the current state of the board for the bot
def best_move(board, count):
    bestValue = -1000
    bestMove = (-1, -1)
    size = len(board)

    # The depth of IDS
    depth = 4
    if size == 7:
        depth = 3
    if size == 3:
        depth = 10
    if count < 1 and size != 3:
        depth = 2

    # For each empty position in board, make a move and fine the best move
    for i in range(size):    
        for j in range(size):
            if board[i][j] == '':
             
                board[i][j] = bot
 
                moveValue = alpha_beta_search(board, depth)

                board[i][j] = ''
 
                if (bestValue < moveValue) :               
                    bestMove = (i, j)
                    bestValue = moveValue
    return bestMove

# Functions for game UI
# initiate the game screen
def init_screen():
    pg.init()

    screenWidth = 1024
    screenHeight = 800

    screen = pg.display.set_mode((screenWidth, screenHeight))

    return screen

# get XO image from the folder
def getSymbolIMG():
    Ximg = pg.image.load('X.png')
    Ximg = pg.transform.scale(Ximg, (90, 89.5))

    Oimg = pg.image.load('O.png')
    Oimg = pg.transform.scale(Oimg, (90, 89.5))

    return Ximg, Oimg

# create board/table based on size, 
def createTable(size, screen, originalX, originalY):
    mouse = pg.mouse.get_pos()

    # Start X and Y for the first square of the matrix
    x, y, n  = originalX, originalY, size * size
    pointList = [(-1,-1) for i in range(n)] # store the x, y position of all the squares
    count = 0
    for i in range(n):
        if count == size:
            y += 90
            x = originalX
            count = 0
        pg.draw.rect(screen, (0,0,0), [x,y,90,90], 1)
        pointList[i] = (x, y)
        
        x += 90
        count += 1
    
    for i in range(n):
        (x, y) = pointList[i]
        if x < mouse[0] <= x + 90 and y < mouse[1] <= y + 90:
            pg.draw.rect(screen, (224, 255, 0), [x,y,90,90])

    return pointList

# return the X-Y position of the board (based on 3x3, 5x5 or 7x7)
def getXY(size):
    if size == 3:
        originalX = 377
        originalY = 265
    elif size == 5:
        originalX = 287
        originalY = 175
    elif size == 7:
        originalX = 197
        originalY = 85
    return originalX, originalY

# return row-col position based on mouse's position
def convertMouseToMatrix(mouse, squarePos, size):
    i = 0
    n = size * size
    for i in range(n):
        x, y = squarePos[i]
        if x < mouse[0] <= x + 90 and y < mouse[1] <= y + 90:
            break
    return int(i / size), i % size

# mark a square at position [row][col] with X-O symbol
def markSquare(screen, row, col, img, originalX, originalY):
    screen.blit(img, (originalX + col * 90 + 0.5, originalY + row * 90 + 0.95))

# Display a text onto screen at (x,y) position with font and color and font chose by the user
def displayText(screen, text, x, y, font, color):
    textRendered = font.render(text, True, color)
    screen.blit(textRendered, (x,y))

def main_game():
    screen = init_screen()
    Ximg, Oimg = getSymbolIMG()

    checkGameStart = 1
    runMainMenu = 1
    gameTableSize = 3

    run = 0
    while runMainMenu:
        count = 0

        # Default choice
        if checkGameStart:
            botTurn = 0
            playerTurn = 1
            checkGameStart = 0

        screen.fill((255,255,255))
        tempMousePos = pg.mouse.get_pos()    

        # Display Title
        pg.draw.rect(screen, (240, 0, 0), [0,0,1080,90])
        displayText(screen, "TIC TAC TOE", 210, 10, bigFont, (0,0,0))


        # Start game  button
        pg.draw.rect(screen, (0, 0, 0), [400,600,223,90], 1)
        if 400 < tempMousePos[0] <= 400 + 223 and 600 < tempMousePos[1] <= 600 + 90:
            pg.draw.rect(screen, (245, 0, 0), [400,600,223,90])
        displayText(screen, "Start Game", 400, 620, smallFont, (0,0,0))

        # Choose table Size option
        pg.draw.rect(screen, (0, 50, 0), [0,100,1080,200], 20)
        pg.draw.rect(screen, (0, 50, 0), [0,100,300,200], 20)

        displayText(screen, "Pick Table Size", 320, 120, mediumFont, (0,0,0))

        pg.draw.rect(screen, (0, 0, 0), [340,180,90,90], 1)
        if 340 < tempMousePos[0] <= 340 + 90 and 180 < tempMousePos[1] <= 180 + 90:
            pg.draw.rect(screen, (245, 0, 0), [340,180,90,90])
        displayText(screen, "3x3", 350, 200, smallFont, (0,0,0))

        pg.draw.rect(screen, (0, 0, 0), [440,180,90,90], 1)
        if 440 < tempMousePos[0] <= 440 + 90 and 180 < tempMousePos[1] <= 180 + 90:
            pg.draw.rect(screen, (245, 0, 0), [440,180,90,90])
        displayText(screen, "5x5", 450, 200, smallFont, (0,0,0))

        pg.draw.rect(screen, (0, 0, 0), [540,180,90,90], 1)
        if 540 < tempMousePos[0] <= 540 + 90 and 180 < tempMousePos[1] <= 180 + 90:
            pg.draw.rect(screen, (245, 0, 0), [540,180,90,90])
        displayText(screen, "7x7", 550, 200, smallFont, (0,0,0))

        displayText(screen, "YOU PICKED", 20, 120, smallFont, (0,0,0))
        tempText = str(gameTableSize) + "x" + str(gameTableSize)
        displayText(screen, tempText, 100, 180, mediumFont, (0,0,255))

        # Choose Player 1-2 option
        displayText(screen, "Choose Player", 320, 340, mediumFont, (0,0,0))
        pg.draw.rect(screen, (0, 0, 200), [0,320,1080,200], 20)
        pg.draw.rect(screen, (0, 0, 200), [0,320,300,200], 20)

        pg.draw.rect(screen, (0, 0, 0), [340,430,200,60],1)
        pg.draw.rect(screen, (0, 0, 0), [560,430,200,60], 1)

        if 340 < tempMousePos[0] <= 340 + 200 and 430 < tempMousePos[1] <= 430 + 60:
            pg.draw.rect(screen, (255, 0, 0), [340,430,200,60])

        if 560 < tempMousePos[0] <= 560 + 200 and 430 < tempMousePos[1] <= 430 + 60:
            pg.draw.rect(screen, (255, 0, 0), [560,430,200,60])
        displayText(screen, "PLAYER 1", 345, 440, smallFont, (0,0,0))
        displayText(screen, "PLAYER 2", 565, 440, smallFont, (0,0,0))

        displayText(screen, "YOU PICKED", 20, 340, smallFont, (0,0,0))

        if botTurn == 0:
            playerTempText = "PLAYER 1"
        else:
            playerTempText = "PLAYER 2"
        displayText(screen, "YOU PICKED", 20, 340, smallFont, (0,0,0))
        displayText(screen, playerTempText, 25, 400, mediumFont, (255,0,0))
        
        # Get pygame event on of the main menu tab
        for menuEvent in pg.event.get():
            if menuEvent.type == pg.QUIT:
                run = 0
                runMainMenu = 0
            
            if menuEvent.type == pg.MOUSEBUTTONDOWN:
                menuMouse = pg.mouse.get_pos()

                # Start game button clicked
                if 400 < tempMousePos[0] <= 400 + 223 and 600 < tempMousePos[1] <= 600 + 90:
                    run = 1
                
                # Choose 3x3
                if 340 < menuMouse[0] <= 340 + 90 and 180 < menuMouse[1] <= 180 + 90:
                    gameTableSize = 3
                # Choose 5x5
                if 440 < menuMouse[0] <= 440 + 90 and 180 < menuMouse[1] <= 180 + 90:
                    gameTableSize = 5
                # Choose 7x7
                if 540 < menuMouse[0] <= 540 + 90 and 180 < menuMouse[1] <= 180 + 90:
                    gameTableSize = 7

                # Choose player (1-2)
                # Choose player 1
                if 340 < tempMousePos[0] <= 340 + 200 and 430 < tempMousePos[1] <= 430 + 60:
                    playerTurn, botTurn = 1, 0
                # Choose player 2
                if 560 < tempMousePos[0] <= 560 + 200 and 430 < tempMousePos[1] <= 430 + 60:
                    playerTurn, botTurn = 0, 1
                
        pg.display.update()
        
        # Init the board and X, Y of the first square before run the game
        if run == 1:
            firstX, firstY = getXY(gameTableSize)
            board = np.chararray((gameTableSize, gameTableSize), unicode=1)

        while run:
            screen.fill((255,255,255))

            # Create board
            squarePos = createTable(gameTableSize, screen, firstX, firstY)

            # Check if the match is over
            wincheck = cal_state_value(board)
            if wincheck == -1:
                displayText(screen, "PLAYER WIN !!!", 175, 10, bigFont, (0,0,0))
                playerTurn = 0
                botTurn = 0
                checkGameStart = 1

                pg.draw.rect(screen, (0, 0, 0), [560,720,315,60], 2)
                displayText(screen, "BACK TO MENU", 560, 735, smallFont, (0,0,0))
            elif wincheck == 1:
                displayText(screen, "BOT WIN !!!", 300, 10, bigFont, (0,0,0))
                playerTurn = 0
                botTurn = 0
                checkGameStart = 1

                pg.draw.rect(screen, (0, 0, 0), [560,720,315,60], 2)
                displayText(screen, "BACK TO MENU", 560, 735, smallFont, (0,0,0))

            elif isEmptyTable(board) == 0:
                displayText(screen, "DRAW !!!", 330, 10, bigFont, (0,0,0))
                playerTurn = 0
                botTurn = 0
                checkGameStart = 1

                pg.draw.rect(screen, (0, 0, 0), [560,720,315,60], 2)
                displayText(screen, "BACK TO MENU", 560, 735, smallFont, (0,0,0))

            # Display the XO symbol to the board
            for i in range(gameTableSize):
                for j in range(gameTableSize):
                    if board[i][j] == '':
                        continue
                    if board[i][j] == 'x':
                        symbolIMG = Ximg
                    elif board[i][j] == 'o':
                        symbolIMG = Oimg
                    markSquare(screen, i, j, symbolIMG, firstX, firstY)
            pg.display.update()

            # Bot's turn
            if botTurn == 1:
                botTurn = 0
                playerTurn = 1

                displayText(screen, "BOT THINKING...", 100, 10, bigFont, (0,0,0))
                pg.display.update()

                # Find the best move
                bestMove = best_move(board, count)
                count += 1
                board[bestMove[0]][bestMove[1]] = bot

            # Get all events of the play game tab
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = 0
                    runMainMenu = 0

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()

                    if playerTurn == 0 and botTurn == 0:
                        if 560 <= mouse[0] <= 560 + 315 and 720 <= mouse[1] <= 720 + 60:
                            run = 0

                    if playerTurn == 1:
                        r, c = convertMouseToMatrix(mouse, squarePos, gameTableSize)
                        
                        if board[r][c] == '':
                            playerTurn = 0
                            botTurn = 1
                            board[r][c] = player

            pg.display.update()

main_game()
