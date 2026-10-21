results = [
    {"email": "valid@test.ru", "status": "PASSED"},
    {"email": "short@test.ru", "status": "FAILED"},
    {"email": "empty@test.ru", "status": "PASSED"},
]

# 1. Записать отчёт: строка на каждого пользователя
with open("report.txt", "w", encoding='utf-8') as f:
    for r in results:
        f.write(r["email"] + " — " + r["status"]+"\n")


# 2. Дописать итог в конец
with open("report.txt", "a", encoding='utf-8') as f:
    f.write("Итого: проверено " + str(len(results)))


# 3. Прочитать отчёт и показать на экране
with open("report.txt", "r", encoding='utf-8') as f:
    print(f.read())
