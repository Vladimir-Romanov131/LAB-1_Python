try:
    amount = float(input("Введите число: "))
    if amount < 0:
        raise ValueError("Некорректный формат!")
    rubles = int(amount)
    kopeks = int((amount - rubles) * 100)
    print("{} рублей. {} копеек.".format(rubles, kopeks))
except ValueError as e:
    print(e)