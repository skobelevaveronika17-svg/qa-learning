

def make_bad_email(name, kind):
    texts = {"noat": "annatest.ru", "twoat": "anna@@test.ru", "nodomain": "anna@", "space": "anna @test.ru", "spaces":"   "}
    return texts.get(kind)
print(make_bad_email("anna", "noat") == "annatest.ru")
print(make_bad_email("anna", "twoat") == "anna@@test.ru")
print(make_bad_email("anna", "nodomain") == "anna@")
print(make_bad_email("anna", "space") == "anna @test.ru")
print(make_bad_email("anna", "spaces") == "   ")
print(make_bad_email("anna", "unknown") is None)