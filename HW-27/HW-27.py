# 1
import datetime


class HeavenlyBody:
    """Родительский класс HeavenlyBody"""

    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        print(f"Название - {self.name}")
        print(f"Возраст - {self.age} млн. лет")
        print(f"Температура - {self.temperature} °C")
        print(f"Радиус - {self.radius} км")


class Planet(HeavenlyBody):
    """Дочерний класс Planet"""

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed

    def display(self):
        super().display()
        print(f"Орбитальная скорость - {self.orbital_speed} км/с")


class Star(HeavenlyBody):
    """Дочерний класс Star"""

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        super().display()
        print(f"Созвездие - {self.constellation} км/с")


# Проверка
# planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
# star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')
#
# print(Planet.__doc__, end='\n')
# planet1.display()
#
# print(Star.__doc__, end='\n')
# star1.display()


# 2
class Pastry:
    def __init__(self, name, price, manufacture_date, term):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def valid_until(self):
        d = self.term - (datetime.date.today() - self.manufacture_date).days
        if d < 0:
            return f"Срок годности истек"
        if d == 0:
            return f"Срок годности истекает сегодня"
        elif d == 1:
            return f"Срок годности истекает Завтра"
        elif d < 5:
            return f"Срок годности истекает через {d} дня"
        else:
            return f"Срок годности истекает через {d} дней"

    def order(self):
        print(f"\nНазвание - {self.name}")
        print(f"Цена - {self.price} руб.")
        print(f"Дата изготовления - {self.manufacture_date}")


class Cake(Pastry):
    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        super().order()
        print(f"Начинка - {self.filling}")

        if self.valid_until() == "Срок годности истек":
            print(self.valid_until())
        else:
            print(self.valid_until())
            print(f"Оформлен заказ - {self.name} с начинкой {self.filling}")


class BentoCake(Pastry):
    def __init__(self, name, price, manufacture_date, term, celebration):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        super().order()
        print(f"Праздник - {self.celebration}")

        if self.valid_until() == "Срок годности истек":
            print(self.valid_until())
        else:
            print(self.valid_until())
            print(f"Оформлен заказ - {self.name} на {self.celebration}")


# Проверка
# cake1 = Cake('Торт', 1300, datetime.date(2023, 8, 14), 3, 'вишня')
# bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 8, 2), 4, 'день рождения')
#
# cake1.order()
# bento1.order()


# 3
class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self.balance = balance
        self.interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, holder1):
        self.__holder = holder1

    def __str__(self):
        print(f"Владелец - {self.__holder}\nБаланс - {self.balance}\nПроцентная ставка - {self.interest_rate}\n")


class BankOperation(BankAccount):
    Operations = []

    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)

    def deposit(self, amount):
        self.balance += amount
        self.Operations.append(f"внесение наличных на счет: ${amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.Operations.append(f"снятие наличных: ${amount}")

    def add_interest(self):
        percent = self.balance * self.interest_rate
        self.balance += percent
        self.Operations.append(f"начислены проценты по вкладу: ${percent}")

    def history(self):
        for operation in self.Operations:
            print(f"Aккаунт {self.holder} - {operation}")


# Проверка
# account = BankOperation('Warren Buffett', 113000000000, 0.08)
# account.__str__()
# account.deposit(4000000000)
# account.withdraw(88000000000)
# account.add_interest()
# account.history()


# 5
class Investments:
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print(f"Тикер - {self.ticker}")
        print(f"Цена - {self.price}")
        print(f"Валюта - {self.currency}")
        print(f"Сектор - {self.industry}")


def buying_securities(func):
    def inside_func(self):
        if self.echelon == 3:
            print('Это высокорискованная сделка \n')
            return None
        return func(self)

    return inside_func


class Shares(Investments):
    count = 15

    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    @buying_securities
    def buying(self):
        if self.profit >= 5:
            print(
                f"Совершена покупка на сумму: {self.count * self.price}. Поздравляю, Вы стали совладельцем компании!\n")
            self.count -= 1
        else:
            print(f"Годовая доходность бумаги ниже 5%. Не рекомендуем приобретать акции.\n")

    def display(self):
        super().display()
        print(f"Количество - {self.count}")


class Bonds(Investments):
    count = 5

    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    @buying_securities
    def buying(self):
        if self.price <= self.nominal:
            print(
                f"Совершена покупка на сумму: {self.count * self.price}. Поздравляю, Вы стали совладельцем компании!\n")
            self.count -= 1
        else:
            print(f'Стоимость облигации больше ее номинальной стоимости. Не рекомендуем приобрести акции.\n')

    def display(self):
        super().display()
        print(f"Количество - {self.count}")


# Проверка
# i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
# i1.display()
# i1.buying()
# i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
# i2.display()
# i2.buying()
