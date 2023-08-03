a = []
for x in input().split():
    a.append(x)
max_word = ""
max_kolvo = 0
for i in a:
    if a.count(i) > max_kolvo:
        max_word = i
        max_kolvo = a.count(i)
print(max_word)
# Ответ: cat
