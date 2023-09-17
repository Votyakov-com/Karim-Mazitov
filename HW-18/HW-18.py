#3
def logging(func):
    def inside_func(*args, **kwargs):
        with open('input.txt', 'w', encoding='UTF8') as file:
            file.write(f'Вызов функции {func.__name__} с аргументами {args}, {kwargs}\n')
            return func(*args, **kwargs)
    return inside_func
