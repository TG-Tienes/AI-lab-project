from re import T
from tabnanny import check
from tracemalloc import start
import turtle

from queue import PriorityQueue
from collections import deque
import numpy as np
import time

def readInputFile(fname):
    with open(fname) as f:
        lines = f.readline()
        pixel = list(map(int, lines.split()))
    
        lines = f.readline()
        lines = lines.split()
        startGoal = [int(i) for i in lines]

        lines = f.readline()
        numOfPoly = int(lines)

        polyList = [[0]] * numOfPoly
        for i in range(0, numOfPoly):
            lines = f.readline()
            lines = lines.split()

            polyList[i] = [int(j) for j in lines]

        # turn 2D array to 3D array
        polyList = np.array(polyList, dtype="object")
        for i in range(numOfPoly):
            polyList[i] = np.array(polyList[i]).reshape(int(len(polyList[i])/2), 2)

    return pixel, startGoal, numOfPoly, polyList

# draw grid based on width, height
def drawGrid(height, width, startGoal):
    tur = turtle.Turtle()
    tur.fillcolor('cyan')

    height += 1
    width += 1
    initX = -400
    initY = -400

    turtle.tracer(0)
    # tur.penup()
    tur.speed(6)
    tur.left(90) 

    tur.up()
    tur.setpos(initX, initY)
    tur.down()
    
    tur.fillcolor("grey")
    tur.begin_fill()
    tur.forward(height * 35)
    tur.right(90)
    tur.forward(width * 35)
    tur.right(90)
    tur.forward(height * 35)
    tur.right(90)
    tur.forward(width * 35)
    tur.right(90)
    tur.end_fill()

    tur.up()
    tur.setpos(initX + 35, initY + 35)
    tur.down()
    tur.fillcolor("white")
    tur.begin_fill()
    tur.forward(height * 35 - 70)
    tur.right(90)
    tur.forward(width * 35 - 70)
    tur.right(90)
    tur.forward(height * 35 - 70)
    tur.right(90)
    tur.forward(width * 35 - 70)
    tur.right(90)
    tur.end_fill()

    x = initX
    for i in range(width):
        tur.up()
        tur.setpos(x, initY)
        tur.down()
        tur.forward(height * 35) 
        x += 35

    tur.right(90)
    y = initY
    for i in range(height):
        tur.up()
        tur.setpos(initX, y)
        tur.down()

        tur.forward(width * 35)
        y += 35
    

    y = initY + 10
    for i in range(height):
        tur.up()
        tur.setpos(initX - 10, y)
        
        tur.write(i, align="center",font=('Arial', 10, 'bold'))
        tur.down()

        y += 35

    x = initX + 10
    for i in range(width):
        tur.up()
        tur.setpos(x + 10, initY - 20)
        
        tur.write(i, align="center",font=('Arial', 10, 'bold'))
        tur.down()

        x += 35

    fillPixel(startGoal[0], startGoal[1], "yellow")
    tur.up()
    tur.setpos(initX + startGoal[0] * 35 + 18, initY + startGoal[1] * 35 + 5)
    tur.write('S', align="center",font=('Arial', 18, 'bold'))
    tur.down()

    fillPixel(startGoal[2], startGoal[3], "yellow")
    tur.up()
    tur.setpos(initX + startGoal[2] * 35 + 18, initY + startGoal[3] * 35 + 5)
    tur.write('G', align="center",font=('Arial', 18, 'bold'))
    tur.down()

    turtle.tracer(1)
    tur.hideturtle()

def fillPixel(x, y, color):
    tur = turtle.Turtle()
    turtle.tracer(0)
    tur.hideturtle()

    tur.fillcolor("cyan")

    tur.up()
    tur.setpos(-400 + x * 35, -400 + y * 35)
    tur.down()

    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(4):
        tur.forward(35)
        tur.left(90)
    tur.end_fill()

    turtle.tracer(1);
