number = int(input("Число?"))
if number %2 == 0:
    print("Четное")
else:
    print("Нечетное")

print("Четное" if number %2 == 0  else "Нечетное")