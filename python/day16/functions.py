users = [
    {"email": "anna@test.ru", "password": "Anna1234"},
    {"email": "ivan@test.ru", "password": "Ivan123"},
    {"email": "olga@test.ru", "password": "olga12345"},
    {"email": "petr@test.ru", "password": "Petrpetrpetr"},
    {"email": "max@test.ru", "password": "Maxim1234567890123456"},
    {"email": "lena@test.ru", "password": "Lena1234567890123456"},
    {"email": "kate@test.ru", "password": "kate"},
    {"email": "nina@test.ru", "password": ""}
]


def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False


def has_upper(password):
    for ch in password:
        if ch.isupper():
            return True
    return False


def check_password(password):
    if password == "":
        return "Заполните поле"
    if len(password) < 8 or len(password) > 20:
        return "Пароль должен содержать от 8 до 20 символов"
    if not has_digit(password):
        return "Пароль должен содержать хотя бы одну цифру"
    if not has_upper(password):
        return "Пароль должен содержать хотя бы одну заглавную букву"
    return "OK"

for u in users:
    print(f"{u['email']} - {check_password(u['password'])}")
