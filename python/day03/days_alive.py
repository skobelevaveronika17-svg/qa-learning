from datetime import datetime

years= int(input("Какой у тебя год рождения?"))
age= datetime.now().year - years
days=age * 365
print (f"Тебе примерно {age} лет, это около {days} дней")
