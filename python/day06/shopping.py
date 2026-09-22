quantity = 0
total_price = 0
max_price = 0
discount_percent = 0
new_price = 0
while True:
    order = input("Введите цену товара или стоп:")
    if order == 'стоп':
        break
    total_price += float(order)
    quantity = quantity + 1
    if float(order) > max_price:
        max_price = float(order)

    if total_price >= 10000:
        discount_percent = 15
    elif total_price >= 5000:
        discount_percent = 10
    elif total_price >= 1000:
        discount_percent = 5
    new_price = total_price - (discount_percent / 100 * total_price)
if quantity == 0:
    print("Корзина пуста")
else:
    print(f"Товаров: {quantity}")
    print(f"Сумма: {total_price}")
    print(f"Самый дорогой товар: {max_price}")
    print(f"Скидка: {discount_percent}")
    print(f"К оплате: {new_price}")

