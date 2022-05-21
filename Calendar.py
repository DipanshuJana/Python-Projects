import calendar
from tkinter import *
from datetime import date

def Calendar():
    year = date.today()
    text = calendar.calendar(year.year)
    root = Tk()
    root.geometry("500x600")
    root.resizable(0, 0)
    root.title("CALENDER")
    Label1 = Label(root, text= 'CALENDER', bg= 'dark gray', font=('comicsansms', 20,))
    Label1.grid(row=1, column=1)
    root.config(background='white') 
    l1 = Label(root, text=text, font=('comicsansms', 10))
    l1.grid(row=2, column=1, padx=20)

    root.mainloop() 

Calendar()