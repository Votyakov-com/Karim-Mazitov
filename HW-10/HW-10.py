b = set(input())
a = sorted([x for x in b if x in "0123456789"])
if len(a) == len(b):
    print("NO")
else:
    print("".join(a))
# Ответ: 12456789
