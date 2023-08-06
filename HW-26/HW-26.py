# Задание №1
from random import *


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()

        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        if number in self.__abiturients:
            raise ValueError('Абитуриент уже внесен в базу данных')
        self.__abiturients[number] = abiturient

    # Проверка статуса абитуриента
    def get_status(self, number):
        return self.__abiturients[number].get_status()


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # СНИЛС
        self.__number = number

        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()

        # есть ли БВИ
        self.__bvi = bvi

    # Сеттер и геттер name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if self.check_str(new_name):
            self.__name = new_name.capitalize()

    # Сеттер и геттер surname
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if self.check_str(new_surname):
            self.__surname = new_surname.capitalize

    # Сеттер и геттер patronymic
    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, new_patronymic):
        if self.check_str(new_patronymic):
            self.__patronymic = new_patronymic.capitalize()

    # Сеттер и геттер age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.check_int(new_age):
            self.__age = new_age

    # Сеттер и геттер RNE
    @property
    def RNE(self):
        return self.__RNE

    @RNE.setter
    def RNE(self, new_RNE):
        if self.check_RNE(new_RNE):
            self.__RNE = new_RNE

    # Сеттер и геттер RNE
    @property
    def bvi(self):
        return self.__bvi

    @bvi.setter
    def bvi(self, new_bvi):
        if self.check_bool(new_bvi):
            self.__bvi = new_bvi

    # Геттер СНИЛС
    def get_number(self):
        return self.__number

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"

    # Проверка на строку
    @staticmethod
    def check_str(obj):
        return isinstance(obj, str)

    # Проверка на подходящий возраст
    @staticmethod
    def check_int(obj):
        return isinstance(obj, int) and 99 >= obj >= 16

    # Проверка на bool
    @staticmethod
    def check_bool(obj):
        return isinstance(obj, bool)

    # Проверка на RNE
    @staticmethod
    def check_RNE(obj):
        return isinstance(obj, int) and 100 >= obj >= 0

    def get_status(self):
        return self.__check()


module = CRM()

# добавление АР-а в список абитуриентов
ar = Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True)
module.add(ar)

# Проверка на возможность изменять имя и т.д. на корректные значения
ar.name = "alex"
ar.RNE = 93
ar.age = 12
# print(ar.name, ar.RNE, ar.age)

# добавление РА в список абитуриентов
ra = Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00")
module.add(ra)


# проверка, проходят ли абитуриенты
# print(module.get_status("111-222-333 00"))
# print(module.get_status("333-222-111 00"))


# Задание №2
class Emerald:
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0

        # цена изумруда
        self.__price = 0

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, amount):
        if self.__status <= amount:
            self.__status = amount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        self.__price = amount

    def account(self):
        self.status = 1

    def store(self):
        self.status = 2

    def set_price(self, amount):
        self.price = amount

    def info(self):
        return f"{self.__status}, {self.__price}"


class Shell:
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = 0

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, amount):
        if self.__status <= amount:
            self.__status = amount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        self.__price = amount

    def account(self):
        self.status = 1

    def process(self):
        self.status = 2

    def smelt(self):
        self.status = 3

    def set_price(self, amount):
        self.price = amount

    def info(self):
        return f"{self.__status}, {self.__price}"


class Coin:
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number

        # год выпуска монеты
        self.__year = year

        # номинал монеты
        self.__value = value

    def get_serial_number(self):
        return self.__serial_number

    def get_year(self):
        return self.__year

    def get_value(self):
        return self.__value

    def info(self):
        return f"{self.__serial_number}, {self.__year}, {self.__value}"


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []

    def add(self, obj, date, info):
        self.__storage.append(Entry(obj, date, info))

    def show_info(self, index):
        return self.__storage[index].info()

    def change_info(self, index, information):
        self.__storage[index].info(information)

    def classify(self, index):
        self.__storage[index].classify()

    def declassify(self, index):
        self.__storage[index].declassify()

    def delete(self, index):
        self.__storage[index] = None

    def __str__(self):
        for i in range(len(self.__storage)):
            print(self.__storage[i].info())


class Entry:
    def __init__(self, item, date, info, secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()

        # указатель на объект
        self.__item = item

        # дата создания записи
        self.__date = date

        # дополнительная информация об объекте
        self.__info = info

        # информация засекречена?
        self.__secret = secret

    def __get_next_ID(self):
        # можно создать свою функцию вместо этой
        return hash(self)

    @property
    def info(self):
        if self.__secret:
            return "Информация засекречена"
        return f"[{self.__date} {self.__info} {self.__item.info()}]"

    @info.setter
    def info(self, information):
        self.__info = information

    def classify(self):
        self.__secret = True

    def declassify(self):
        self.__secret = False


arch = Archive()
em = Emerald()
em.account()
arch.add(em, "5 августа", "Первый изумруд")
# Сижу туплю, не могу понять, в чем ошибка, которая после следующей строки вылезает, подскажите, пожалуйста
print(arch.show_info(0))
