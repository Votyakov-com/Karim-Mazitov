# 1
class CoffeeMachine:
    def __init__(self, water_level=0, coffee_level=0, milk_level=0, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, number):
        self.cups += number

    def check_resources(self):
        if self.water_level > 0 and self.milk_level > 0 and self.coffee_level > 0 and self.sugar_level > 0 \
                and self.cups > 0:
            return True
        else:
            return False

    def make_coffee(self):
        if self.check_resources():
            self.water_level -= 1
            self.coffee_level -= 1
            self.cups -= 1
            self.milk_level -= 1
            self.sugar_level -= 1
            print("Кофе готов!")
        else:
            print("Недостаточно ингридиентов!")


# 2
class PhotoCamera:
    def __init__(self, brand="", model="", resolution=(), is_on=False, memory_capacity=0):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = []

    def take_photo(self):
        print(f"Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}.")

    def get_camera_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}."

    def turn_on(self):
        self.is_on = True
        print("Фотокамера включена.")

    def turn_off(self):
        self.is_on = False
        print("Фотокамера выключена.")

    def is_camera_on(self):
        return self.is_on

    def store_photo(self):
        if len(self.photos) < self.memory_capacity:
            self.photos.append(
                f'Фотография №{len(self.photos) + 1} с разрешением {self.resolution[0]}x{self.resolution[1]}')
            return True
        else:
            return False

    def view_photos(self):
        return self.photos

    def clear_memory(self):
        self.photos = []


# Проверка
# camera1 = PhotoCamera("Canon", "3.3", (1920, 1080), False, 10)
# camera1.turn_on()
# print(camera1.get_camera_info())
# camera1.take_photo()
# camera1.store_photo()
# camera1.take_photo()
# camera1.store_photo()
# print(camera1.view_photos())
# camera1.clear_memory()
# print(camera1.view_photos())


# 3
from random import randint


class Revolver:
    def __init__(self):
        self.max_capacity = 6
        self.bullets = [0] * 6
        self.indicator = 0

    def add_bullet(self, bullet):
        if self.bullets.count(0) > 0:
            self.bullets[self.indicator] = bullet
            self.indicator += 1
            return True
        else:
            return False

    def add_bullets_from_list(self, list):
        if len(list) == 0 or self.bullets.count(0) == 0:
            return False
        else:
            for bullet in list:
                self.add_bullet(bullet)
            return True

    def shoot(self):
        if self.indicator == 0:
            return None
        self.bullets[self.indicator - 1] = 0
        self.indicator -= 1

    def unload(self, all_items=False):
        self.all_items = all_items
        if self.indicator == 0:
            return None
        elif self.all_items == True:
            ans = self.bullets.copy()
            self.bullets = [0] * 6
            return ans
        else:
            ans = self.bullets[self.indicator - 1]
            self.bullets[self.indicator - 1] = 0
            return ans

    def scroll(self):
        self.indicator = randint(1, 6)

    def bullet_count(self):
        return 6 - self.bullets.count(0)


# Проверка
rev1 = Revolver()

rev1.add_bullet(1)
print(*rev1.bullets)

rev1.shoot()
print(*rev1.bullets)

rev1.add_bullets_from_list([1, 2, 3, 4])
print(*rev1.bullets)

rev1.unload()
print(*rev1.bullets)

rev1.scroll()
rev1.shoot()
print(*rev1.bullets)
print(rev1.bullet_count())
