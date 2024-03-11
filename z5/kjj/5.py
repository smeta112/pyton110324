from tkinter import *

def hello():
    lb1["text"] = 'jklj' #надпись меняется



wind = Tk() #создание окна
wind.title("program 1") #заголовок окна

wind.minsize(400,550) #мин размер
wind.resizable(False, False) #1 шир, 2 выс
wind["bg"]='black'#bg - фон fg- текст

lb1 = Label(wind, text = "hello world!", font='Arial 30', bg='white', fg='black')
lb1.place(x=50, y=50) #надпись

btn1 = Button(wind, text='click me!', font='Arial 10', bg='red', fg='white', width=20,height=3, command=hello) #кнопка
btn1.place(x=50, y=120)

ent1 = Entry(wind, bg='green', fg='white', font='Arial 10', width=15)  #поле для ввода(нельзя height)
ent1.place(x=50, y=200)

mainloop() #всегда в конце, для зацикливания # обработчик событий



def summ(player_choice):
    return x+y

print(summ(2, 5))