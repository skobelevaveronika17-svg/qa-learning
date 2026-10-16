def is_release_allowed(bugs):
    for bug in bugs:
        if bug["severity"] == "critical" and bug["status"] == "open":
            return False
    return True

bugs = [
    {"id": "BUG-01", "severity": "critical", "status": "open"},
    {"id": "BUG-02", "severity": "major",    "status": "closed"},
    {"id": "BUG-03", "severity": "minor",    "status": "open"},
    {"id": "BUG-04", "severity": "major",    "status": "open"},
    {"id": "BUG-05", "severity": "critical", "status": "closed"},
    {"id": "BUG-06", "severity": "trivial",  "status": "open"},
    {"id": "BUG-07", "severity": "major",    "status": "open"},
]

print(is_release_allowed(bugs) == False)
print(is_release_allowed([]) == True)
print(is_release_allowed([{"id": "BUG-05", "severity": "critical", "status": "closed"}]) == True)





