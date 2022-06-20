from re import T
from tabnanny import check
import turtle
import numpy as np

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
    tur.speed(0)
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

def drawPolygon(polygonList, height, width):    
    turtle.tracer(0)
    # turtle.speed(0)
    blockedList = [ [ '|' for i in range(width) ] for j in range(height) ]

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

            # print(x, y, nextX, nextY)
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

    for i in blockedList:
        print(i)
    
    turtle.mainloop()

main()