def count_by(items, key):
    counts = {}
    for item in items:
        value = item[key]
        counts[value] = counts.get(value, 0) + 1
    return counts


bugs = [
    {"id": "BUG-01", "severity": "critical", "status": "open"},
    {"id": "BUG-02", "severity": "major", "status": "closed"},
    {"id": "BUG-03", "severity": "minor", "status": "open"},
    {"id": "BUG-04", "severity": "major", "status": "open"},
    {"id": "BUG-05", "severity": "critical", "status": "closed"},
    {"id": "BUG-06", "severity": "trivial", "status": "open"},
    {"id": "BUG-07", "severity": "major", "status": "open"},
]

print(f" {count_by(bugs, 'severity')}")
print(f" {count_by(bugs, 'status')}")
