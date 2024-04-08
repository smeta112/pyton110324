from tkinter import *

wind = Tk()
wind.title("Calculator")
wind.minsize(340, 400)
wind.resizable(False, False)
wind['bg'] = 'grey'



ent = Entry(wind, width=30, borderwidth=5, bg="black", fg = 'white')
ent.grid(row=0, column=0, columnspan=4)

#КНОПКИ
buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '/', '*', '=', 'Clear']

row = 1
col = 0
for button in buttons:
    if col == 3:
        col = 0
        row += 1

    btn = Button(wind, text=button, padx=40, pady = 20, command= lambda button=button: button_click_handler(button))
    btn.grid(row=row, column=col)
    col += 1

def button_click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(END, current + str(number))

def button_clear():
    ent.delete(0, END)


def button_equal():
    result = eval(ent.get())
    ent.delete(0, END)
    ent.insert(END, result)

def button_click_handler(button):
    if button == "=":
        button_equal()
    elif button == "Clear":
        button_clear()
    else:
        button_click(button)

#for r in range(3):
 #   for c in range(3):

mainloop()


#font= 'Arial 15',
