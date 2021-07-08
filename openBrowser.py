import webbrowser
from tkinter import *

from prompt_toolkit.widgets import Button

root = Tk( 'Abrir o CV do Faslala')
root.title('Abrir Browser')
root.geometry('300x200')


def faslala():
    webbrowser.open('www.faslala.com')

mypage = Button(root)
root.mainloop()
