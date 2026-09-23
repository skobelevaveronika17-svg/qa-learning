passwords = ["Anna123", "Annaaaa1", "Anna1234567890123456", "", "1234567A", "anna1234", "Annaaaaa" ]

for pwd in passwords:
    if len(pwd) < 8 or len(pwd) > 20:
        print(f"{pwd} — длина {len(pwd)}, нужно от 8 до 20")
        continue
    is_digit_found = False
    is_latter_found = False
    for character in pwd:
        if character.isdigit():
            is_digit_found = True
        if character.isupper():
            is_latter_found = True
    if not is_digit_found:
        print(f"{pwd} — нет цифры")
    elif not is_latter_found:
            print(f"{pwd} нет  заглавной буквы")
    else:
         print(f"{pwd} — OK")