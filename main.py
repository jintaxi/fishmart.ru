from requests import get
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from os import getenv
from telebot import TeleBot
from os import path


token = getenv("TOKEN_SECRET")
bot = TeleBot(token=token)


"""Получаем реальную страницу сайта"""
url = "https://fishmart.ru/catalog/okhlazhdennaya_ryba/"
headers = {"User-Agent": UserAgent().chrome}
req = get(url=url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

"""Отладочная страница"""
# with open("site.html", "r") as file:
#     soup = BeautifulSoup(file.read(), "lxml")


try:
    """
    Если на странице ничего нет
    """

    # Данные со страницы
    result = soup.find('div', class_="catalog_no_items").text

    # Данные последнего состояния
    with open("/var/tmp/result.txt", 'r') as file:
        data = file.read()
    
    # Отладочня информация
    print("-"*40)
    print(f"[INFO] data  : {data}")
    print(f"[INFO] result: {result}")
    print("-"*40)

    if data == result:
        print(f"[INFO] Данные *не* поменялсиь. Файл *не* перезаписан")
    else:
        with open("/var/tmp/result.txt", 'w') as file:
            file.write(result)
        print(f"[INFO] Данные поменялись. Файл перезаписан")
        # ----- Отправка сообщения, что не осталось больше товара -----
        bot.send_message(443264815, f'Товар закончился', parse_mode='Markdown')

except Exception as _:
    """
    Если на странице что-то есть
    """
    print(f"[INFO] На сайте что-то есть")

    # Поиск необхомых элементов
    main_page = soup.find_all('div', id="main_block_page")
    positions = []
    for item in main_page:
        title = item.find('div', class_="bx_catalog_section_box").find('div', class_="img_box").find('a', class_="image main_preview_image offers_hide").get('title')
        link = "https://fishmart.ru" + item.find('div', class_="bx_catalog_section_box").find('div', class_="img_box").find('a', class_="image main_preview_image offers_hide").get('href')
        position = f"[{title}]({link})"
        positions.append(position)

    # Данные последнего состояния
    with open("/var/tmp/result.txt", 'r') as file:
        data = file.read()
    
   # Отладочня информация
    print("-"*40)
    print(f"[INFO] data  : {data}")
    print(f"[INFO] result: {positions}")
    print("-"*40)

    result = '\n'.join(positions)

    if data == result:
        print(f"[INFO] Данные *не* поменялсиь. Файл *не* перезаписан")
    else:
        with open("/var/tmp/result.txt", 'w') as file:
            file.write(result)
        print(f"[INFO] Данные поменялись. Файл перезаписан")
        bot.send_message(443264815, f'{result}', parse_mode='Markdown')

        
    
