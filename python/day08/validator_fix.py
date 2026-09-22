name = input("Введите имя: ")
name = name.strip()

if name == "":
    print("Имя не может быть пустым")
elif len(name) < 2:
    print("Имя слишком короткое")
elif len(name) > 30:
    print("Имя слишком длинное")
else:
    print(f"Здравствуйте, {name}!")
