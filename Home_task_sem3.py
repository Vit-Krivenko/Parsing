import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['Seminar3']
collections = db['books']

count = collections.count_documents({})
print(f'Количество записей в базе данных: {count}')

query = {'Rating':5}
print(f"Количество книг c Рейтингом 5: {collections.count_documents(query)}")

query = {'Price (Euro)':{'$gte':30}}
print(f"Количество книг cтоимостью больше 30: {collections.count_documents(query)}")

query = {'Quantity_in_stock':{'$lt':10}}
print(f"Количество книг в наличии меньше  10 штук: {collections.count_documents(query)}")

query = {'Category':'Default'}
print(f"Количество документов с категорией Default: {collections.count_documents(query)}")

query = {'Category':{'$ne':'Default'}}
print(f"Количество документов с категорией НЕ Default: {collections.count_documents(query)}")