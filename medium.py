from tkinter import *
import random
import time
import tkinter.messagebox
counter=0
counter1=0

tk=Tk()
tk.title("AIR HOCKEY GAME")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)


canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
canvas.config(bg="black")
tk.update()

canvas.create_line(250,0,250,400,fill="white",width=3)


class ball:
    def __init__(self,canvas,color,paddle1,paddle2):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,233,168)
        starts=[-3,3]#[-3,-2,-1,0,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3.5
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=500

    def hit_paddle1(self,pos):
        paddle1_pos=self.canvas.coords(self.paddle1.id)
        if pos[1]>=paddle1_pos[1] and pos[1]<=paddle1_pos[3]:
            if pos[0]>=paddle1_pos[0] and pos[0]<=paddle1_pos[2]:
                return True
            return False
        
    def hit_paddle2(self,pos):
        paddle2_pos=self.canvas.coords(self.paddle2.id)
        if pos[1]>=paddle2_pos[1] and pos[1]<=paddle2_pos[3]:
            if pos[2]>=paddle2_pos[0] and pos[2]<=paddle2_pos[2]:
                return True
            return False
        
#canvas.move takes three parameters (1.is the id of the ball-- 2.is the horizontal move position--3.vertical position
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#coords creates an array [x1(0),y1(1),x2(2),y2(3)]
        if pos[1]<=0:
            self.y=3.5
        if pos[3]>=self.canvas_height:
            self.y=-3.5
        if pos[0]<=0:
            self.x=3.5
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-3.5
            self.score(False)
        if self.hit_paddle1(pos)== True:
            self.x=3.5
        if self.hit_paddle2(pos)== True:
            self.x=-3.5

    def score(self,value):
        global counter
        global counter1

        if value==True:
            a= self.canvas.create_text(125,40,text=counter,font=("Arial",30),fill="yellow")
            canvas.itemconfig(a,fill="black")
            counter+=1
            a= self.canvas.create_text(125,40,text=counter,font=("Arial",30),fill="yellow")



        if value==False:
            a= self.canvas.create_text(375,40,text=counter1,font=("Arial",30),fill="yellow")
            canvas.itemconfig(a,fill="black")
            counter1+=1
            a= self.canvas.create_text(375,40,text=counter1,font=("Arial",30),fill="yellow")

    


class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,30,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("W",self.turn_left)
        self.canvas.bind_all("S",self.turn_right)
        self.canvas.bind_all("w",self.turn_left)
        self.canvas.bind_all("s",self.turn_right)
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0
    def turn_left(self,evt):
        self.y=-3
    def turn_right(self,evt):
        self.y=3


class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(470,150,500,250,fill=color)
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Up>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Down>",self.turn_right)


    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=400:
            self.y=0
    def turn_left(self,evt):
        self.y=-3
    def turn_right(self,evt):
        self.y=3
canvas.create_text(125,10,text="__PLAYER 1__",fill="violet",font=("algerian",10))
canvas.create_text(375,10,text="__ PLAYER 2 __",fill="violet",font=("algerian",10))


paddle1=Paddle1(canvas,"sky blue")
paddle2=Paddle2(canvas,"light green")
BALL=ball(canvas,'red',paddle1,paddle2)

while 1:
    BALL.draw()
    paddle1.draw()
    paddle2.draw()

    if counter==10:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="--CONGRATULATIONS PLAYER 2!--",font=("algerian",20),fill="orange")
        canvas.create_text(250,230,text=" you won!!!",font=("algerian",20),fill="orange")
        #canvas.create_text(250,215,text="SCORE:"+str(counter)+"-"+str(counter1),font=("arial",15),fill="red")
    if counter1==10:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="--CONGRATULATIONS PLAYER 1!--",font=("algerian",20),fill="orange")
        canvas.create_text(250,230,text=" you won!!!",font=("algerian",20),fill="orange")
        #canvas.create_text(250,215,text="SCORE:"+str(counter)+"-"+str(counter1),font=("arial",15),fill="red") 

           
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    if counter==10 or counter1==10:
        break

       

