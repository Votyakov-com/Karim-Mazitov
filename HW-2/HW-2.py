# 2
password = input()
ver_password = input()
if password == ver_password:
    print("YES")
else:
    print("NO")
# Ответ: False

# 3
print(min(map(int, input().split())))
# Ответ: 5

# 4
print(max(map(int, input().split())))
# Ответ: 30

# 5
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("True")
else:
    print("False")
# Ответ: True

# 6
a, b, c = map(int, input().split())
if a == b == c:
    print("равносторонний")
elif a == b or b == c or a == c:
    print("равнобедренный")
elif a + b > c and a + c > b and b + c > a:
    print("разносторонний")
else:
    print("вырожденный")
# Ответ: вырожденный

# 7
a, b, c, d = map(int, input().split())
if c <= a:  # c левее a
    if d < a:  # d левее a
        print(0)
    elif d < b:  # d левее b, но правее a
        print(d - a + 1)
    else:  # d правее b
        print(b - a + 1)
elif c <= b:  # c между а и b
    if d <= b:  # d левее b
        print(d - c + 1)
    else:  # d правее b
        print(b - c + 1)
else:  # c правее b
    print(0)
# Ответ: 7
