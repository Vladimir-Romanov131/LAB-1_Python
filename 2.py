def is_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

lst = [1, 2, 3, 4, 5]
print(is_increasing(lst))