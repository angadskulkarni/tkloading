import tkinter as tk
from tkinter import *
import tkloading as tkl


root = tk.Tk()
root.geometry("800x500+300+100")
condition = True

def cancel(event = None):
    global condition
    condition = False
    print("Process Terminated by User")
    tkl.endwait(root)

def onclick(event = None):
    global condition
    tkl.waiting(root, scale = 0.5)
    for i in range(2000):
        if not condition: break
        g = i*2
        print(g)
        root.update()
    tkl.endwait(root)

B = tk.Button(root, text = "A Time Taking Process Starts Here", command = onclick)
B.pack(padx = 50, pady = 50)
L = tk.Label(root, text = "Press ctrl + E to cancel the process anytime in between")
L.pack(padx = 50, pady = (0,50))


root.bind('<Control-e>', cancel)
root.bind('<Control-E>', cancel)

root.mainloop()
