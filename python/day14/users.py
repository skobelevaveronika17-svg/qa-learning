users = [
    {"email": "anna@test.ru", "password": "Anna1234"},
    {"email": "ivan@test.ru", "password": "Ivan123"},
    {"email": "olga@test.ru", "password": "olga12345"},
    {"email": "petr@test.ru", "password": "Petrpetrpetr"},
    {"email": "max@test.ru",  "password": "Maxim1234567890123456"},
    {"email": "lena@test.ru", "password": "Lena1234567890123456"},
    {"email": "kate@test.ru", "password": "kate"},
    {"email": "nina@test.ru", "password": ""},
]
for u in users:
    errors = []
    password = u["password"]
    has_digit = False
    has_upper = False
    for character in password:
            if character.isdigit():
                has_digit = True
            if character.isupper():
                has_upper = True

    if password == "":
        message = "Заполните поле"
    elif len(password) < 8 or len(password) > 20:
        message = "Пароль должен содержать от 8 до 20 символов"
    elif not has_digit:
        message = "Пароль должен содержать хотя бы одну цифру"
    elif not  has_upper:
        message = "Пароль должен содержать хотя бы одну заглавную букву"
    else:
        message = "OK"
    print(f"{u['email']} — {message}")