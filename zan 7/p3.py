'''
from tkinter import *

wind = Tk()

wind.title("Programm 1")
#wind.geometry('250x200')
wind.minsize(500, 500)
wind.resizable(False, False)

#wind['bg'] = 'black'
wind['bg'] = '#FF69B4'
#label хранит текст или картинку
lb1 = Label(wind, text="gfedg", font= 'Arial 15')
lb1.place(x=190, y = 10)

#button
btn1 =Button(wind, width=15, height=2)
btn1.place(x=190, y = 150)

#entry
ent1 = Entry(wind, font="Arial 15", width=15)
ent1.place(x=190, y = 90)

mainloop()
'''