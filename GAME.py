from tkinter import *

tk=Tk()
botFrame=Frame(tk)
botFrame.pack(side=BOTTOM)

tk.title("AIR HOCKEY GAME")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

#interface of game
canvas=Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
canvas.config(bg="light green")
tk.update()


canvas.create_text(250,60,text="___ WELCOME TO ___",fill="red",font=("algerian",20))
canvas.create_text(250,150,text="***AIR HOCKEY GAME***",fill="purple",font=("broadway",23))
canvas.create_line(100,170,400,170,fill="purple",width=3)
canvas.create_text(0,250,text="***********************************************************************************",fill="navy blue",font=("broadway",23))
canvas.create_text(250,270,text="INSTRUCTION FOR KEYS :",fill="black",font=("Showcard Gothic",15))
canvas.create_text(100,300,text="PLAYER 1 :",fill="brown4",font=("algerian",15))
canvas.create_text(200,330,text=" UP : W               DOWN : S",fill="deeppink",font=("Bernard MT Condensed",15))
canvas.create_text(100,380,text="PLAYER 2 :",fill="brown4",font=("algerian",15))
canvas.create_text(250,410,text=" UP  : UP ARROW KEY      DOWN : DOWN ARROW KEY",fill="deeppink",font=("Bernard MT Condensed",15))


def game_start():
    import levels
def end_game():
    import END


    
button1= Button(tk,text='Play',font=("Showcard Gothic",10),command = game_start,fg='yellow',bg='blue',width=10)
button1.pack(side=RIGHT)

button2=Button(tk,text='Exit',font=("Showcard Gothic",10),command = end_game,fg='white',bg='red',width=10)
button2.pack(side=LEFT)







