# Задача 1
# Программа 1 - ООП, т.к. создается класс
# Программа 2 - Функциональное программирование, т.к. используется функция, в которой вместо цикла используют map
# Программа 3 - Императивное программирование, т.к. в функции используется цикл, программа выполняется последовательно


# Задача 2
from functools import reduce


# Cпособ 1
def sum_even_numbers1(list1):
    return reduce(lambda m, n: m + n, filter(lambda x: x % 2 == 0, list1))

    # Cпособ 2


def sum_even_numbers2(list):
    if len(list) == 1:
        if list[0] % 2 == 0:
            return list[0]
        else:
            return 0
    else:
        if list[0] % 2 == 0:
            return list[0] + sum_even_numbers1(list[1:])
        else:
            return sum_even_numbers1(list[1:])


numbers = [14, 93, 19, 38, 18, 51, 77]
print(sum_even_numbers1(numbers))
print(sum_even_numbers2(numbers))


# Задача 3
def sum_even_numbers3(list):
    s = 0
    for i in list:
        if i % 2 == 0:
            s += i
    return s


numbers = [60, 84, 9, 49, 7, 85, 38]
print(sum_even_numbers3(numbers))
