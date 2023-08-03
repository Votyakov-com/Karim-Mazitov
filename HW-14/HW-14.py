# 1
names = ["Александр", "Алекс", "Альберт"]
surnames = ["Вотяк", "Вотяков", "Вотякович"]
name3 = "Романович"
for i in range(3):
    print(f"Диплом с отличием вручается {surnames[i]}у {names[i]}у {name3}у.")

# 2
A = input()
B = int(input())
C = int(input())
print(f"{A}{B:>04}-{C:>03}")

# 3
a = int(input())
b = int(input())
print(f"{a:>10}\n{b:>10}\n{a + b:>10}")

# 5
s = 100000000
r = int(input())
k = int(input())
sum_end = s * ((1 + r / 100) ** k)
print(f"{sum_end:,.2f}")

# 6
a, b, c, d = map(int, input().split())
bin8_temp = "Восьмибитном двоичном: {:08b}.{:08b}.{:08b}.{:08b}"
bin_temp = "Двоичном: {:b}.{:b}.{:b}.{:b}"
oct_temp = "Восьмиричном: {:o}.{:o}.{:o}.{:o}"
dec_temp = "Десятичном: {}.{}.{}.{}"
hex_temp = "Шестнадцатиричном: {:x}.{:x}.{:x}.{:x}"
template = [bin8_temp, bin_temp, oct_temp, dec_temp, hex_temp]
for temp in template:
    print(temp.format(a, b, c, d))
