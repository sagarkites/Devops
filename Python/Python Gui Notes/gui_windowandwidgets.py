from tkinter import *
root = Tk()
sagar = Frame(root)
sagar.pack()
chanti = Frame(root)
chanti.pack(side = BOTTOM)
button1 = Button(sagar, text = 'open', foreground='purple') #to create buttons use Buttons fg color of button
button1.pack(side = RIGHT) # where location of buttons
button2 = Button(sagar, text ='edit', fg='black')
button2.pack(side = LEFT)
root.mainloop()

