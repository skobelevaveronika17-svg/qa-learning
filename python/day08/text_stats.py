sentence = input("Введите предложение: ").strip()
number = len(sentence)
text_without_spaces = sentence.replace(" ", "")
without_spaces = len(text_without_spaces)
words = sentence.split()
words_count = len(words)
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Символов с пробелами:{number}")
print(f"Символов без пробелов:{without_spaces}")
print(f"Слов:{words_count}")
print(f"Самое длинное слово:{longest}")
