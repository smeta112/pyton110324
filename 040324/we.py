from tkinter import *

root = Tk() #создание окна пишется название с большой буквы
root.title('PROGRAMM 1')
root.minsize(500,500)
root.maxsize(700,700)
root.resizable(False, False)
#OR (True, False),(True,True)
root["bg"]='#BA55D3'

Label_1 = Label(root, text="HIII World", font='Arial 15', fg='white', bg='black')
Label_1.place(x=250,y=250)

btn1 = Button(root, text="click me!",
              width=10,height=3)
btn1.place(x=250,y=250)

entr1 = Entry(root, font ='Arial 10', width=20)
entr1.place(x=250,y=250)
mainloop()