from tkinter import *

tk=Tk()
tk.title("end game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)




canvas=Canvas(tk,width=500,height=250,bd=0,highlightthickness=0)
canvas.pack()
canvas.config(bg="navy blue")
tk.update()

canvas.create_text(250,60,text="*** THANK YOU ***",fill="deeppink",font=("Snap ITC",20))
canvas.create_text(250,150,text="Hope You Will Get Back Soon!!!",fill="yellow",font=("lucida handwriting",18))
canvas.create_line(20,170,465,170,fill="yellow",width=3)
