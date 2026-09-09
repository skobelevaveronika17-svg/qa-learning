check = float(input("Сумма счета"))
tips = float(input("сколько чаевых?"))
tips_amount = check * tips / 100
total = check + tips_amount
print(f"Сумма счета {total} $ из них чаевые {tips_amount} $ ")