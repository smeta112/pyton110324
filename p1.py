a=int(input("Введте начало диапазона: "))
b=int(input("Введте конец диапазона: "))

for i in range(a,b+1):
  if i % 7 == 0:
    print(i)