raw =  ["passed", "failed", " passed", "blocked", "Passed", "failed ", "FAILED", "skipped"]
allowed = ["passed", "failed", "blocked"]
clean = []
unknown = []
for s in raw:
    cleaned_status = s.strip().lower()
    clean.append(cleaned_status)
    if cleaned_status not in allowed:
        unknown.append(cleaned_status)
print("passed:", clean.count("passed"))
print("failed:", clean.count("failed"))
print(f"Неизвестные статусы: {unknown}")
print(f"Исходные данные: {raw}")

counts = {}
for r in clean:
    if r in counts:
        counts[r] += 1
    else:
        counts[r] = 1
for key, value in counts.items():
    print(f"{key} - {value}")
if len(raw) == 0:
    print("Прогон пуст")
else:
    percent = round(counts.get('passed', 0) / len(clean) * 100, 1)
    print(f"Прошло: {percent}%")
