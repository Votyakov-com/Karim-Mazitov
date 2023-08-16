# 3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2


def calculate_total_area(L1):
    s = 0
    for i in L1:
        s += i.area()
    return s


# Проверка
# rectangle = Rectangle(4, 5)
# square = Square(3)
# print(calculate_total_area([rectangle, square]))


# 5
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Lamp(Device):
    def turn_on(self):
        print("Lamp turned on")

    def turn_off(self):
        print("Lamp turned off")


class Thermostat(Device):
    def turn_on(self):
        print("Thermostat turned on")

    def turn_off(self):
        print("Thermostat turned off")


class MotionSensor(Device):
    def turn_on(self):
        print("MotionSensor turned on")

    def turn_off(self):
        print("MotionSensor turned off")


class SmartHome:
    def __init__(self, devices):
        self.devices = devices

    def turn_on_all_devices(self):
        for device in self.devices:
            device.turn_on()

    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

# lamp = Lamp()
# motion_sensor = MotionSensor()
# thermostat = Thermostat()
# smart_home = SmartHome([lamp, motion_sensor, thermostat])
# smart_home.turn_on_all_devices()
# smart_home.turn_off_all_devices()


# 6
class Transfer:
    def __init__(self, sender_account, destination_account):
        self.sender_account = sender_account
        self.destination_account = destination_account

    def transfer(self, money):
        self.sender_account.transfer(self.destination_account, money)


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            raise ValueError("Недостаточно средств на счету")

    def get_balance(self):
        return self.balance

    def transfer(self, destination_account, money):
        self.withdraw(money)
        destination_account.deposit(money)


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return f"Проценты по счету - {self.balance * self.interest_rate / 100}"

    def get_interest_rate(self):
        return self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, fee_percentage=0):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        self.balance -= self.balance * self.fee_percentage / 100
        print("Комиссия вычтена")

    def get_fee_percentage(self):
        return self.fee_percentage


class Bank:
    accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def del_account(self, account):
        self.accounts.remove(account)

    def search_account(self, number):
        for account in self.accounts:
            if account.account_number == number:
                return account
        return "Аккаунт не найден"

    def transfer(self, sender_account_number, destination_account_number, money):
        self.search_account(sender_account_number).withdraw(money)
        self.search_account(destination_account_number).deposit(money)


# Создаем экземпляры счетов
savings_account = SavingsAccount(account_number="SAV-001", balance=1000, interest_rate=5)
checking_account = CheckingAccount(account_number="CHK-001", balance=500, fee_percentage=2)

# Создаем экземпляр банка и добавляем счета
bank = Bank()
bank.add_account(savings_account)
bank.add_account(checking_account)

# Выводим балансы счетов
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
# Savings Account Balance: 1000
# Checking Account Balance: 500

# Переводим деньги со счета-источника на счет-назначение
bank.transfer(sender_account_number="SAV-001", destination_account_number="CHK-001", money=500)

# Выводим обновленные балансы счетов
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
# Savings Account Balance: 500
# Checking Account Balance: 1000
