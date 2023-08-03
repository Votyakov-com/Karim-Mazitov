l, r = map(int, input().split())
ans = 0
for x in range(l, r + 1):
    for y in range(l, r + 1):
        for k in range(max(x, y), r + 1):
            if x ** 2 + y ** 2 == k ** 2:
                ans += 1
print(ans)
# Ответ : 26
