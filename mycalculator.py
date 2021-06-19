from tkinter import *
screen=Tk()
screen.title("my calculator")
screen.geometry("361x490")
screen.maxsize(361,490)
screen.minsize(361,490)

def clear():
    global operator
    operator = " "
    tex.set(operator)

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def ans():
    global operator
    result = eval(operator)
    operator=str(result)
    tex.set(operator)

tex= StringVar()
operator=" "

entry=Entry(screen,bg="gold",font=("arial",20,"italic bold"),bd="30",justify="right",textvariable=tex)
entry.grid(row=0,columnspan=4)

btn7=Button(screen,text="7",font=("arial",20,"italic bold"),bd="10",padx=16 ,pady=16,command=lambda:click(7),
            activebackground="lime",activeforeground="white")
btn7.grid(row=1,column=0)

btn8=Button(screen,text="8",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(8)
            ,activebackground="lime",activeforeground="white")
btn8.grid(row=1,column=1)

btn9=Button(screen,text="9",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(9)
            ,activebackground="lime",activeforeground="white")
btn9.grid(row=1,column=2)

btnadd=Button(screen,text="+",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click("+")
              ,activebackground="Turquoise",activeforeground="white")
btnadd.grid(row=1,column=3)

btn4=Button(screen,text="4",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(4)
            ,activebackground="lime",activeforeground="white")
btn4.grid(row=2,column=0)

btn5=Button(screen,text="5",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(5)
            ,activebackground="lime",activeforeground="white")
btn5.grid(row=2,column=1)

btn6=Button(screen,text="6",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(6)
            ,activebackground="lime",activeforeground="white")
btn6.grid(row=2,column=2)

btnmul=Button(screen,text="x",font=("arial",20,"bold"),bd="10",padx=16,pady=16,command=lambda:click("*")
              ,activebackground="Turquoise",activeforeground="white")
btnmul.grid(row=2,column=3)

btn1=Button(screen,text="1",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(1)
            ,activebackground="lime",activeforeground="white")
btn1.grid(row=3,column=0)

btn2=Button(screen,text="2",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(2)
            ,activebackground="lime",activeforeground="white")
btn2.grid(row=3,column=1)

btn3=Button(screen,text="3",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(3)
            ,activebackground="lime",activeforeground="white")
btn3.grid(row=3,column=2)

btnsub=Button(screen,text="-",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click("-")
              ,activebackground="Turquoise",activeforeground="white")
btnsub.grid(row=3,column=3)

btn0=Button(screen,text="0",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click(0)
            ,activebackground="lime",activeforeground="white")
btn0.grid(row=4,column=0)

btnclear=Button(screen,text="C",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=clear
                ,activebackground="Turquoise",activeforeground="white")
btnclear.grid(row=4,column=1)

btnans=Button(screen,text="=",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=ans
              ,activebackground="Red",activeforeground="white")
btnans.grid(row=4,column=2)

btndiv=Button(screen,text="/",font=("arial",20,"italic bold"),bd="10",padx=16,pady=16,command=lambda:click("/")
              ,activebackground="Turquoise",activeforeground="white")
btndiv.grid(row=4,column=3)


screen.mainloop()
