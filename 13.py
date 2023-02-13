def extra_enumerate(x):
    total = sum(x)
    cumulative = 0
    for i, elem in enumerate(x):
        cumulative += elem
        yield i, elem, cumulative, cumulative/total
    