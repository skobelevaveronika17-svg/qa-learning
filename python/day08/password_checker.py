password = input("Введите пароль: ")
is_digit_found = False
is_latter_found = False
is_spase_found = True

for character in password:
    if character.isdigit():
        is_digit_found = True
    elif character.isalpha():
        is_latter_found = True
    elif character.isspace():
        is_spase_found = False
if not is_digit_found:
    print("В пароле нет цифр")
if not is_latter_found:
    print("В пароле нет букв")
if not is_spase_found:
    print("Пробел недопустим")
if len(password) < 8:
    print("Пароль слишком короткий")
elif len(password) > 20:
    print("Пароль слишком длинный")
if is_digit_found and is_latter_found and is_spase_found and len(password) > 8 and len(password) < 20:
    print("Пароль подходит")
