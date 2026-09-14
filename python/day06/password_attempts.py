password : str = str(123456)

attempt : int = 3
while attempt > 0:
    password_user  = input("Введите пароль: ")
    if password_user  == password:
        print("Добро пожаловать!")
        break
    else:
        attempt -= 1
        print(f"Неверный пароль.Осталось попыток {attempt}")
else:
    print ("Аккаунт заблокирован.")