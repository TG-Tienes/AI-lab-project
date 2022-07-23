from re import T
from tabnanny import check
import turtle
import numpy as np
from queue import PriorityQueue
from collections import deque
import math
import random

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
    turtle.tracer(123192381928319273192387192)
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
    blockedList = [ [ '.' for i in range(width) ] for j in range(height) ]

    for i in range(0, len(polygonList), 1):
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



def UCS(blockedList,startGoal,matrixHeight,matrixWidth):
    #thong so cua me cung 
    length, width = matrixHeight, matrixWidth
    tur=turtle.Turtle()
    # hang doi frontier cua thuat toan
    queue = PriorityQueue()

    #them vao frontier x,y cua diem xuat phat, voi "" se dung de luu str huong di sau nay
    queue.put((0,startGoal[1], startGoal[0], ""))

    #4 huong agent co the di
    way = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    #tao noi luu tru thong tin tin cac vi tri chua duoc truy cap den
    visited =[[0 for x in range(width)] for y in range(length)] 
    
    # danh dau da di den diem bat dau
    visited[startGoal[1]][startGoal[0]] = True


    #dieu kien lap cho den khi trong frontier khong con phan tu nao
    while not queue.empty():
        
        #lay ra khoi frontier
        agentInfo = queue.get()
        
        
        #danh dau vi tri da truy cap den  
        visited[agentInfo[1]][agentInfo[2]] = True

        # trong vong for nay huong se chay 4 lan, do agent duoc phep di 4 huong (len xuong trai phai) 
        for n_e_s_w in way:

            # cap nhat lai toa do x,y sau khi di chuyen theo 1 huong
            x, y = agentInfo[1] + n_e_s_w[0], agentInfo[2] + n_e_s_w[1]
           
            
            #kiem tra huong di nay co hop le hay khong theo cac qui dinh yeu cau cua de bai
            #neu khong hop le quay ve va doi sang huong di khac
            if (x < 1 or x >=length or y < 1 or y >= width or blockedList[x][y] == "%" or visited[x][y] == True):
                continue
            else:
                #neu huong di den vi tri goal
                if blockedList[x][y] == "@@":
                    # lay cac huong di da di de den goal
                    dir = str(agentInfo[3])
                    dir = dir.split()
                    #dat vi tri ve diem bat dau
                    a = startGoal[1]
                    b = startGoal[0]
                    cost=1# do khi den goal can di chuyen 1 lan nen cost se dat la 1 
                    costVisited=0 # bien dem chi phi mo rong                       
                    for i in dir:
                        cost+=1
                        #voi L,X,T,P(len,xuong,trai,phai) la cac huong di
                        # cap nhap lai vi tri de danh dau
                        if i == "L":
                            b = b + 1
                        elif i == "X":
                            b = b - 1
                        elif i == "T":
                            a = a - 1
                        elif i == "P":
                            a = a + 1
                        #danh dau path den dich
                        fillPixel(b,a,"crimson")
                    # hien thi cost path ra man hinh
                    for y in range(width):
                        for x in range(length):
                            if visited[x][y]:
                                costVisited+=1
                    tur.up()
                    tur.setpos(-100,-450)
                    #vi tri bat dau se khong tinh vao cost-path
                    tur.write("Cost of final path: "+str(cost) +"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
                    tur.down()
                    return
                # danh dau da ghe tham
                visited[x][y] = True  # danh dau da di quq
                if (blockedList[x][y] != "%"):
                    fillPixel(y,x,"violet")
                # luu vao queue gom toa do x, y, pathcost, huong di cua moi o
                
                # 
                if n_e_s_w == [0, 1]:
                    queue.put((agentInfo[0]+1,x, y, agentInfo[3] + " L"))
                elif n_e_s_w == [0, -1]:
                    queue.put((agentInfo[0]+1,x, y, agentInfo[3] + " X"))
                elif n_e_s_w == [-1, 0]:
                    queue.put((agentInfo[0]+1,x, y, agentInfo[3] + " T"))
                elif n_e_s_w == [1, 0]:
                    queue.put((agentInfo[0]+1,x, y, agentInfo[3] + " P"))
    costVisited=0 # bien dem chi phi mo rong   
    for y in range(width):
        for x in range(length):
            if visited[x][y]:
                costVisited+=1

    tur.up()
    tur.setpos(-100,-450)
    tur.write("No path to goal!"+"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
    tur.down()
    return 


def calcHeuristics(height, width, goal):
    heuristicList = [ [ 0 for i in range(width) ] for j in range(height) ]
    for i in range(height):
        for j in range(width):
            heuristicList[i][j] = abs(goal[3] - i) + abs(goal[2] - j)
    return heuristicList
def GBFS(blockedList,startGoal,matrixHeight,matrixWidth):
    # tham khao https://www.youtube.com/watch?v=dv1m3L6QXWs
    #thong so cua me cung 
    length, width = matrixHeight, matrixWidth
    tur=turtle.Turtle()
    # hang doi frontier cua thuat toan
    queue = PriorityQueue()
    # f(n) mahatan
    heu=calcHeuristics(matrixHeight,matrixWidth,startGoal)
    #them vao frontier x,y cua diem xuat phat, voi "" se dung de luu str huong di sau nay
    queue.put((heu[startGoal[1]][startGoal[0]],startGoal[1], startGoal[0], ""))

    #4 huong agent co the di
    way = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    #tao noi luu tru thong tin tin cac vi tri chua duoc truy cap den
    visited =[[0 for x in range(width)] for y in range(length)] 
    
    # danh dau da di den diem bat dau
    visited[startGoal[1]][startGoal[0]] = True


    #dieu kien lap cho den khi trong frontier khong con phan tu nao
    while not queue.empty():
        
        #lay ra khoi frontier
        agentInfo = queue.get()
        
        
        #danh dau vi tri da truy cap den  
        visited[agentInfo[1]][agentInfo[2]] = True

        # trong vong for nay huong se chay 4 lan, do agent duoc phep di 4 huong (len xuong trai phai) 
        for n_e_s_w in way:

            # cap nhat lai toa do x,y sau khi di chuyen theo 1 huong
            x, y = agentInfo[1] + n_e_s_w[0], agentInfo[2] + n_e_s_w[1]
           
            
            #kiem tra huong di nay co hop le hay khong theo cac qui dinh yeu cau cua de bai
            #neu khong hop le quay ve va doi sang huong di khac
            if (x < 1 or x >=length or y < 1 or y >= width or blockedList[x][y] == "%" or visited[x][y] == True):
                continue
            else:
                
                #neu huong di den vi tri goal
                if blockedList[x][y] == "@@":
                    # lay cac huong di da di de den goal
                    dir = str(agentInfo[3])
                    dir = dir.split()
                    #dat vi tri ve diem bat dau
                    a = startGoal[1]
                    b = startGoal[0]
                    cost=1# do khi den goal can di chuyen 1 lan nen cost se dat la 1   
                    costVisited=0 # bien dem chi phi mo rong                   
                    for i in dir:
                        cost+=1
                        #voi L,X,T,P(len,xuong,trai,phai) la cac huong di
                        # cap nhap lai vi tri de danh dau
                        if i == "L":
                            b = b + 1
                        elif i == "X":
                            b = b - 1
                        elif i == "T":
                            a = a - 1
                        elif i == "P":
                            a = a + 1
                        #danh dau path den dich
                        fillPixel(b,a,"crimson")
                    # hien thi cost path ra man hinh
                    
                    for y in range(width):
                        for x in range(length):
                            if visited[x][y]:
                                costVisited+=1

                    tur.up()
                    tur.setpos(-100,-450)
                    #vi tri bat dau se khong tinh vao cost-path
                    tur.write("Cost of final path: "+str(cost) +"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))

                    tur.down()
                    return
                # danh dau da ghe tham
                visited[x][y] = True  # danh dau da di quq
                if (blockedList[x][y] != "%"):
                    fillPixel(y,x,"violet")
                # luu vao queue gom toa do x, y, pathcost, huong di cua moi o
                
                # 
                if n_e_s_w == [0, 1]:
                    queue.put((heu[x][y],x, y, agentInfo[3] + " L"))
                elif n_e_s_w == [0, -1]:
                    queue.put((heu[x][y],x, y, agentInfo[3] + " X"))
                elif n_e_s_w == [-1, 0]:
                    queue.put((heu[x][y],x, y, agentInfo[3] + " T"))
                elif n_e_s_w == [1, 0]:
                    queue.put((heu[x][y],x, y, agentInfo[3] + " P"))

    #khong tim ra path
    costVisited=0 # bien dem chi phi mo rong   
    for y in range(width):
        for x in range(length):
            if visited[x][y]:
                costVisited+=1

    tur.up()
    tur.setpos(-100,-450)
    tur.write("No path to goal!"+"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
    tur.down()
    return 



 
frontierGlobal=deque()
solutionGlobal={}
visitedGlobal= set()
def DLS(x,y,l,blockedList,visitedGlobal,matrixHeight, matrixWidth,startGoal):
    frontierGlobal.append((l, (x, y)))# hang doi
    solutionGlobal[x, y] = x, y # luu vet de tim path
    
    length, width = matrixHeight, matrixWidth
    color_Table = ['RED','BLUE','teal','purple','pink','crimson','brown','orange','beige','violet']
    color=color_Table[random.randint(0,8)]
    while len(frontierGlobal) != 0:
        (l, (x, y)) = frontierGlobal.pop()
        if (x, y) == (startGoal[3],startGoal[2]):
            return True#tim ra goal
        if (x, y) != (startGoal[1],startGoal[0])and (x, y) != (startGoal[3],startGoal[2]) :
            fillPixel(y,x,color)#to mau vi tri hien tai
        if l == 0:#dieu kien dung
            continue
        #cac huong di cua agent 
        if (x-1 > 0 and x-1 <length and y >0 and y < width and blockedList[x-1][y] != "%" and (x-1,y)not in visitedGlobal ):
            cellleft = (x - 1, y)
            solutionGlobal[cellleft] = x, y
            frontierGlobal.append((l - 1, cellleft))
            visitedGlobal.add(cellleft)
        if (x > 0 and x <length and y-1 >0 and y-1 < width and blockedList[x][y-1] != "%" and (x,y-1)not in visitedGlobal):
            celldown = (x, y - 1)
            solutionGlobal[celldown] = x, y
            frontierGlobal.append((l - 1, celldown))
            visitedGlobal.add(celldown)
        if (x > 0 and x <length and y+1 >0 and y+1 < width and blockedList[x][y+1] != "%" and (x,y+1)not in visitedGlobal):
            cellup = (x, y + 1)
            solutionGlobal[cellup] = x, y
            frontierGlobal.append((l - 1, cellup))
            visitedGlobal.add(cellup)
        if (x +1> 0 and x+1 <length and y >0 and y < width and blockedList[x+1][y] != "%" and (x+1,y)not in visitedGlobal):
            cellright = (x + 1, y)
            solutionGlobal[cellright] = x, y
            frontierGlobal.append((l - 1, cellright))
            visitedGlobal.add(cellright)
    return False#frontier khong con phan tu va khong tim ra duoc goal
def IDS(x, y,matrixHeight,matrixWidth,blockedList,startGoal):
    l = 1#khoi tai do sau
    tur = turtle.Turtle()
    while(DLS(x,y,l,blockedList,visitedGlobal,matrixHeight, matrixWidth,startGoal) == False):#lap den khi tim duoc goal
        
        #reset lai cac bien gloabl 
        visitedGlobal.clear()
        frontierGlobal.clear()
        solutionGlobal.clear()
        # print("loop:"+str(l))
        l += 1#tang do sau
        

        #dieu kien dung tranh truong hop lap vo han
        if l > (matrixHeight * matrixWidth):# dieu kien nay du de cho thuat toan tim het tat ca cac vi tri trong maze
            tur.up()
            tur.setpos(-100,-450)
            tur.write("No path found",False, align="center",font=('Arial', 18, 'bold'))#khong tim duoc goal trong maze 
            tur.down()
            return False
    

    return True

def traceBack(startGoal):#ham truy nguoc lai tim path va path cost
    cost = 0
    tur = turtle.Turtle()
    x,y=startGoal[3],startGoal[2]

    #khong to mau vo 2 vi tri goal va start
    while (x, y) != (startGoal[1], startGoal[0]):    
        if(x, y) != (startGoal[3], startGoal[2]):
            fillPixel(y,x,"cyan")
        
        cost += 1                          
        x, y = solutionGlobal[x, y]
                     
    tur.up()
    tur.setpos(-100,-450)
    tur.write("Cost of final path: "+str(cost) +"    Cost of expanded node: "+str(len(visitedGlobal)), align="center",font=('Arial', 18, 'bold'))
    tur.down()

def SolveBFS(blockedList,startGoal,matrixHeight,matrixWidth):
    #thong so cua me cung 
    length, width = matrixHeight, matrixWidth
    tur=turtle.Turtle()
    # hang doi frontier cua thuat toan
    queue = deque()

    #them vao frontier x,y cua diem xuat phat, voi "" se dung de luu str huong di sau nay
    queue.append((startGoal[1], startGoal[0], ""))

    #4 huong agent co the di
    way = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    #tao noi luu tru thong tin tin cac vi tri chua duoc truy cap den
    visited =[[0 for x in range(width)] for y in range(length)] 
    
    # danh dau da di den diem bat dau
    visited[startGoal[1]][startGoal[0]] = True


    #dieu kien lap cho den khi trong frontier khong con phan tu nao
    while  len(queue)!=0:
        
        #lay ra khoi frontier
        agentInfo = queue.popleft()
        
        
        #danh dau vi tri da truy cap den  
        visited[agentInfo[0]][agentInfo[1]] = True

        # trong vong for nay huong se chay 4 lan, do agent duoc phep di 4 huong (len xuong trai phai) 
        for n_e_s_w in way:

            # cap nhat lai toa do x,y sau khi di chuyen theo 1 huong
            x, y = agentInfo[0] + n_e_s_w[0], agentInfo[1] + n_e_s_w[1]
           
            
            #kiem tra huong di nay co hop le hay khong theo cac qui dinh yeu cau cua de bai
            #neu khong hop le quay ve va doi sang huong di khac
            if (x < 1 or x >=length or y < 1 or y >= width or blockedList[x][y] == "%" or visited[x][y] == True):
                continue
            else:
                #neu huong di den vi tri goal
                if blockedList[x][y] == "@@":
                    # lay cac huong di da di de den goal
                    dir = str(agentInfo[2])
                    dir = dir.split()
                    #dat vi tri ve diem bat dau
                    a = startGoal[1]
                    b = startGoal[0]
                    cost=1# do khi den goal can di chuyen 1 lan nen cost se dat la 1 
                    costVisited=0 # bien dem chi phi mo rong                       
                    for i in dir:
                        cost+=1
                        #voi L,X,T,P(len,xuong,trai,phai) la cac huong di
                        # cap nhap lai vi tri de danh dau
                        if i == "L":
                            b = b + 1
                        elif i == "X":
                            b = b - 1
                        elif i == "T":
                            a = a - 1
                        elif i == "P":
                            a = a + 1
                        #danh dau path den dich
                        fillPixel(b,a,"crimson")
                    # hien thi cost path ra man hinh
                    for y in range(width):
                        for x in range(length):
                            if visited[x][y]:
                                costVisited+=1
                    tur.up()
                    tur.setpos(-100,-450)
                    #vi tri bat dau se khong tinh vao cost-path
                    tur.write("Cost of final path: "+str(cost) +"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
                    tur.down()
                    return
                # danh dau da ghe tham
                visited[x][y] = True  # danh dau da di quq
                if (blockedList[x][y] != "%"):
                    fillPixel(y,x,"violet")
                # luu vao queue gom toa do x, y, pathcost, huong di cua moi o
                
                # 
                if n_e_s_w == [0, 1]:
                    queue.append((x, y, agentInfo[2] + " L"))
                elif n_e_s_w == [0, -1]:
                    queue.append((x, y, agentInfo[2] + " X"))
                elif n_e_s_w == [-1, 0]:
                    queue.append((x, y, agentInfo[2] + " T"))
                elif n_e_s_w == [1, 0]:
                    queue.append((x, y, agentInfo[2] + " P"))
    costVisited=0 # bien dem chi phi mo rong   
    for y in range(width):
        for x in range(length):
            if visited[x][y]:
                costVisited+=1

    tur.up()
    tur.setpos(-100,-450)
    tur.write("No path to goal!"+"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
    tur.down()
    return   

    
    
def SolveAstar(blockedList,startGoal,matrixHeight,matrixWidth):
    #thong so cua me cung 
    length, width = matrixHeight, matrixWidth
    tur=turtle.Turtle()
    # hang doi frontier cua thuat toan
    queue = deque()

    #them vao frontier x,y cua diem xuat phat, voi "" se dung de luu str huong di sau nay
    queue.appendleft((startGoal[1], startGoal[0], 0, calc_heuristic((startGoal[1],startGoal[0]), (startGoal[3],startGoal[2])) + 0, ""))

    #4 huong agent co the di
    way = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    #tao noi luu tru thong tin tin cac vi tri chua duoc truy cap den
    visited =[[0 for x in range(width)] for y in range(length)] 
    
    # danh dau da di den diem bat dau
    visited[startGoal[1]][startGoal[0]] = True


    #dieu kien lap cho den khi trong frontier khong con phan tu nao
    while len(queue) !=0:
        queue = deque(sorted(queue, key=lambda x: x[3], reverse=True)) #priority queue
        #lay ra khoi frontier
        agentInfo = queue.pop()
        
        
        #danh dau vi tri da truy cap den  
        visited[agentInfo[0]][agentInfo[1]] = True

        # trong vong for nay huong se chay 4 lan, do agent duoc phep di 4 huong (len xuong trai phai) 
        for n_e_s_w in way:

            # cap nhat lai toa do x,y sau khi di chuyen theo 1 huong
            x, y = agentInfo[0] + n_e_s_w[0], agentInfo[1] + n_e_s_w[1]
           
            
            #kiem tra huong di nay co hop le hay khong theo cac qui dinh yeu cau cua de bai
            #neu khong hop le quay ve va doi sang huong di khac
            if (x < 1 or x >=length or y < 1 or y >= width or blockedList[x][y] == "%" or visited[x][y] == True):
                continue
            else:
                #neu huong di den vi tri goal
                if blockedList[x][y] == "@@":
                    # lay cac huong di da di de den goal
                    dir = str(agentInfo[4])
                    dir = dir.split()
                    #dat vi tri ve diem bat dau
                    a = startGoal[1]
                    b = startGoal[0]
                    cost=1# do khi den goal can di chuyen 1 lan nen cost se dat la 1 
                    costVisited=0 # bien dem chi phi mo rong                       
                    for i in dir:
                        cost+=1
                        #voi L,X,T,P(len,xuong,trai,phai) la cac huong di
                        # cap nhap lai vi tri de danh dau
                        if i == "L":
                            b = b + 1
                        elif i == "X":
                            b = b - 1
                        elif i == "T":
                            a = a - 1
                        elif i == "P":
                            a = a + 1
                        #danh dau path den dich
                        fillPixel(b,a,"crimson")
                    # hien thi cost path ra man hinh
                    for y in range(width):
                        for x in range(length):
                            if visited[x][y]:
                                costVisited+=1
                    tur.up()
                    tur.setpos(-100,-450)
                    #vi tri bat dau se khong tinh vao cost-path
                    tur.write("Cost of final path: "+str(cost) +"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
                    tur.down()
                    return
                # danh dau da ghe tham
                visited[x][y] = True  # danh dau da di quq
                if (blockedList[x][y] != "%"):
                    fillPixel(y,x,"violet")
                # luu vao queue gom toa do x, y, pathcost, huong di cua moi o
                
                # 
                if n_e_s_w == [0, 1]:
                    queue.appendleft((x, y, agentInfo[2]+1,calc_heuristic((x,y), (startGoal[3],startGoal[2]))+agentInfo[2]+1,agentInfo[4] + " L"))
                elif n_e_s_w == [0, -1]:
                    queue.appendleft((x, y,agentInfo[2]+1,calc_heuristic((x,y), (startGoal[3],startGoal[2]))+agentInfo[2]+1, agentInfo[4] + " X"))
                elif n_e_s_w == [-1, 0]:
                    queue.appendleft((x, y,agentInfo[2]+1,calc_heuristic((x,y), (startGoal[3],startGoal[2]))+agentInfo[2]+1, agentInfo[4] + " T"))
                elif n_e_s_w == [1, 0]:
                    queue.appendleft((x, y,agentInfo[2]+1,calc_heuristic((x,y), (startGoal[3],startGoal[2]))+agentInfo[2]+1, agentInfo[4] + " P"))
    costVisited=0 # bien dem chi phi mo rong   
    for y in range(width):
        for x in range(length):
            if visited[x][y]:
                costVisited+=1

    tur.up()
    tur.setpos(-100,-450)
    tur.write("No path to goal!"+"    Cost of expanded node: "+str(costVisited), align="center",font=('Arial', 18, 'bold'))
    tur.down()
    return 



def calc_heuristic(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def main():
   
    choice = 0
    option = 0
    while True:
        tur = turtle.Turtle()
        turtle.clearscreen()
        
        # turtle.done()
       
        print('1. Breadth-first search')
        print('2. Uniform-cost search')
        print('3. Iterative deepening searh')
        print('4. Greedy-best first search ')
        print('5. Graph-search A* ')

        choice = input('Choose Searching Algorithm: ')
        while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = input('Choose Searching Algorithm: ')
        
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
   

        blockedList[startGoal[1]][startGoal[0]] = '@'
        blockedList[startGoal[3]][startGoal[2]] = '@@'

        if choice == '1':
            print('\nBFS\nSearching...')
            GBFS(blockedList,startGoal,matrixHeight,matrixWidth)
        elif choice == '2':
            print('\nUCS\nSearching...')
            UCS(blockedList,startGoal,matrixHeight,matrixWidth)
        elif choice == '3':
            print('\nIDS\nSearching...')
            result= IDS(startGoal[1],startGoal[0],matrixHeight,matrixWidth,blockedList,startGoal)
            if result:
                traceBack(startGoal)
        elif choice == '4':
            print('\nGBFS\nSearching...')
            SolveBFS(blockedList,startGoal,matrixHeight,matrixWidth)
        elif choice == '5':
            print('\nA* Search\nSearching...')
            # SolveAstar2(blockedList,startGoal,matrixHeight,matrixWidth)
            SolveAstar(blockedList,startGoal,matrixHeight,matrixWidth)

        print()
        option = input('Do you want to continue (0: No, 1: Yes)? ')
        while option != '0' and option != '1':
            option = input('Do you want to continue (0: No, 1: Yes)? ')
        print()
        if option == '0':
            return
    # turtle.mainloop()

main()