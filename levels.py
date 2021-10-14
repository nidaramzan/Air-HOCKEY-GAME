from tkinter import *
tk=Tk()


tk.title("LEVELS")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

#interface of game
canvas=Canvas(tk,width=400,height=200,bd=0,highlightthickness=0)
canvas.grid()
canvas.config(bg="wheat1")
tk.update()


canvas=Canvas(tk,width=400,height=70,bd=0,highlightthickness=0)
canvas.grid()
canvas.config(bg="wheat1")
tk.update()

def easy_level():
    import easy
button1= Button(tk,text='Easy',font=("Showcard Gothic",15),command = easy_level,fg='red',bg='turquoise1',width=13)
button1.grid(row=1,column=0)

canvas=Canvas(tk,width=400,height=50,bd=0,highlightthickness=0)
canvas.grid()
canvas.config(bg="wheat1")
tk.update()
    
def medium_level():
    import medium
button2=Button(tk,text='Medium',font=("Showcard Gothic",15),command = medium_level,fg='black',bg='olivedrab1',width=13)
button2.grid(row=2,column=0)

canvas=Canvas(tk,width=400,height=70,bd=0,highlightthickness=0)
canvas.grid()
canvas.config(bg="wheat1")
tk.update()

def hard_level():
    import hard

button3=Button(tk,text='Hard',font=("Showcard Gothic",15),command = hard_level,fg='white',bg='red',width=13)
button3.grid(row=3,column=0)


