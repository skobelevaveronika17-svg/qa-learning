def make_email(name, domain="test.ru"):
    return f"{name}@{domain}"


def make_bad_email(name, kind):
    texts = {"noat": f"{name}test.ru", "twoat": f"{name}@@test.ru", "nodomain": f"{name}@", "space": f"{name} @test.ru",
             "spaces": "   "}
    return texts.get(kind)


print(make_bad_email("anna", "noat") == "annatest.ru")
print(make_bad_email("anna", "twoat") == "anna@@test.ru")
print(make_bad_email("anna", "nodomain") == "anna@")
print(make_bad_email("anna", "space") == "anna @test.ru")
print(make_bad_email("anna", "spaces") == "   ")
print(make_bad_email("anna", "unknown") is None)


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


def generate_email_users():
    emails = [
        {"email": f"{make_email("valid")}", "expected": "OK"},
        {"email": f"{make_bad_email("veronchik", "noat")}", "expected": "Неверный формат email"},
        {"email": f"{make_bad_email("veronchik", "twoat")}", "expected": "Неверный формат email"},
        {"email": f"{make_bad_email("veronchik", "nodomain")}", "expected": "Неверный формат email"},
        {"email": f"{make_bad_email("veronchik", "space")}", "expected": "Неверный формат email"},
        {"email": f"{make_bad_email("   ", "spaces")}", "expected": "Заполните поле"}
    ]
    return emails
xei = {}
emails = generate_email_users()
for email in emails:
    status = "PASSED"
    check_email_result = check_email(email["email"])
    if check_email_result == email["expected"]:
        print("PASSED")
    else:
        print(f"FAILED: {check_email_result}")
    if status in xei:
        xei[status] = xei[status] + 1
    else:
        xei[status] = 1
print(f"Итого: {xei}")


generate_email_users()
