import json

text = """
{
  "users": [
    {
      "email": "anna@test.ru",
      "password": "Anna1234",
      "active": true
    },
    {
      "email": "ivan@test.ru",
      "password": "Ivan1234",
      "active": true
    },
    {
      "email": "olga@test.ru",
      "password": "Olga1234",
      "active": false,
      "role": null
    },
    {
      "email": "petr@test.ru",
      "password": "Petr1234",
      "active": true
    }
  ]
}
"""

data = json.loads(text)
print("Файл прочитан, пользователей:", len(data["users"]))