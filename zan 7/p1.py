from tkinter import *

wind = Tk()

wind.title("Programm 1")
#wind.geometry('250x200')
wind.minsize(200, 200)
wind.resizable(False, False)

#wind['bg'] = 'black'
wind['bg'] = '#FF69B4'

for c in range(3): wind.columnconfigure(index=c, weight=1)#если одна строчка
for r in range(3): wind.rowconfigure(index=r, weight=1)


'''grid() - column(номер столбца, отсчет начинается с нуля,
row(номер строки, отсчет начинается с нуля, columnspan(объединение нескольких ячеек в одну, 
rowspan(сколько строк должен занимать элемент, 
ipadx/ipady(отступ в кнопке), padx/pady(отступ за кнопкой), 
sticky(north, e , s, w, ne, nw...)#(выравнит элемент в ячейке)
#f' - форматирование'''

for r in range(3):
    for c in range(3):
        btn = Button(wind, text=f'Ячейка:({r},{c})')
        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4,pady=4)
mainloop()