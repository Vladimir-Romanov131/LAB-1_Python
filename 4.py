text = input("Введите текст: ")
words = text.split()

long_words = [word for word in words if len(word) > 7]
medium_words = [word for word in words if 4 <= len(word) <= 7]
short_words = [word for word in words if len(word) < 4]

print("Длинные слова:", long_words)
print("Нормальной длинный слова:", medium_words)
print("Короткие слова:", short_words)