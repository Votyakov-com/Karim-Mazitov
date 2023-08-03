n = int(input())
a = [int(input()) for x in range(n)]
sum = 0
for i in range(0, n, 2):
    sum += a[i]
print(sum)
# Ответ: 6
