name = input("Имя пользователя")
letters = len(name)
if name == "":
    print(" Имя некорректно. Имя не введено.")
elif letters < 3:
    print("Имя некорректно. Введено меньше трех символов")
elif letters > 20:
    print("Имя некорректно. Введено более 20 символов")
else:
    print("Имя корректно")

