# 1
s = input().split()
try:
    print(float(s[0]) / float(s[2]))
except ZeroDivisionError:
    print("ERROR")

# 2
# while True:
#     try:
#         print(int(input(), 16))
#     except ValueError as name:
#         print(f"Не может быть паролем")


# 3
def check_results(name):
    try:
        print(f'{olympiad1["name"]} победитель {olympiad1["winners"][name]}')
    except KeyError:
        print(f'{olympiad1["name"]} призер -')
    finally:
        print("--------------------")

    try:
        print(f'{olympiad2["name"]} победитель {olympiad2["winners"][name][4]}')
    except IndexError:
        print(f'{olympiad2["name"]} победитель -')
    except KeyError:
        print(f'{olympiad2["name"]} призер -')
    finally:
        print("--------------------")


olympiad1 = {"name": "Пробная вышка",
             "winners": {
                 "Олеся Олимпиадникова": 594,
                 "Олег Олимпиадников": 587,
                 "Онисим Олимпиадников": 581,
             }
             }
olympiad2 = {"name": "Горные воробьи",
             "winners": {
                 "Ольга Олимпиадникова": (20, 20, 19, 20),
                 "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                 "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
             }
             }
check_results("Ольга Олимпиадникова")
check_results("Олеся Олимпиадникова")


# 4
def bad_func():
    try:
        while True:
            pass
    except:
        print("хе хе хе")
        bad_func()


bad_func()


# 5
class Lizard(Exception):
    pass


class Fire(Exception):
    pass


def Beer():
    try:
        x = input("Сколько кружек заказываете?\n").lower()
        if x == "где здесь туалет?":
            raise Fire
        if x == "ящерицу в стакане":
            raise Lizard
        x = int(x)
        assert x <= 2
        if x <= 0:
            raise ValueError
    except Fire:
        print("К сожалению, бар сгорел\nПриходите, когда мы отремонтируем бар, и", end=" ")
        return
    except Lizard:
        print("Извините, ящерицы закончились")
    except ValueError:
        print("Вы не можете заказать данное число кружек")
    except AssertionError:
        print("У бара сегодня кризис: не больше одной кружки в одни руки.")
    finally:
        print("закажите ещё что-нибудь!")
    Beer()


Beer()