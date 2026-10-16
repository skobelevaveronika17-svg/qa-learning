def check_length(password):
    length = len(password)
    return 8 <= length <= 20


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


def check_password(password, email):
    if password == "":
        return "Заполните поле"
    if not check_length(password):
        return "Пароль должен содержать от 8 до 20 символов"
    if not has_digit(password):
        return "Пароль должен содержать хотя бы одну цифру"
    if not has_upper(password):
        return "Пароль должен содержать хотя бы одну заглавную букву"
    return "OK"


def is_blocked(attempts, limit=4):
    return attempts > limit


def add_attempt(attempts=0):
    attempts = attempts + 1
    return attempts


password = "Anna1234"
email = "anna@test.ru"

attempts = 0 # нигде не используется
print(has_upper("Anna1234"))  # ожидаем True
print(check_length("Anna1234"))  # ожидаем True
print(has_digit("Anna1234"))  # ожидаем True
print(check_password("anna@test.ru", "Anna1234"))  # ожидаем ошибку, перепутаны данные
print(is_blocked(4))  # ожидаем False: блокирует пятая попытка (3.8)
print(check_password("Anna1234", "anna@test.ru")) # ожидаем увидеть OK
print(add_attempt())  # ожидаем 1
