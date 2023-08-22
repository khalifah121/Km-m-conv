from tkinter import *


def request():
    gotten=float(input.get())
    num2=gotten*1000
    output.delete(1.0,"end")
    output.insert(1.0,num2)
    

scr=Tk()

scr.title("My converter")
scr.geometry("350x300")
scr.resizable(False,False)
scr.config(bg="",padx=20,pady=30)

frame2=Frame(scr,background="green",width=200,height=200,padx=50,pady=30)
frame2.place(x=0,y=0)

input=Entry(frame2,width=20,bd=0,font=("Arial",10,"bold"))
input.grid(row=0,column=3,pady=20)

label1=Label(frame2,text="KM",fg="red",font=("Arial",10,"bold"),padx=10)
label1.grid(row=0,column=4,padx=10)

output=Text(frame2,width=20,height=1,bd=0,font=("Arial",10,"bold"))
output.grid(row=1,column=3,padx=5,pady=15)

label2=Label(frame2,text="M",fg="red",font=("Arial",10,"bold"),padx=10)
label2.grid(row=1,column=4)

btn=Button(frame2,text="Convert",fg="white",bd=0,padx=10,font=("Arial",10,"bold"),bg="#A70D2A",command=request)
btn.grid(row=2,column=3)

scr.mainloop()