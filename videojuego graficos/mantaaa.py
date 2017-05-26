import time
import random
from tkinter import*
from tkinter import ttk
tk=Tk()
c= Canvas(tk,widt=1000,height=1000)
c.pack()
energia1= PhotoImage(file="energia1.png")
energia=c.create_image(125,60,image=energia1)


def energia1():

    c.move(1,0,6)
    if(c.coords(energia)[1]>1000):
        e=c.coords(energia)[0]
        f=random.randint(0,10)
        c.move(energia,f-e,-800)
        
    c.after(10,energia1)
   

energia1()
