elements = [
    {"tag": "input", "id": "email", "type": "email", "class": "field", "data-testid": "login-email"},
    {"tag": "input", "id": "password", "type": "password", "class": "field"},
    {"tag": "input", "type": "checkbox", "class": "check"},
    {"tag": "button", "id": "submit", "type": "submit", "class": "btn primary"},
    {"tag": "a", "class": "link", "href": "#"},
]


def by_id(element_id):
    return f"#{element_id}"

def by_class(name):
   return f".{name}"

def by_attr(attr,value):
    return f'[{attr}="{value}"]'

def find_by_attr(elements, attr, value):
    found = []
    for element in elements:
        if element.get(attr) == value:
            found.append(element.get("id", "без id"))
    return found


def is_unique(elements, attr, value) -> bool:
    return len(find_by_attr(elements, attr, value)) == 1

    return var
    #print(f'{attr=} {value=} {find_by_attr(elements, attr, value)=}')
    #return True


print(by_id("email") == "#email")
print(by_class("field") == ".field")
print(by_attr("type", "password") == '[type="password"]')
print(by_attr("data-testid", "login-email") == '[data-testid="login-email"]')
print(find_by_attr(elements, "class", "field") == ["email", "password"])
print(find_by_attr(elements, "type", "checkbox") == ["без id"])
print(find_by_attr(elements, "name", "login") == [])

print(is_unique(elements, "id", "email") == True)
print(is_unique(elements, "class", "field") == False)
print(is_unique(elements, "name", "login") == False)

