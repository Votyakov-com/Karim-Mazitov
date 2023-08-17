# 1

# print(statistics.mean(a))

# print(mean(a))

# print(mean(a))

# print(st.mean(a))

# print(mn(a))
import datetime

a = [1, 2, 3, 4]

# 2

# help("modules")

# print(dir())

# print(sys.modules.keys())


# 3

from sys import setrecursionlimit


def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)


setrecursionlimit(1500)
# print(recursive_function(1000, 0))   # Ans: 500500


# 4

import re

text = 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'
# print(re.findall('\d+', text))


# 5

from random import randint as rnd, choice as chc

array = []
for i in range(10):
    array.append(rnd(1, 100))
# print(*array)
# print(chc(array))


# 6

from math import sqrt

a = b = c = 0
# a, b, c = map(float, input().split())
D = b ** 2 - 4 * a * c
if a == 0:
    if c == 0 and b == 0:
        ans = "x ∈ R"
    elif b == 0:
        ans = "Корней нет"
    else:
        ans = f"x = {-c / b}"
elif D == 0:
    ans = f"x = {-b / (2 * a)}"
elif D > 0:
    ans = f"x1 = {(-b + sqrt(D)) / (2 * a)}\nx2 = {(-b - sqrt(D)) / (2 * a)}"
else:
    ans = "Корней нет"
# print(ans)


# 7

# print(datetime.datetime.now().time())


# 10

from calculator import *
while True:
    print("1.Сложение")
    print("2.Умножение")
    print("3.Вычитание")
    print("4.Деление")
    print("5.Выход из калькулятора")
    x = int(input("Выберите действие: "))
    if x == 5:
        print("Выход из калькулятора.")
        break
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат: ", end="")
    if x == 1:
        print(add(a, b))
    elif x == 2:
        print(multiply(a, b))
    elif x == 3:
        print(subtract(a, b))
    elif x == 4:
        print(divide(a, b))
    print()
