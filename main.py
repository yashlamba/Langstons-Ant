import tkinter as tk
from tkinter import ALL


class mainFrame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, height=400, width=400)
        self.canvas.pack()
        self.steps = tk.IntVar()
        self.stepsLabel = tk.Entry(
                            self.master,
                            textvariable=self.steps,
                            width=15
                        )
        self.stepsLabel.pack()
        self.submitButton = tk.Button(
                                self.master,
                                command=self.antMovement,
                                text="GO!",
                                justify="center",
                            )
        self.submitButton.pack()
        self.grid = [[-1 for j in range(400)] for i in range(400)]
        self.antX = 200
        self.antY = 200
        self.antDir = 3
        self.scaleBar = tk.Scale(
                            self.master,
                            from_=1,
                            to=2,
                            resolution=0.1,
                            orient='horizontal',
                            command=lambda x: self.scale(
                                                    self.scaleBar.get()*1.0
                                                    ),
                            length=100,
                        )
        self.scaleBar.set(1)
        self.prevScale = 0
        self.scaleBar.pack(anchor='e')

    def scale(self, scaleAmount):
        if self.scaleBar.get() > self.prevScale:
            self.canvas.scale(ALL, 200, 200, scaleAmount, scaleAmount)
        elif self.scaleBar.get() < self.prevScale:
            self.canvas.scale(
                        ALL, 200, 200,
                        1.0/(scaleAmount+0.1),
                        1.0/(scaleAmount+0.1),
                    )
        self.prevScale = self.scaleBar.get()

    def antMovement(self):
        for i in range(int(self.stepsLabel.get())):
            self.ant()
        self.createGrid()
        self.grid = [[-1 for j in range(400)] for i in range(400)]
        self.antX = 200
        self.antY = 200
        self.antDir = 3

    def turnLeft(self):
        if self.antDir % 4 == 0:
            self.antX += 1
        elif self.antDir % 4 == 1:
            self.antY -= 1
        elif self.antDir % 4 == 2:
            self.antX -= 1
        else:
            self.antY += 1
        self.antDir += 1

    def turnRight(self):
        if self.antDir % 4 == 0:
            self.antX -= 1
        elif self.antDir % 4 == 1:
            self.antY += 1
        elif self.antDir % 4 == 2:
            self.antX += 1
        else:
            self.antY -= 1
        self.antDir -= 1

    def ant(self):
        if self.grid[self.antX][self.antY] == -1:
            self.grid[self.antX][self.antY] *= -1
            self.turnRight()
        elif self.grid[self.antX][self.antY] == 1:
            self.grid[self.antX][self.antY] *= -1
            self.turnLeft()

    def createGrid(self):
        for i in range(400):
            for j in range(400):
                if self.grid[i][j] == -1:
                    self.canvas.create_rectangle(i, j, i, j, outline='white')
                else:
                    self.canvas.create_rectangle(i, j, i, j, outline='red')


def main():
    root = tk.Tk(className="Langston's Ant")
    root.geometry("400x500")
    root.title("Langston's Ant")
    root.call("wm", "iconphoto", root._w, tk.PhotoImage(file="logo.png"))
    root.resizable(False, False)
    app = mainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
