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

def check_email(email):
    if email.strip() == "":
        return "Заполните поле"
    if email.count("@") != 1:
        return "Неверный формат email"
    if " " in email:
        return "Неверный формат email"
    domain = email[email.index("@") + 1:]
    if domain == "" or "." not in domain:
        return "Неверный формат email"
    return "OK"

if __name__ == "__main__":
    print(check_password("Anna1234") == "OK")
    print(check_email("annna@gmail.com") == "OK")

