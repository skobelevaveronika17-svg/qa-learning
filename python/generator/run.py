import json
from data import make_email, make_password, make_bad_email
from checks import check_password, check_email
from config import BASE, load_settings

settings = load_settings(BASE / "settings.txt")
domain = settings["domain"]
min_len = int(settings["min_length"])
max_len = int(settings["max_length"])


def generate_users():
    return [
        {"email": make_email("valid", domain), "password": make_password(12), "expected": "OK"},
        {"email": make_email("short", domain), "password": make_password(min_len - 1),
         "expected": "Пароль должен содержать от 8 до 20 символов"},
        {"email": make_email("long", domain), "password": make_password(max_len + 1),
         "expected": "Пароль должен содержать от 8 до 20 символов"},
        {"email": make_email("nodigit", domain), "password": make_password(10, has_digit=False),
         "expected": "Пароль должен содержать хотя бы одну цифру"},
        {"email": make_email("noupper", domain), "password": make_password(10, has_upper=False),
         "expected": "Пароль должен содержать хотя бы одну заглавную букву"},
        {"email": make_email("empty", domain), "password": make_password(0), "expected": "Заполните поле"},
        {"email": make_email("min8", domain), "password": make_password(min_len), "expected": "OK"},
        {"email": make_email("max20", domain), "password": make_password(max_len), "expected": "OK"}
    ]


users = generate_users()
with open(BASE / "test_users.json", 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

with open(BASE / "test_users.json", encoding="utf-8") as f:
    loaded = json.load(f)

summary = {}
lines = []
for u in loaded:
    status = "PASSED"
    output = ""
    if check_password(u['password']) == u['expected']:
        output = f"{u['email']} - PASSED"

    else:
        status = "FAILED"
        output = f"{u['email']} - FAILED: {check_password(u['password'])}"
    if status in summary:
        summary[status] = 1 + summary[status]
    else:
        summary[status] = 1
    lines.append(output)
    print(output)
print(f"Итого: {summary}")
print(lines)

with open(BASE / "report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
    # for l in lines:
    #     f.write(l + "\n")
    f.write(f"\nИтого: {summary}")

