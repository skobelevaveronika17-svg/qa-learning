number = int(input("Введите число: "))
total = 0
for i in range(1, number + 1):
    total += i

print(f"Сумма чисел от 1 до {number} = {total}")
