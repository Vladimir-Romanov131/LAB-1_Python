def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i - 1]
            return func(s)
        return wrapper
    return decorator

@pre_process(a=0.9)
def process_data(s):
    return s

data = [1, 2, 3, 4, 5, 6]
processed_data = process_data(data)
print(processed_data)