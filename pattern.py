# Вот три основные команды:

import turtle           # импортируем модуль turtle
window = turtle.Screen()# вызовем функцию  Screen() из модуля turtle,
                        # и она автоматически создаст холст. 
t = turtle.Pen()# ввести инструкцию с функцией  Pen(),
                # заставляющую черепашку рисовать по холсту
                # как бы ручкой (пером) (pen – по-англ. ручка)


# импортируем модуль time - это я сделала для того,
# чтобы использовать секунды для замедления рисования,
# и вы смогли рассмотреть, что происходит,
# вам его импортировать не нужно
import time 
# изначально черепашка находится в центре экран и стрелка повернута вправо               
time.sleep(2) # здесь я включила паузу на 2 сек,
              # чтобы вы смогли посмотреть, что происходит
              # вам это не нужно писать в коде
t.forward(200)# черепашка двигается вперед на 200 пикселей
              # по направлению стрелки 
time.sleep(1) # здесь я опять включила паузу на 1 сек,
               # чтобы вы смогли посмотреть, что происходит
t.left(90)     # стрелка поворачивается влево на 90 градусов
time.sleep(1)  # снова пауза 1 сек
t.penup()      # поднимаем перо вверх
time.sleep(1)  # пауза 1 сек
t.forward(50)  # перемещаем поднятую перо на 50 пикселей вперед
time.sleep(1)  # пауза 1 сек
t.right(90)    # стрелка поворачивается вправо на 90 градусов
t.pendown()    # опускаем перо на холст
time.sleep(1)  # пауза 1 сек
t.backward(300)# перемещаем стрелку назад на 300 пикселей
time.sleep(1)  # пауза 1 сек
t.pensize(5)   # толщина пера стала 5 пикселей
t.left (45)    # стрелка поворачивается влево на 45 градусов
time.sleep(1)  # пауза 1 сек
t.forward(150) # перемещаем поднятую перо на 150 пикселей вперед
time.sleep(1)  # пауза 1 сек
t.reset()      # сброс программы в исходное состояние
