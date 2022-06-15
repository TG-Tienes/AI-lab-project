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
def drawGrid(height, width):
    tur = turtle.Turtle()
    tur.fillcolor('cyan')

    height += 1
    width += 1
    initX = -400
    initY = -300

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
    

    y = initY - 10
    for i in range(height):
        tur.up()
        tur.setpos(initX - 10, y)
        
        tur.write(i, align="center",font=('Arial', 10, 'bold'))
        tur.down()

        y += 35

    x = initX + 10
    for i in range(width):
        tur.up()
        tur.setpos(x, initY - 15)
        
        tur.write(i, align="center",font=('Arial', 10, 'bold'))
        tur.down()

        x += 35

    turtle.tracer(1)
    tur.hideturtle()

def fillPixel(x, y, color):
    tur = turtle.Turtle()
    tur.speed(0)
    tur.hideturtle()

    tur.fillcolor("cyan")

    tur.up()
    tur.setpos(-400 + x * 35, -300 + y * 35)
    tur.down()

    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(4):
        tur.forward(35)
        tur.left(90)
    tur.end_fill()

def drawPolygon(polygonList, height, width):    
    turtle.tracer(0)
    for i in range(len(polygonList)):
        for j in range(len(polygonList[i])):
            x = polygonList[i][j][0]
            y = polygonList[i][j][1]

            if j + 1 < len(polygonList[i]):
                nextX = polygonList[i][j + 1][0]
                nextY =  polygonList[i][j + 1][1]
                
                stepX = stepY = 1
                if x > nextX:
                    stepX = -1
                if y > nextY:
                    stepY = -1
                for r in range(x, nextX, stepX):
                    for s in range(y, nextY, stepY):
                        fillPixel(r, s, "red")
    
    for i in range(len(polygonList)):
        for j in range(len(polygonList[i])):
            fillPixel( polygonList[i][j][0], polygonList[i][j][1], "black")        

            
    turtle.tracer(1)

def main():
    pixel, startGoal, numOfPoly, polyList = readInputFile(fname="input.txt")
    height = 1000
    width = 1680

    # init screen
    screen = turtle.Screen()
    screen.setup(width, height)

    drawGrid(height=pixel[1], width=pixel[0])

    blockedList = drawPolygon(polyList, pixel[1], pixel[0])

    # print(len(blockedList))
    # print(blockedList[2][2])
    # # for i in range(len(blockedList)):
    # #     print(blockedList[i])
    turtle.mainloop()

main()