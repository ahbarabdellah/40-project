from tkinter import *
from random import *
from PIL import ImageTk, Image

root = Tk()

a = Label(root, text='Do you want to play monopoly!!!  \n and you don\'t find your dice \n this is a soloution for all your pain try it now !!! ')
a.pack()


def change_pic():
    imgs = [
        ImageTk.PhotoImage(Image.open('img/1.png')),
        ImageTk.PhotoImage(Image.open('img/2.png')),
        ImageTk.PhotoImage(Image.open('img/3.png')),
        ImageTk.PhotoImage(Image.open('img/4.png')),
        ImageTk.PhotoImage(Image.open('img/5.png')),
        ImageTk.PhotoImage(Image.open('img/6.png'))]
    root.x = choice(imgs)

    vlabel.configure(image=root.x)


photo = 'img/1.png'
root.photo = ImageTk.PhotoImage(Image.open(photo))
b2 = Button(root, text="try", command=change_pic)
b2.pack()
vlabel = Label(root, image=root.photo)

vlabel.pack()
root.geometry('400x400')
root.title('Roll Dice')

root.mainloop()
