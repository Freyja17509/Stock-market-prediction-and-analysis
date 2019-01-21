from tkinter import *
import tkinter.messagebox

def doNothing():
    print("Yes")

window = Tk()

#*********Photo***************
photo = PhotoImage(file="learn how to treat.png")
label = Label(window, image=photo)
label.pack(fill=BOTH, expand=True)

# ********MAIN MENU***************
menu = Menu(window)
window.config(menu=menu)


subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project..", command= doNothing())
subMenu.add_command(label="New..", command= doNothing())
subMenu.add_command(label="Open", command= doNothing())
subMenu.add_command(label="Save", command= doNothing())
subMenu.add_command(label="Save As..", command= doNothing())
subMenu.add_separator()
subMenu.add_command(label="Exit", command= doNothing())



editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command= doNothing())

exchange_menu = Menu(menu)
menu.add_cascade(label="Exchange",menu=exchange_menu)


interval_menu = Menu(menu)
menu.add_cascade(label="OLHC Interval",menu=interval_menu)
interval_menu.add_command(label="Tick", command= doNothing())
interval_menu.add_command(label="1 minute", command= doNothing())
interval_menu.add_command(label="5 minutes", command= doNothing())
interval_menu.add_command(label="15 minutes", command= doNothing())
interval_menu.add_command(label="30 minute", command= doNothing())
interval_menu.add_command(label="1 hour", command= doNothing())
interval_menu.add_command(label="5 hours", command= doNothing())


pause_resume_menu = Menu(menu)
menu.add_cascade(label="Pause/Resume",menu=pause_resume_menu)


help_menu = Menu(menu)
menu.add_cascade(label="Help",menu=help_menu)


#******************Tool Bar******************
toolbar = Frame(window, bg="blue")

insertButt = Button(toolbar, text="insert image", command= doNothing())
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt =  Button(toolbar, text="Print", command= doNothing())
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#**************Status Bar******************

status = Label(window,text="Preparing to do nothing", bd=1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


window.title("Stock Market Analysis and Prediction")


topFrame = Frame(window)
topFrame.pack()
bottomFrame =Frame(window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text='Button 1',fg="BLUE")
button2 = Button(topFrame, text='Button 2',fg="RED")
button3 = Button(bottomFrame, text='Button 3',fg="GREEN")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)


answer=tkinter.messagebox.askquestion("q1","Do you like me??")
if answer == "yes":
    tkinter.messagebox.showinfo("Window Title", "I like you too")
else:
    tkinter.messagebox.showinfo("Window Title", "FUCK OFF")

window.mainloop()