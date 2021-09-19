from sender import send_mail
from bs4 import BeautifulSoup
from os import getenv
from requests import get
from fake_useragent import UserAgent


# Обращение к странице сайта и получение данных
url = "https://fishmart.ru/catalog/okhlazhdennaya_ryba/"
headers = {"User-Agent": UserAgent().chrome}
req = get(url=url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")


"""Начало парсинга"""
try:
    """Если на странице ничего нет"""


    # Данные со страницы сайта
    parse_data = soup.find('div', class_="catalog_no_items").text

    # Данные последнего состояния
    with open("/var/tmp/result.txt", 'r') as file:
        last_data = file.read()

    # С послдней проверки что-то изменилось
    # Надо отослать сообщение о том, что закончился товар
    if last_data != parse_data:
        with open("/var/tmp/result.txt", 'w') as file:
            file.write(parse_data)
        
        # Отправка сообщения    
        send_mail("Товар закончился!")

except Exception as _:
    """Если на странице что-то есть"""


    # Поиск необхомых элементов
    main_page = soup.find_all('div', id="main_block_page")
    parse_data = []
    for item in main_page:
        title = item.find('div', class_="bx_catalog_section_box").find('div', class_="img_box").find('a', class_="image main_preview_image offers_hide").get('title')
        link = "https://fishmart.ru" + item.find('div', class_="bx_catalog_section_box").find('div', class_="img_box").find('a', class_="image main_preview_image offers_hide").get('href')
        position = f"{title}: {link}"
        parse_data.append(position)

    # Данные последнего состояния
    with open("/var/tmp/result.txt", 'r') as file:
        last_data = file.read()

    parse_data = '\n'.join(parse_data)

    # С послдней проверки что-то изменилось
    # Надо отослать сообщение о том, что что-то появилось
    if last_data != parse_data:
        with open("/var/tmp/result.txt", 'w') as file:
            file.write(parse_data)
        # Отправка сообщения        
        send_mail(parse_data)  
    