price = float(input("Цена товара"))
discount = float(input("Какая скидка?"))
saved = price * discount / 100
new_price = price - saved
print(f"Цена товара со скидкой - {new_price} $. Сэкономлено - {saved} $")
