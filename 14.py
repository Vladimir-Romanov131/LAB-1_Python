def non_empty(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x for x in result if x and x != ""]
    return wrapper

@non_empty
def get_pages():
    return ["Страница 1", "", "Страница 2", None, "Страница 3"]

print(get_pages())