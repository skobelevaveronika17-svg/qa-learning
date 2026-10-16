# Итоги прогона тест-кейсов формы входа
results = ["passed", "failed", "passed", "blocked", "Passed", "failed "]

print("Всего кейсов:", len(results))                 # ожидаем 6
print("Первый кейс:", results[1])                    # ожидаем passed
print("Последний кейс:", results[len(results)-1])      # ожидаем failed
print("Упало:", results.count("failed"))             # ожидаем 2
print("Прошло:", results.count("passed"))            # ожидаем 3

sorted_results = sorted(results, key=lambda x: x[0].lower())
print("По алфавиту:", sorted_results)                # ожидаем отсортированный список

# Тестовый пользователь для кейсов
user = {"email": "anna@test.ru", "password": "Anna1234", "role": "user"}
print("Роль:", user["role"])                         # ожидаем user

# Делаем копию, чтобы проверить вход под админом
admin = user
admin["role"] = "admin"
print("Роль Анны:", user["role"])                    # ожидаем user

# На перезапуск — всё, кроме упавших
retest = ["failed", "failed", "passed", "blocked"]
for r in retest:
    if r == "failed":
        retest.remove(r)
        print(retest)
print("На перезапуск:", retest)                      # ожидаем ['passed', 'blocked']