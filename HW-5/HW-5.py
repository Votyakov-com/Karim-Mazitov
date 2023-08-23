a = int(input())
b = int(input())
n = int(input())
c = a ** 2 + b ** 2
k = 0
for i in range(n):
    x = int(input())
    if x ** 2 == c and x > 10 and (x % 4 == 0 or x % 3 == 0):
        k += 1
print(k)
# Ответ: 1
