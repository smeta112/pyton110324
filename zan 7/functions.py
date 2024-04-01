'''
cntr + shift + f10 - воспрроизведение
'''

def hi(name):
    print(f'Прив,{name}, как жизнь?')

def sum(a,b):
    print(a+b)
'''
def converter(km):
    return km*1000
km = int(input("Введите км: "))
print(f"это- ", converter(km), "в метрах")'''
def math(a):
    return a*2
print(math(5))

d = lambda a: a*2
print(d(5))
num = [1,2,3,4,5,6,7,8,9]
sq_num = map (lambda x:x**2, num) #позволяет для каждого эл 1 раз
print(list(sq_num))


hi("Villiam")
hi("Olga")
sum(2,2)
