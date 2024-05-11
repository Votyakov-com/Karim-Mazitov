# 1
import requests

# url = input("Введите URL-адрес веб-страницы: ")
# response = requests.get(url)
#
# if response.status_code == 200:
#     print("Запрос выполнен успешно!")
# else:
#     print("Не удалось выполнить запрос, произошла ошибка")
#
# print(f"Состояние HTTP-ответа: {response.status_code}")


# 2
from PIL import Image

# my_image = Image.open('C:\\Users\\karim\\Downloads\\img1.jpg')

# = my_image.resize((800, 800))

# my_image.save('C:\\Users\\karim\\Downloads\\resize_img1.jpg')


# 3
import pytube

# link = input()
# video = pytube.YouTube(link)
# video = video.streams.get_highest_resolution()
# video.download('C:\\Users\\karim\\Downloads')


# 4
import colorama

# colorama.init()
# print(colorama.Fore.RED + "сам текст покрашен в какой-то цвет;")
# print(colorama.Back.CYAN + "сам текст + его фон покрашен в какой-то цвет;")
# print(colorama.Style.RESET_ALL + "снова текст, но без какого-либо окрашивания;")
# print(colorama.Fore.BLACK + colorama.Back.YELLOW + "сам текст с покрашенным фоном в какой-то цвет.")
# colorama.deinit()


# 5
import emoji

# text = input()
# print(emoji.demojize(text))

# 6
import pyperclip
import time

# print("Hello \n   world!\n   \t\t")
# while True:
#     text = pyperclip.paste()
#     text = " ".join(text.split()).replace('ё', "е").lower()
#     pyperclip.copy(text)
#     print(text)
#     time.sleep(1)


# 7
import wikipedia

print(wikipedia.summary("Computer program"))
