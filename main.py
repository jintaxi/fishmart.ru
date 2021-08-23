import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json
from os import getenv
import telebot

token = getenv("TOKEN")
bot = telebot.TeleBot(token=token)


"""Реальный сайт"""
url = "https://fishmart.ru/catalog/okhlazhdennaya_ryba/"
headers = {"User-Agent": UserAgent().chrome}
req = requests.get(url=url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

"""Тестовый файл"""
# with open("site.html", "r") as file:
#     soup = BeautifulSoup(file.read(), "lxml")


try:
    result = soup.find('div', class_="catalog_no_items").text
    print(result)
    with open("BD.json", 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)
except Exception as ex:
    main_page = soup.find_all('div', id="main_block_page")
    items = []

    for item in main_page:
        item = item.find('div', class_="bx_catalog_section_box").find('div', class_="img_box").find('a', class_="image main_preview_image offers_hide")
        with open ("BD.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        items.append({"name": f"{item.get('title')}",
        "link": f"https://fishmart.ru/{item.get('href')}"})

        if data == items:
            status = 'Ничего не поменялось'

        else:
            with open("BD.json", 'w', encoding='utf-8') as file:
                json.dump(items, file, ensure_ascii=False)
            status = 'Есть изменения'

finally:
    pass

if status == 'Есть изменения':
    with open('users.json', 'r') as file:
        users = json.load(file)

    with open('BD.json', 'r') as file:
        data = json.load(file)

    my_string = []
    for item in data:
        my_string.append(f"[{item['name']}]({item['link']})")

    answer = '\n'.join(my_string)
    print(answer)
    for user in users:
        try:
            bot.send_message(user['id'], answer, parse_mode='Markdown')
        except Exception:
            pass
