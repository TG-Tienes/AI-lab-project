# Import the required Libraries
from ast import Str
from itertools import combinations
import tkinter as tk
import tkinter.filedialog as tkFileDiaglog
from matplotlib.pyplot import text
import numpy as np



class app(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.geometry("1280x960")
        self.fileDir = "asdasdsadsa"

        tk.Button(self.root, text="Browse", command= lambda : self.openFile()).pack(pady=5,padx=20,ipadx=50)

        self.textBox_fileDir = tk.Text(self.root, height = 2, width = 52)
        self.textBox_fileDir.pack(pady=0)
        self.textBox_fileDir.config(state='disabled')

        self.myCanvas = tk.Canvas(root, bg="white", height= 0, width= 0)
        tk.Button(self.root, text="Start", command= lambda : self.pySat()).pack(pady=5,padx=20,ipadx=50,ipady=20)


    def openFile(self):
        self.myCanvas.destroy()
        self.fileDir = tkFileDiaglog.askopenfilename(initialdir = '/', title = "Select file", filetypes=[("input TXT files", "*.txt")])
        file = open(self.fileDir)

        lines = []
        # Remove '\n' from each line
        for i in file:
            lines.append(i.strip())

        # assign numbers to temp 2D array
        matrixList = [[int(number) for number in line.split(',')] for line in lines]       
        
        # convert temp 2D array to numpy array
        self.matrix = np.array(matrixList)

        # Show file directory text on tkinter UI
        self.textBox_fileDir.config(state='normal')
        self.textBox_fileDir.delete(1.0,'end')
        self.textBox_fileDir.insert('end', self.fileDir)
        self.textBox_fileDir.config(state='disabled')

        # dim of result matrix
        self.matrixRow, self.matrixCol = len(self.matrix), len(self.matrix[0])

        self.drawBoard()

    def drawBoard(self):
        squareSize = 40
        canvasHeight, canvasWidth = self.matrixRow * squareSize, self.matrixCol * squareSize
        self.myCanvas = tk.Canvas(root, bg="white", height= canvasHeight, width= canvasWidth)
        y0, y1 = 2, squareSize+1
        for i in range(self.matrixRow):
            x0, x1 = 2, squareSize+1
            for j in range(self.matrixCol):
                self.myCanvas.create_rectangle((x0,y0),(x1,y1),fill='red')
                
                temp = self.matrix[i][j]
                if temp != -1:
                    self.myCanvas.create_text((x0 + squareSize/2, y0 + squareSize/2), text=temp)

                x0 += squareSize
                x1 += squareSize
            y0 += squareSize
            y1 += squareSize
        self.myCanvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def isValid(self, row, col):
        return row >= 0 and col >= 0 and row < self.matrixRow and col < self.matrixCol

    def pySat(self):
        self.finalMatrix = np.zeros((self.matrixRow, self.matrixCol), dtype=bool)

        rowAdj = [-1,0,1,-1,0,1,-1,0,1]
        colAdj = [-1,-1,-1,0,0,0,1,1,1]

        for row in range(self.matrixRow):
            squareAdj = []
            for col in range(self.matrixCol):
                if self.matrix[row][col] < 0:
                    continue
                for k in range(9):
                    tempRow, tempCol = row + rowAdj[k], col + colAdj[k]
                    if self.isValid(tempRow, tempCol):
                        squareAdj.append(self.matrix[tempRow][tempCol])
                print(combinations(squareAdj, self.matrix[row][col]))
    

if __name__ == "__main__":
    root = tk.Tk()

    app(root).pack(side="top", fill="both", expand=True)

    root.mainloop()