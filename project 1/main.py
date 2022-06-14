from tracemalloc import start
import turtle
from unicodedata import name

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

    return pixel, startGoal, numOfPoly, polyList

# draw grid based on width, height
def drawGrid(height, width):
    tur = turtle.Turtle()
    tur.fillcolor('cyan')

    height += 1
    width += 1

    turtle.tracer(0)
    # tur.penup()
    tur.speed(100)
    tur.left(90) 

    tur.up()
    tur.setpos(-400, -200)
    tur.down()
    
    tur.fillcolor("grey")
    tur.begin_fill()
    tur.forward(height * 30)
    tur.right(90)
    tur.forward(width * 30)
    tur.right(90)
    tur.forward(height * 30)
    tur.right(90)
    tur.forward(width * 30)
    tur.end_poly()
    tur.right(90)
    tur.end_fill()

    tur.up()
    tur.setpos(-370, -170)
    tur.down()
    tur.fillcolor("white")
    tur.begin_fill()
    tur.forward(height * 30 - 60)
    tur.right(90)
    tur.forward(width * 30 - 60)
    tur.right(90)
    tur.forward(height * 30 - 60)
    tur.right(90)
    tur.forward(width * 30 - 60)
    tur.end_poly()
    tur.right(90)
    tur.end_fill()

    x = -400
    for i in range(width):
        tur.up()
        tur.setpos(x, -200)
        tur.down()
        tur.forward(height * 30) 
        x += 30


    tur.right(90)
    y = -200
    for i in range(height):
        tur.up()
        tur.setpos(-400, y)
        tur.down()

        tur.forward(width * 30)
        y += 30
    

    y = -190
    for i in range(height):
        tur.up()
        tur.setpos(-410, y)
        
        tur.write(i, align="right",font=('Arial', 10, 'bold'))
        tur.down()

        y += 30

    x = -390
    for i in range(width):
        tur.up()
        tur.setpos(x, -217)
        
        tur.write(i, align="center",font=('Arial', 10, 'bold'))
        tur.down()

        x += 30

    turtle.tracer(1)
    tur.hideturtle()

def fillPixel(x, y, color):
    tur = turtle.Turtle()
    tur.hideturtle()

    tur.fillcolor("cyan")

    tur.up()
    tur.setpos(-400 + x * 30, -200 + y * 30)
    tur.down()

    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(4):
        tur.forward(30)
        tur.left(90)
    tur.end_fill()

def drawPolygon(polygonList, height, width):    
    blockedPosList = [([0] * width)] * height
    turtle.tracer(0)
    for i in range(len(polygonList)):
        for j in range(0, len(polygonList[i]) - 1, 2):
            fillPixel(polygonList[i][j], polygonList[i][j + 1], "black")
            
    turtle.tracer(1)

    return blockedPosList

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