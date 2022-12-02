import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pickle


ind = 0
wait = None

class ModuleBrokenError(Exception):
    '''This is an Exception Class for internal use of this module.'''
    pass


def waiting(top, offset_x = 0, offset_y = 0, scale = 1):
    '''Parameters - top: tkinter Toplevel Widget
                    offset_x: offset pixel number in X direction can be positive or negative
                    offset_y: offset pixel number in Y direction can be positive or negative
                    scale: size of the loading widget - 0.125, 0.25, 0.5, 1, 2, 3, 4, etc'''
    
    global ind, wait
    frameCnt = 26
    ind = 0
    #frames = [PhotoImage(file='preloader.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    #frames = PhotoImage(file='preloader.gif')

    def resize_frames(frames, scale):
        new_frames = []
        for frame in frames:
            if scale >= 1:
                new = frame.zoom(x = int(scale))
            elif scale < 1 and scale > 0:
                new = frame.subsample(x = int(1/scale))
            new_frames.append(new)
        return new_frames
    

    wait = tk.Toplevel(top)
    #wait.geometry("+400+200")
    wait.resizable(height = FALSE, width = FALSE)
    wait.config(bg = 'yellow')

    def update(ind):
        #global ind
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        L.config(image = frame)
        tkx = top.winfo_x()+top.winfo_width()/2-wait.winfo_width()/2+offset_x
        tky = top.winfo_y()+top.winfo_height()/2-wait.winfo_height()/2+offset_y
        wait.geometry("+"+str(int(tkx))+"+"+str(int(tky)))
        wait.after(20, update, ind)
    
    try:
        wait.wm_attributes('-type', 'splash')
    except Exception:
        wait.overrideredirect(True)
    wait.wait_visibility(wait)
    #wait.attributes('-alpha',0.3)
    wait.wm_attributes('-transparentcolor','yellow')
    #img = Image.open('preloader.gif')
    #frames = ImageTk.PhotoImage(image = img.resize((200, 200)))
    try:
        frames = [PhotoImage(file='module_data.vtdt',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    except:
        raise ModuleBrokenError("Looks like the module is missing its important files. Try reinstalling the module")
    frames = resize_frames(frames, scale)
    L = tk.Label(wait, image = frames[0], bg = 'yellow')
    L.pack()


    wait.after(0, update, 0)
    wait.grab_set()
    wait.lift()
    wait.bind('<Control-e>', endwait)
    wait.bind('<Control-E>', endwait)
    #wait.mainloop()
    


def endwait(top = None):
    '''Parameters - top: tkinter Toplevel Widget'''
    
    global wait
    try:
        wait.destroy()
    except:
        pass




'''This is an Example Script to use the module'''

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x500+300+100")
    condition = True

    def cancel(event = None):
        global condition
        condition = False
        print("Process Terminated by User")
        endwait(root)

    def onclick(event = None):
        global condition
        waiting(root, scale = 0.125)
        for i in range(2000):
            if not condition: break
            g = i*2
            print(g)
            root.update()
        endwait(root)

    B = tk.Button(root, text = "Wait Here", command = onclick)
    B.pack(padx = 50, pady = 50)

    
    root.bind('<Control-e>', cancel)
    root.bind('<Control-E>', cancel)
    
    root.mainloop()
