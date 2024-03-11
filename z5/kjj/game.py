from tkinter import *
from random import *

def game(player_choice):
    lis1=["stone", "scissors", "paper"]
    comp_choise = lis1[randint(0, len(lis1)-1)]
    if comp_choise == player_choice:
        lb_none['text']= f"Draw! Компьютер выбрал-{comp_choise}, Ваш выбор-{player_choice}"


wind = Tk()
wind.title("Game")

wind.minsize(600,650)
wind.resizable(False, False)
wind["bg"]='white'

lb1 = Label(wind, text = " ", font='Arial 20', bg='white', fg='black')
lb1.place(x=30, y=350)

lb2 = Label(wind, text = "COMPUTER", font='Arial 26', bg='white', fg='black')
lb2.place(x=30, y=10)
lb3 = Label(wind, text = "VS", font='Arial 26', bg='white', fg='black')
lb3.place(x=310, y=10)
lb4 = Label(wind, text = "YOU", font='Arial 26', bg='white', fg='black')
lb4.place(x=450, y=10)

lb5 = Label(wind, text = "Lose:", font='Arial 20', bg='white', fg='black')
lb5.place(x=30, y=100)
lb6 = Label(wind, text = "Win:", font='Arial 20', bg='white', fg='black')
lb6.place(x=30, y=150)
lb7 = Label(wind, text = "Drow:", font='Arial 20', bg='white', fg='black')
lb7.place(x=30, y=200)

btn1 = Button(wind, text='stone', font='Arial 15', bg='grey', fg='black', width=9,height=1, command=game("stone"))
btn1.place(x=430, y=100)
btn2 = Button(wind, text='paper', font='Arial 15', bg='grey', fg='black', width=9,height=1)
btn2.place(x=430, y=150)
btn3 = Button(wind, text='scissors', font='Arial 15', bg='grey', fg='black', width=9,height=1)
btn3.place(x=430, y=200)

btn4 = Button(wind, text='New game', font='Arial 25', bg='blue', fg='yellow', width=11,height=2)
btn4.place(x=30, y=500)



mainloop()