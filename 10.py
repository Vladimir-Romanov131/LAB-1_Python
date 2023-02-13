import re

def check_password_strength(password):
    if len(password) < 8:
        return "Слабый"
    if not re.search("[a-z]", password):
        return "Слабый"
    if not re.search("[A-Z]", password):
        return "Слабый"
    if not re.search("[0-9]", password):
        return "Слабый"
    if not re.search("[!@#$%^&*()]", password):
        return "Слабый"
    return "Сильный"

password = input("Введите пароль: ")
print("Надежность пароля:", check_password_strength(password))