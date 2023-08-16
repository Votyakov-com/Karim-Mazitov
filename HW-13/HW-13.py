# 2
print(*list(map(lambda x: int(x) ** 3, input().split())))

# 3
print(*list(filter(lambda x: int(x) > 0, input().split())))

# 4
from functools import reduce

n = 8
print(reduce(lambda x, y: x * y, range(1, n + 1)))

# 5
# Решение 1
print(max(list(filter(lambda x: int(x) % 3 == 0, input().split()))))

# Решение 2
from functools import reduce

s = [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]
print(reduce((lambda x, y: y if (y % 3 == 0 and y > x) else x), s))
