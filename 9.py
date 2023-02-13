denominations = [1000, 500, 100, 50, 10, 5, 1]

def atm(balance, amount_requested):
    if amount_requested > balance:
        return "Операция не может быть выполнена!"

    result = []
    for denomination in denominations:
        if denomination <= amount_requested:
            num_notes = amount_requested // denomination
            amount_requested = amount_requested - num_notes * denomination
            result.append(f"{num_notes}*{denomination}")
    return " + ".join(result)

balance = 10000
amount_requested = 5436

print(atm(balance, amount_requested))

# Этот код реализует функцию банкомата, которая выдает минимальное количество купюр для запрашиваемой суммы. Функция atm принимает два аргумента: 
# balance, который определяет доступный баланс, и amount_requested, который определяет запрашиваемую сумму.

# Если запрашиваемая сумма превышает доступный баланс, функция возвращает сообщение "Операция не может быть выполнена!".

# В противном случае, функция использует цикл while для перебора деноминаций купюр, чтобы определить, сколько купюр каждого номинала нужно выдать.
#  Для каждой деноминации цикл while вычисляет количество купюр этого номинала, которые нужно выдать, и обновляет запрашиваемую сумму, вычитая из нее 
# выданные купюры.

# Результаты выдачи купюр сохраняются
