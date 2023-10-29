# 1
def infiltrate():
    pass


class SignedMessage:
    def __new__(cls, *args, **kwargs):
        infiltrate()
        return object.__new__(cls)

    def __init__(self, message, signature="-~=$([{PETR}])$=~-"):
        self.message = message
        self.signature = signature

    def __str__(self):
        return f"{self.message} {self.signature}"

    def __add__(self, other):
        return SignedMessage(self.message + other.message, self.signature)


# Проверка
# SIGNATURE = "-~=$([{PETR}])$=~-"
# print(SignedMessage("Hello ") + SignedMessage("world!") + SignedMessage(" Goodbye"))


# 2
from math import sqrt


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{" + f'{self.x}, {self.y}' + "}"

    def coords(self):
        return [self.x, self.y]

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return sqrt(sum(map(lambda x: x ** 2, self.coords())))

    def __len__(self):
        return int(sqrt(sum(map(lambda x: x ** 2, self.coords()))))  # len может возвращать только целые значения

    def __eq__(self, other):
        return self.coords() == other.coords()

    def __ne__(self, other):
        return self.coords() != other.coords()

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{" + f'{self.x}, {self.y}, {self.z}' + "}"

    def coords(self):
        return [self.x, self.y, self.z]

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return sqrt(sum(map(lambda x: x ** 2, self.coords())))

    def __len__(self):
        return int(sqrt(sum(map(lambda x: x ** 2, self.coords()))))  # len может возвращать только целые значения

    def __eq__(self, other):
        return self.coords() == other.coords()

    def __ne__(self, other):
        return self.coords() != other.coords()

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


# Проверка
# a = Vector2(4, 3)
# p = Vector3(4, 0, 3)
# b = Vector3(-1, 3, 0)
# c = a + b
# print(len(a), abs(a))
# print(str(-b))
# print(a == p, p != b)
# print(a * b)


# 3
class Item:
    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color

    def __ne__(self, other):
        return self != other

    def __eq__(self, other):
        return self == other

    def __lt__(self, other):
        if self.ID != other.ID:
            return self.ID < other.ID
        elif self.price != other.price:
            return self.price < other.price
        elif self.rarity != other.rarity:
            return self.rarity < other.rarity
        elif self.color != other.color:
            return self.color < other.color
        return False

    # Как мне кажется, необязательные модули
    # def __le__(self, other):
    #     return self < other or self == other
    #
    # # def __gt__(self, other):
    #     return not self < other
    #
    # def __ge__(self, other):
    #     return not self <= other

    def __str__(self):
        return f"[{self.ID}] {self.price}$ {self.rarity} #{self.color}"


# Проверка
# new_item1 = Item(128, 500, 1, "FF5819")
# new_item2 = Item(128, 400, 2, "FF5819")
# items = [new_item1, new_item2]
# print(*items, sep=", ")
# items.sort()
# print(*items, sep=", ")
