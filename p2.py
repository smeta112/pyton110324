a=int(input("Введте начало диапазона: "))
b=int(input("Введте конец диапазона: "))

print("1.Все числа диапазона:")
for i in range(a,b+1):
    print(i)
print("2.Числа диапозона в убывающем порядке:")
for n in range(-b,-(a - 1)):
    print(-n)

print("3.Числа кратные 7:")
for i in range(a,b+1):
    if i % 7 == 0:
        print(i)

print("4.Чисел кратно 5:")
count = 0
for i in range(a,b+1):
    if i % 5 == 0:
        count += 1
print(count)
