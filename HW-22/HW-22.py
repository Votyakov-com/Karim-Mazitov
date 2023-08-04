# 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(5))        #Ans = 120


# 2
def is_prime(n, i=2):
    if n <= 1:
        return False
    elif i >= n // 2 + 1:
        return True
    elif n % i == 0:
        return False
    else:
        return is_prime(n, i + 1)


# print(is_prime(1001))      #Ans = False

# 3
def filter_odd(numbers):
    return list(filter(lambda x: x % 2 == 1, numbers))


# print(filter_odd([1, 2, 3, 4, 5]))     #Ans = [1, 3, 5]

# 4
def map_square(numbers):
    return list(map(lambda x: x ** 2, numbers))


# print(map_square([1, 2, 3, 4, 99]))     #Ans = [1, 4, 9, 16, 9801]

# 5
from functools import reduce


def reduce_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)


# print(reduce_sum([1, 2, 4, 6, 90]))    #Ans = 103

# 6
def partial_apply(func):
    def partial_func(x):
        return func(x, 10)

    return partial_func


func = lambda x, y: x + y
func2 = partial_apply(func)


# print(func2(8))     #Ans = 18

# 7
def compose(f, g):
    def h(*args):
        return g(f(*args))

    return h


f = lambda x: x + 5
g = lambda x: x ** 2
fg = compose(f, g)


# print(fg(6))    #Ans = 121

# 8
def create_functions_with_arguments(func, arguments):
    def new_func():
        return reduce(func, arguments)

    return new_func


func = lambda x, y: x * y
new_func1 = create_functions_with_arguments(func, [5, 4, 3])


# print(new_func1())     # 60


# 9
def compose_functions(functions):
    def composed_function(x, list=functions):
        if len(list) == 1:
            return list[0](x)
        else:
            return list[0](composed_function(x, list[1:]))

    return composed_function


g = lambda x: x + 5
k = lambda x: x * 2
p = lambda x: x ** 2
q = compose_functions([p, k, g])
# print(q(5))   #400
