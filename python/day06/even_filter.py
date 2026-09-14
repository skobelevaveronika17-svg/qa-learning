number = int(input("Введите число: "))
count = 0
for i in range(1, number + 1):

    if i % 2 == 1:
        continue
    print(i)
    count = count + 1
print (f"Всего четных: {count}")