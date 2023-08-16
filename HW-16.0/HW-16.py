# 6
def f6(file):
    with open(file, 'r', encoding='UTF8') as f:
        s = f.read()
        print(" ".join(s.split('\n')))


# 8
def f8(string):
    return string.strip("!?.")


# 14
def f14(file):
    with open(file, 'r', encoding='UTF8') as f:
        dict = {}
        for line in f:
            s = line.split()
            if s[2].isdigit():
                dict[s[0]] = (s[1], s[2])
        return dict
