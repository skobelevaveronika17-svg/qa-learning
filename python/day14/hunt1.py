raw = ["passed", "failed", " passed", "blocked", "Passed", "failed ", "FAILED", "skipped"]
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