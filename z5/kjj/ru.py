from tkinter import *

wind = Tk() #создание окна
wind.title("program 1") #заголовок окна

wind.minsize(500,550) #мин размер
wind.resizable(False, False) #1 шир, 2 выс
wind["bg"]='black'#bg - фон fg- текст

lb1 = Label(wind, text = "hello world!", font='Arial 30', bg='white', fg='black')
lb1.place(x=150, y=220) #надпись

btn1 = Button(wind, text='click me!', font='Arial 10', bg='red', fg='white', width=20,height=3) #кнопка
btn1.place(x=80, y=120)


mainloop() #всегда в конце, для зацикливания # обработчик событий
#pass #пропуск