def make_email(name, domain="test.ru"):
    return f"{name}@{domain}"

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


def make_bad_email(name, kind):
    texts = {"noat": f"{name}test.ru", "twoat": f"{name}@@test.ru", "nodomain": f"{name}@", "space": f"{name} @test.ru",
             "spaces": "   "}
    return texts.get(kind)


if __name__ == "__main__":
    print(make_email("anna") == "anna@test.ru")
    print(make_password(8) == "Aaaaaaa1")
    print(make_password(1) is None)
    print(make_bad_email("anna", "noat") == "annatest.ru")