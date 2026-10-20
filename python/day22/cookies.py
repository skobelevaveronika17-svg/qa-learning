def parse_cookies(text):
    result = {}
    for part in text.split("; "):
        if text == "":
            return result
        pair = part.split("=")
        result[pair[0]] = pair[1]
    return result

print(parse_cookies("session_id=abc123; theme=dark") == {"session_id": "abc123", "theme": "dark"})
print(parse_cookies("theme=dark") == {"theme": "dark"})
print(parse_cookies("") == {})
print(parse_cookies("cart=3")["cart"] == "3")

def is_logged_in(cookies):
    return "session_id" in cookies is not None and cookies["session_id"] != ""

print(is_logged_in({"session_id": "abc123"}) == True)
print(is_logged_in({"theme": "dark"}) == False)
print(is_logged_in({"session_id": ""}) == False)
print(is_logged_in({}) == False)
