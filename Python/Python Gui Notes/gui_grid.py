from tkinter import *
root = Tk()
sagar = Label(root, text = "username")
chanti = Label(root, text = "password")
entry_1 = Entry(root) #The Tkinter Entry Widget. The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
entry_2 = Entry(root)

sagar.grid(row = 0) #simillar to the pack
chanti.grid(row =1)

entry_1.grid(row =0,column =1)
entry_2.grid(row =1, column =1)
check = Checkbutton(root, text = "always") #widget that shows keepme logged button
check.grid(columnspan =2)
root.mainloop()