from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.minsize(340, 400)
wind.resizable(False, False)
wind['bg'] = 'grey'

buttons_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '+', 'C', '0', '=', '-' ]


label = Label(wind, font= 'Arial 15', bg="black", fg = 'white')
label.grid(row=0, column=0, columnspan=4)

for r in range(3):
    for c in range(3):

mainloop()