def drawPolygon(polygonList, height, width):    
    turtle.tracer(0)
    # turtle.speed(0)
    blockedList = [ [ '.' for i in range(width) ] for j in range(height) ]

    for i in range(0, len(polygonList), 1):
        print("----")
        for j in range(0, len(polygonList[i]), 1):
            x = polygonList[i][j][0]
            y = polygonList[i][j][1]

            # kiem tra den diem n - 1
            if j + 1 == len(polygonList[i]):
                nextX = polygonList[i][0][0]
                nextY = polygonList[i][0][1]
            else:
                nextX = polygonList[i][j + 1][0]
                nextY =  polygonList[i][j + 1][1]

            print(x, y, nextX, nextY)
            xList = []
            yList = []

            check = 0
            if x > nextX:
                x, nextX = nextX, x
                check = 1
            if x != nextX:
                r = x + 1
                while True:
                    if r > nextX:
                        break
                    xList.append(r)
                    r += 1
                if len(xList) == 0:
                    xList.append(r)
            else:
                xList.append(x)

            if check == 1:
                xList.reverse()
                check = 0

            if y > nextY:
                y, nextY = nextY, y
                check = 1
            if y != nextY:
                s = y 
                while True:
                    if s > nextY:
                        break
                    yList.append(s)
                    s += 1
                if len(yList) == 0:
                    yList.append(y)
            else:
                yList.append(y)

            if check == 1:
                yList.reverse()

            print(xList, yList)
            if len(xList) != 1 and len(yList) != 1:
                rangeVal = max(len(xList), len(yList))
                for q in range(0, rangeVal, 1):
                    if len(xList) > len(yList):
                        if(q >= len(yList)):
                            fillPixel(xList[q], yList[len(yList) - 1], "green")
                            blockedList[yList[len(yList) - 1]][xList[q]] = '%'
                        else:
                            fillPixel(xList[q], yList[q], "green")
                            blockedList[yList[q]][xList[q]] = '%'
                    elif len(xList) < len(yList):
                        if(q >= len(xList)):
                            fillPixel(xList[len(xList) - 1], yList[q], "green")
                            blockedList[yList[q]][xList[len(xList) - 1]] = '%'
                        else:
                            fillPixel(xList[q], yList[q], "green")   
                            blockedList[yList[q]][xList[q]] = '%'
                    else:
                        fillPixel(xList[q], yList[q], "green")      
                        blockedList[yList[q]][xList[q]] = '%'
            else:
                for q in range(0, len(xList), 1):
                    for t in range(0, len(yList), 1):
                        fillPixel(xList[q], yList[t], "green")
                        blockedList[yList[t]][xList[q]] = '%'

            # xList.clear()
            # yList.clear()

    for i in range(len(polygonList)):
        for j in range(len(polygonList[i])):
            fillPixel(polygonList[i][j][0], polygonList[i][j][1], "black") 
            blockedList[polygonList[i][j][1]][polygonList[i][j][0]] = '%'

    turtle.tracer(1)
    return blockedList

# calc g for each from start
def calcCost(blockedList,matrixHeight,matrixWidth,startGoal):
    for i in range (matrixHeight):
        for j in range (matrixWidth):
            if (blockedList[i][j]!='%'):
                blockedList[i][j]=(abs(i-startGoal[1])+abs(j-startGoal[0]))
            else:
                blockedList[i][j]='.'
    return blockedList

# check point x,y are valid or not 
def checkRule(matrixHeight,matrixWidth,pointX,pointY):
    return 0<pointY<matrixHeight-1 and 0<pointX<matrixWidth-1 

# def UCSs(arrayCost,matrixHeight,matrixWidth,startGoal):
#     queue= PriorityQueue()
#     queue.put((arrayCost[startGoal[1]][startGoal[0]],(startGoal[1],startGoal[0],"Start")))
#     visited=np.full((matrixHeight, matrixWidth), True, dtype=bool)
#     # visited[startGoal[1]][startGoal[0]]=True
#     path=[]
#     i=0
#     while True:
#         # time.sleep(0.5)
#         i=i+1
#         if not queue:
#             break
#         agentCost,agentPos=queue.get()
#         print("=====")
#         print("Loop: ",i)
#         print("Move: ",agentPos[2])
#         # print(agentCost)
#         # print(agentPos[0])
#         # print(agentPos[1])
#         # print(path)
#         fillPixel(agentPos[1],agentPos[0],"BLUE")
        
