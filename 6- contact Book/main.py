from tkinter import *
from functions import *


def search():
    global s
    n = e1.get()
    p = e2.get()
    res = cherchre(n, p)
    if res == -1:
        k = 'Not found !!!'
        s.config(text=k)
        s.pack()
    else:
        txt = write(res)
        s.config(text=txt)
        s.pack()


def add():
    n, p = e1.get(), e2.get()
    txt = add2db(n, p)
    s.config(text=txt)
    s.pack()


root = Tk()
root.geometry('300x200')
root.title('Contact book')

Label(root, text='serch for a name or phone number :').pack()

frame = Frame(root)
Label(root, text='').pack()

name = Label(frame, text='Contact Name :')
nmbrPhone = Label(frame, text='Phone Number :')

e1 = Entry(frame)
e2 = Entry(frame)

name.grid(row=0, column=0)
e1.grid(row=0, column=1)

nmbrPhone.grid(row=1, column=0)
e2.grid(row=1, column=1)

frame.pack()
Label(root, text='').pack()
BTNframe = Frame(root)
Button(BTNframe, text='Search', command=search).grid(row=0, column=0)
Button(BTNframe, text='add', command=add).grid(row=0, column=1)
BTNframe.pack()
s = Label(root, text='')
s.pack()
Button(root, text='Quit', command=root.quit).pack()

root.mainloop()
