bugs = [
    {"id": "BUG-01", "severity": "critical", "status": "open"},
    {"id": "BUG-02", "severity": "major",    "status": "closed"},
    {"id": "BUG-03", "severity": "minor",    "status": "open"},
    {"id": "BUG-04", "severity": "major",    "status": "open"},
    {"id": "BUG-05", "severity": "critical", "status": "closed"},
    {"id": "BUG-06", "severity": "trivial",  "status": "open"},
    {"id": "BUG-07", "severity": "major",    "status": "open"},
]
counts = {}
spisok = []
open_critical = 0

for r in bugs:
    s = r["severity"]
    if s in counts:
        counts[s] = counts[s] + 1
    else:
        counts[s] = 1
for severity, count in counts.items():
    print(f" - {severity}: {count}")
for b in bugs:
    if b["status"] == "open" and (b["severity"] == "critical" or b["severity"] == "major"):
        spisok.append(b["id"])
print(f'Открытые critical и major:{spisok}')
for o in bugs:
    if o["status"] == "open" and o["severity"]== "critical" :
        open_critical = open_critical + 1

if open_critical == 0:
        print("Релиз: можно")
else:
        print(f"Релиз: нельзя, открытых критических — {open_critical}")








