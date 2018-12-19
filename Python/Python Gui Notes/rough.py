#This program was to create a dropdown menu
from tkinter import *
#functions for buttons
def something():
    print("everything is good")
def open():
    print("unable to open file")
def project():
    print("opens certain file")
def quit():
    print("exit")
def edit():
    print("edit certain files")
def text():
    print("edit the text size")
def color():
    print("change the color")
def font():
    print("incregese or decrease the font size")
root = Tk()
menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu) #to create 1st label
menu.add_cascade(label = 'Open',menu = submenu)
submenu.add_command(label = 'file', command =open)
submenu.add_command(label = 'project', command =project)
submenu.add_separator() #To create a next label button
submenu.add_command(label = 'Exit', command = 'quit')
editMenu = Menu(menu) #To create 2nd labele
menu.add_cascade(label = 'Configure', menu = editMenu )
editMenu.add_command(label ='text', command =text) #To create sub-button
editMenu.add_command(label ='color',command = color)
editMenu.add_command(label ='font', command = font)
# Inserting toolbar
toolbar = Frame(root, bg = 'white')
insert = Button(toolbar, text = 'paste url',fg ='orange', command = something)
insert.pack(side = LEFT, padx = 2, pady =2)
insert1 = Button(toolbar, text = 'download', fg = 'green', command = something)
insert1.pack(side = LEFT, padx =2, pady=2)
toolbar.pack(side = TOP, fill = X)
#status bar
status = Label(root, text = "info about the application...", bd = 1,relief =SUNKEN, anchor= W)
status.pack(side = BOTTOM, fill=X)
root.mainloop()
