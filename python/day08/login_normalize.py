saved = "anna@mail.ru"
mail = input("Введите ваш email: ")
normalized = mail.strip().lower()

if normalized == "":
    print("Поле не может быть пустым")
elif normalized == saved:
    print("Вход выполнен")
else:
    print("Неверный логин или пароль")
