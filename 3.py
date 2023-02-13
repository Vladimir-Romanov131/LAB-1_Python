card_number = input("Введите номер дебетовой карты: ")

hidden_number = card_number[:4] + " **** **** " + card_number[-4:]
print("Скрытый номер:", hidden_number)