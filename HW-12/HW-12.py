cards = ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"] * 4
masti = [" Пики", " Черви", " Крести", " Буби"]
deck = (cards[i] + masti[i//9] for i in range(36))
iter_deck = iter(deck)
for i in iter_deck:
    print(i)
print("Stop iteration")
