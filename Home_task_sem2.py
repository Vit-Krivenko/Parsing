"""
Урок 2. Парсинг HTML. BeautifulSoup
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
и извлечь информацию о всех книгах на сайте во всех категориях:
 название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Затем сохранить эту информацию в JSON-файле.
"""
from bs4 import BeautifulSoup
import urllib.parse
import requests
import re
import json

url = 'http://books.toscrape.com/'
# Заголовки запроса для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

# Отправка GET-запроса на URL
response = requests.get(url, headers=headers)
# Разбор HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

release_links = []
# Поиск всех элементов td с определенным классом, содержащих ссылки на фильмы
for link in soup.find_all('h3'):
    a_tag = link.find('a')  # Поиск тега <a> внутри элемента
    if a_tag:
        release_links.append(a_tag.get('href'))  # Добавление ссылки на фильм в список

url_joined = [urllib.parse.urljoin('http://books.toscrape.com/', link) for link in release_links]

books_info = []
for link in url_joined:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    book = soup.find('article', {'class': 'product_page'})
    book_dict = {}
    book_dict['Name'] = book.find('h1').text if book.find('h1') else ''
    book_dict['Price (Euro)'] = float(book.find('p', {'class': 'price_color'}).text[1:]) if book.find('p', {
        'class': 'price_color'}) else ''
    book_dict['Quantity_in_stock'] = int(
        re.findall(r'\d+', book.find('p', {'class': 'instock availability'}).text)[0]) if book.find(
        'p', {'class': 'instock availability'}) else ''
    book_dict['Description'] = book.find_all('p')[3].text.strip() if book.find_all('p')[3] else ''
    books_info.append(book_dict)




with open('books_one_page2.json', 'w', encoding='utf-8') as f:
    json.dump(books_info, f, ensure_ascii=False, indent=4)

