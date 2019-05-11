from distutils.log import  warn as printf
from tkinter import Button,Label,Tk,mainloop
import this
a = lambda :label.config(font='Helvetica -40 bold')
top = Tk('XXX')
label = Label(top, text='a')
button = Button(top, text = '单击', command = a)
button.pack()
label.pack()
mainloop()
button.pack
