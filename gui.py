from tkinter import *

gui = Tk()
gui.title('LOGIN PAGE')
gui.geometry("500x400")
gui.configure(bg='blue')


l1= Label(gui, text='ENTER YOUR FIRST NAME')
l1.grid(column= 0, row = 0, padx=20)

l2 = Label(gui, text='ENTER YOUR SECOND NAME')
l2.grid(column=0, row=1)

l3 = Label(gui, text='ENTER YOUR SURNAME')
l3.grid(column=0, row=2)


gui.mainloop()






