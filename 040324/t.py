#0 1 1 2 3 5 8 13 21....
#Вывести кол-во эл послед-ти: 10
#1
n = int(input('Введите количество элементов посл-ти: '))
firstnum = 0
secondnum = 1
sum = 0
f = firstnum
s = secondnum
for i in range(n):
    print(s)
    sum = f + s
    f = s
    s = sum
#2
n = int(input('Введите количество элементов посл-ти: '))
firstnum, secondnum = 0,1
f = firstnum
s = secondnum
for i in range(n):
    print(f)
    f, s = s, f+s
    #firstnum,secondnum = secondnum, firstnum + secondnum