#         # if not visited[agentPos[1]][agentPos[0]]:
#         #     fillPixel(agentPos[1],agentPos[0],"RED")
#         if(agentPos[0]==startGoal[2]and agentPos[1]==startGoal[3]):
#             print("done")
#             break
#         x,y,w1=moveUp(agentPos[1],agentPos[0])
#         z,p,w2=moveDown(agentPos[1],agentPos[0])
#         a,b,w3=moveLeft(agentPos[1],agentPos[0])
#         c,d,w4=moveRight(agentPos[1],agentPos[0])
#         if checkRule(matrixHeight,matrixWidth,x,y) and arrayCost[x][y]!='.':
#             if visited[x][y]:
#                 queue.put((arrayCost[y][x],(x,y,w1)))
#                 visited[x][y]=False
#         if checkRule(matrixHeight,matrixWidth,z,p) and arrayCost[z][p]!='.':
#             if visited[z][p]:
#                 queue.put((arrayCost[p][z],(z,p,w2)))
#                 visited[z][p]=False
#         if checkRule(matrixHeight,matrixWidth,a,b)and arrayCost[a][b]!='.':
#             if visited[a][b]:
#                 queue.put((arrayCost[b][a],(a,b,w3)))
#                 visited[a][b]=False
#         if checkRule(matrixHeight,matrixWidth,c,d)and arrayCost[c][d]!='.':
#             if visited[c][d]:
#                 queue.put((arrayCost[d][c],(c,d,w4)))
#                 visited[c][d]=False
#         print(queue.queue)
#         # time.sleep(1)
#     return path
   

def UCS(arrayCost,x,y,matrixHeight,matrixWidth):
    dict={}
    frontier=PriorityQueue()
    frontier.put((arrayCost[x][y],(x,y)))
    visited=set()
    
    dict[x,y]=x,y
    i=0
    j=0
    while frontier:
        i=i+1
       
        print("===")
        print("Loop: ",i)
        cost,pos=frontier.get()
        fillPixel(x,y,"RED")
        y, x = pos 
        
        print("X: ",x)
        print("Y: ",y)
        print("Cost:",cost)
        print("J: ",j)
        # print(dict)
        # time.sleep(2)
        if (x,y) not in visited:
            fillPixel(x,y,"BLUE")
            j=j+1
        if arrayCost[x][y]=="@@":
            return True
        if checkRule(matrixHeight,matrixWidth,x+1,y) and (x+1,y) not in visited and arrayCost[x+1][y]!="." : # check move Up
            dict[x+1,y]=x,y
            frontier.put((arrayCost[x+1][y],(x+1,y)))
            visited.add((x+1,y))
        if checkRule(matrixHeight,matrixWidth,x-1,y) and (x-1,y) not in visited and arrayCost[x-1][y]!="." : # check move Down
            dict[x-1,y]=x,y
            frontier.put((arrayCost[x-1][y],(x-1,y)))
            visited.add((x-1,y))
        if checkRule(matrixHeight,matrixWidth,x,y-1) and (x,y-1) not in visited and arrayCost[x][y-1]!="." : # check move Left
            dict[x,y-1]=x,y
            frontier.put((arrayCost[x][y-1],(x,y-1)))
            visited.add((x,y-1))
        if checkRule(matrixHeight,matrixWidth,x,y+1) and (x,y+1) not in visited and arrayCost[x][y+1]!="." : # check move Right
            dict[x,y+1]=x,y
            frontier.put((arrayCost[x][y+1],(x,y+1)))
            visited.add((x,y+1))
    
    return True

   
def main():
    pixel, startGoal, numOfPoly, polyList = readInputFile(fname="input.txt")
    screenHeight = 1000
    screenWidth = 1680

    matrixHeight = pixel[1]
    matrixWidth = pixel[0]
    # init screen
    screen = turtle.Screen()
    screen.setup(screenWidth, screenHeight)

    drawGrid(height=matrixHeight, width=matrixWidth, startGoal=startGoal)

    blockedList = drawPolygon(polyList, matrixHeight, matrixWidth)
    # print(blockedList[0][1])

    blockedList[startGoal[1]][startGoal[0]] = '@'
    blockedList[startGoal[3]][startGoal[2]] = '@@'
    
    
    calcCost(blockedList,matrixHeight,matrixWidth,startGoal)
    UCS(blockedList,2,2,matrixHeight,matrixWidth)
    # arrayCost =np.copy(blockedList)
   
    # print("block:")
    # blockedList.reverse()
    # for i in blockedList:
    #     print(i)
    
    
    # calcCost(arrayCost,matrixHeight,matrixWidth,startGoal)
    # print("calcCost:")
    
    # print(arrayCost[16][19])

    # print(arrayHeu[16][19])
    # print("test usc :")
    # # 
    # print(arrayCost[4][4])
    # UCS(arrayCost,2,2,matrixHeight,matrixWidth)
    # print(startGoal[1],startGoal[0])
    turtle.mainloop()
    
main()