import requests
from lxml import html
from pymongo import MongoClient
import time
import pandas as pd



response = requests.get("https://footranking.com/")
tree = html.fromstring(response.content)
print(tree)
table_rows = tree.xpath("//*[@class='RankingTable_rankingTable__dTNCx table']/tbody/tr")
print(table_rows)


# Печатаем строки таблицы
for row in table_rows:
    # Извлекаем текстовые значения ячеек
    cells = row.xpath("./td/span[1]/text()")
    print(cells)


list_data = []
for row in table_rows:
    list_data.append({
        'Rank': row.xpath(".//td/span/text()")[0].strip(),
        'Country': row.xpath(".//td/span[1]/text()")[1],
        'Points': row.xpath(".//td/span[1]/text()")[2],
        'Prev FIFA RANK': row.xpath(".//td/text()")[0].strip(),
        'Prev FIFA POINTS': row.xpath(".//td/text()")[1].strip()
    })
print(list_data)

df = pd.DataFrame(list_data)
df.index = df.index + 1
print(df)
df.to_csv('footranking.csv')
