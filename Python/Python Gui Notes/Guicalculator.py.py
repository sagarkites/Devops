from tkinter import*
#Functions
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def btnCLEARdisplay():
    global operator
    operator = ""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
root = Tk()
root.title("ScottCalculator", )
root.geometry("200x250+30+30")
operator = ""
text_Input = StringVar()
#Frame-1
top = Frame(root, width = 200, height = 70, bd = 6,relief ='raised',bg = 'silver')
top.pack(side = TOP)
#Frame-2
bottom = Frame(root, width = 254, height = 300, bd = 6,relief ='raised',bg = 'silver')
bottom.pack(side = BOTTOM)
# display in top
display = Entry(top, font = ('arial', 16, 'bold'),textvariable =text_Input, width = 14, bd = 2, justify = 'right')
display.grid(row =0, column =0)
#buttons
bt7 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='7',command = lambda:btnclick(7)).grid(row =0, column =0)
bt6 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='6',command = lambda:btnclick(6)).grid(row =0, column =1)
bt5 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='5',command = lambda:btnclick(5)).grid(row =0, column =2)
bt4 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='4',command = lambda:btnclick(4)).grid(row =1, column =0)
bt3 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='3',command = lambda:btnclick(3)).grid(row =1, column =1)
bt2 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='2',command = lambda:btnclick(2)).grid(row =1, column =2)
bt1 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='1',command = lambda:btnclick(1)).grid(row =2, column =0)
bt0 = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='0',command = lambda:btnclick(0)).grid(row =2, column =1)
btcl = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='CL',command = btnCLEARdisplay).grid(row =2, column =2)
btplus  = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='+',command = lambda:btnclick("+")).grid(row =3, column =0)
btsub  = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='-',command = lambda:btnclick("-")).grid(row =3, column =1)
btmul  = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='*',command = lambda:btnclick("*")).grid(row =3, column =2)
btdiv  = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='/',command = lambda:btnclick("/")).grid(row =4, column =0)
bteql  = Button(bottom, padx = 16, pady =2, bd=2, fg = 'black', font = ('arial', 16, 'bold'),width = 1, height = 1, text ='=',command =  btnEqualsInput).grid(row =4, column =1)
root.mainloop()