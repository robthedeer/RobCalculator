from tkinter import*
import math

expression = ""

def press(num):
    global expression
    expression = expression +str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)
def sqrt():
    global expression
    squareroot = str(math.sqrt(float(expression)))
    equation.set(squareroot)

    expression = ""

def to_Power():
    global expression
    n = str(math.power(float(expression)))
    equation.get(n)

    expression = ""



def equal():
    try: 
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except:
        equation.set("Error")
        expression = ""

calc = Tk()
calc.title("CALCULATOR")
calc.configure(background="grey")
calc.geometry("397x195")

equation =StringVar()

exp_field =Entry(calc,textvariable=equation)
exp_field.grid(columnspan=25, ipadx=100,ipady=9)

#Buttons
b1 =Button(calc,text='1',fg='black',bg='green',command=lambda: press(1), height=1, width=7)
b1.grid(row=1,column=0)

b2 =Button(calc,text='2',fg='black',bg='green',command=lambda: press(2), height=1, width=7)
b2.grid(row=1,column=1)

b3 =Button(calc,text='3',fg='black',bg='green',command=lambda: press(3), height=1, width=7)
b3.grid(row=1,column=2)

DEL =Button(calc,text='DEL',fg='black',bg='green',command=clear, height=1, width=7)
DEL.grid(row=1,column=3)

b4 =Button(calc,text='4',fg='black',bg='green',command=lambda: press(4), height=1, width=7)
b4.grid(row=2,column=0)

b5 =Button(calc,text='5',fg='black',bg='green',command=lambda: press(5), height=1, width=7)
b5.grid(row=2,column=1)

b6 =Button(calc,text='6',fg='black',bg='green',command=lambda: press(6), height=1, width=7)
b6.grid(row=2,column=2)

plus =Button(calc,text='+',fg='black',bg='green',command=lambda: press("+"), height=1, width=7)
plus.grid(row=2,column=3)

b7 =Button(calc,text='7',fg='black',bg='green',command=lambda: press(7), height=1, width=7)
b7.grid(row=3,column=0)

b8 =Button(calc,text='8',fg='black',bg='green',command=lambda: press(8), height=1, width=7)
b8.grid(row=3,column=1)

minus =Button(calc,text='-',fg='black',bg='green',command=lambda: press("-"), height=1, width=7)
minus.grid(row=3,column=3)

b9 =Button(calc,text='9',fg='black',bg='green',command=lambda: press(9), height=1, width=7)
b9.grid(row=3,column=2)

b0 =Button(calc,text='0',fg='black',bg='green',command=lambda: press(0), height=1, width=7)
b0.grid(row=4,column=0)

dot =Button(calc,text='.',fg='black',bg='green',command=lambda: press("."), height=1, width=7)
dot.grid(row=4,column=1)

multiply =Button(calc,text='x',fg='black',bg='green',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4,column=2)

divide =Button(calc,text='/',fg='black',bg='green',command=lambda: press("/"), height=1, width=7)
divide.grid(row=4,column=3)

sqrt=Button(calc,text='⎷',fg='black',bg='green',command=sqrt, height=1, width=7)
sqrt.grid(row=5,column=0)

power =Button(calc,text='^',fg='black',bg='green',command=to_Power,height=1, width = 7)
power.grid(row=5,column=1)

equal =Button(calc,text='=',fg='black',bg='green',command=equal, height=1, width=7)
equal.grid(row=5,column=3)


calc.mainloop()

 



