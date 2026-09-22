password = "Anna1234"

count = 5
while count > 0:
    password_user = input("Введите пароль: ")
    if password_user == password:
        print("Вход выполнен")
        break
    else:
        count = count - 1
        if count > 0:
           print(f"Неверный пароль. Осталось попыток: {count}")
else:
    print("Вход заблокирован на 15 минут")

