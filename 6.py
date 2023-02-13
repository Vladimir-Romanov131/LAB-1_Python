sentence = input("Введите предложение: ")
unique_chars = []
for char in sentence:
    if sentence.count(char) == 1:
        unique_chars.append(char)
print("Уникальные символы: ", ''.join(unique_chars))