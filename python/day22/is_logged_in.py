def parse_cookies(text):
    result = {}
    for part in text.split("; "):
        if text == "":
            return result
        pair = part.split("=", 1)
        result[pair[0]] = pair[1]
    return result

print(parse_cookies("session_id=abc123; theme=dark") == {"session_id": "abc123", "theme": "dark"})
print(parse_cookies("theme=dark") == {"theme": "dark"})
print(parse_cookies("") == {})
print(parse_cookies("cart=3")["cart"] == "3")

def is_logged_in(cookies):
    return "session_id" in cookies and cookies["session_id"] != ""

print(is_logged_in({"session_id": "abc123"}) == True)
print(is_logged_in({"theme": "dark"}) == False)
print(is_logged_in({"session_id": ""}) == False)
print(is_logged_in({}) == False)

cases = [
    {"cookie": "session_id=abc123; theme=dark", "expected": True},
    {"cookie": "theme=dark", "expected": False},
    {"cookie": "session_id=; theme=dark", "expected": False},
    {"cookie": "", "expected": False},
    {"cookie": "theme=dark; session_id=xyz", "expected": True}
]
summary = {}
for case in cases:
    cookies = parse_cookies(case["cookie"])
    print(cookies)
    logged_in = is_logged_in(cookies)
    print(logged_in)
    status = "PASSED"
    if case ["expected"] == logged_in:
        print(repr (case["cookie"]), "PASSED")
    else:
        status = "FAILED"

        print(repr (case["cookie"]), "FAILED")

    if status in summary:
        summary[status] = summary[status] + 1
    else:
        summary[status] = 1
print(f"Итого:{summary}")

print(parse_cookies("token=abc=="))