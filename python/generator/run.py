import json
from data import make_email, make_password, make_bad_email
from checks import check_password, check_email

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
    print(f"Итого: {summary}")