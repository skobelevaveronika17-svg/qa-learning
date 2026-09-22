order = int(input("Какая сумма заказа?"))
discount_percent = 0

if order >= 10000:
    discount_percent = 15
elif order >= 5000:
    discount_percent = 10
elif order >= 1000:
    discount_percent = 5
new_price = order - (discount_percent / 100 * order)



print(f"Скидка {discount_percent} % ,{discount_percent / 100 * order} $, итоговая сумма = {new_price}$ ")