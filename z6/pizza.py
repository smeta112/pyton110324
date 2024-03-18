kol_pizza = int(input("Сколько пицц вы хотите? \n"))
price_pizza = float(input('Сколько стоит пицца? \n'))
summa = kol_pizza * price_pizza
print()
print("Ваш заказ: ", kol_pizza, 'шт. пиццы')
print("По цене", price_pizza, "за одну пиццу")
print("К оплате", summa, "руб.")
tips = float(input('сколько процентов вы хотите оставить официанту "на чай".?\n'))