# Import the required Libraries
import tkinter as tk
import tkinter.filedialog as tkFileDiaglog

class app(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.geometry("1080x860")

        # browse file button
        tk.Button(self.root, text="Browse", command= lambda : self.openFile()).pack(pady=20)

    def openFile(self):
        file = tkFileDiaglog.askopenfile(mode = 'r', initialdir = '/', title = "Select file", filetypes=[("input TXT files", "*.txt")])
        
        if file:
            self.fileName = self.file.name
            self.matrix = file.read()
            self.file.close()


        
        

if __name__ == "__main__":
    root = tk.Tk()

    app(root).pack(side="top", fill="both", expand=True)

    root.mainloop()