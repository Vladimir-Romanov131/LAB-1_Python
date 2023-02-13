sentence = input("Введите предложение: ")
words = sentence.split()
new_sentence = []

for word in words:
    if word[0].isupper():
        new_sentence.append(word.upper())
    else:
        new_sentence.append(word)

new_sentence = " ".join(new_sentence)
print(new_sentence)