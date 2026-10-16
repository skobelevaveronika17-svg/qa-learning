import json


def make_email(name, domain="test.ru"):
    return f"{name}@{domain}"


def make_user(name, password, expected):
    return {"email": make_email(name), "password": password, "expected": expected}


def make_password(length: int, has_digit=True, has_upper=True):
    if length == 0:
        return ""


    need = int(has_upper) + int(has_digit)
    if length < need:
        return None
    if length == 1:
        if  has_upper:
            return "A"
        if has_digit:
            return "1"
        return "a"

    first = "A" if has_upper else "a"
    last = "1" if has_digit else "a"
    average = "a" * (length - 2)
    return f"{first}{average}{last}"


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

def generate_users():
    return [
    {"email": make_email("valid"), "password": make_password(12), "expected": "OK"},
    {"email": make_email("short"), "password":  make_password(7), "expected": "Пароль должен содержать от 8 до 20 символов"},
    {"email": make_email("long"), "password":  make_password(21),
     "expected": "Пароль должен содержать от 8 до 20 символов"},
    {"email": make_email("nodigit"), "password":  make_password(10, has_digit=False), "expected": "Пароль должен содержать хотя бы одну цифру"},
    {"email": make_email("noupper"), "password":  make_password(10, has_upper=False),
     "expected": "Пароль должен содержать хотя бы одну заглавную букву"},
    {"email": make_email("empty"), "password": make_password(0), "expected": "Заполните поле"},
    {"email": make_email("min8"), "password": make_password(8), "expected": "OK"},
    {"email": make_email("max20"), "password": make_password(20), "expected": "OK"}
]
users = generate_users()
u = make_user("valid", "Anna1234", "OK")
print(u)

print(make_password(8) == "Aaaaaaa1")
print(make_password(0) == "")
print(make_password(1) is None)
print(make_password(2) == "A1")
print(make_password(1, has_digit=False) == "A")
print(make_password(1, has_upper=False) == "1")
print(make_password(1, has_digit=False, has_upper=False) == "a")
print(make_password(-1) is None)
print(make_password(-1, has_digit=False, has_upper=False) is None)
print(len(make_password(20)) == 20)
with open('test_users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

with open("test_users.json", encoding="utf-8") as f:
    loaded = json.load(f)
summary = {}
for u in loaded:
    status = "PASSED"

    if check_password(u['password']) == u['expected']:
        print(f"{u['email']} - PASSED")
    else:
        status = "FAILED"
        print(f"{u['email']} - FAILED: {check_password(u['password'])}")
    if status in summary:
        summary[status] = 1 + summary[status]
    else:
        summary[status] = 1
print (f"Итого: {summary}")

