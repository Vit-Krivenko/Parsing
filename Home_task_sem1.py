
import requests
import pandas as pd
import json

city = input("Введите интересующий вас город: ")
category = input("Введите категорию заведения для поиска в городе: ")

url = "https://api.foursquare.com/v3/places/search"

client_id = "__"
client_secret = "__"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near":city,
    "query": category

}
response = requests.get(url, params=params, headers=headers)
#print(response.text)


if response.status_code == 200:
    print("Успешный запрос")
    data = response.json()  
    venues = data["results"]

    venues_data = []
    for venue in venues:
        name = venue["name"]
        address = venue.get("location", {}).get("address", "Адрес не указан")
        rating = venue.get("rating", "-")
        venues_data.append({"Название": name, "Адрес": f'{address}', 'Рейтинг': rating})
    df = pd.DataFrame(venues_data)
    print(df.head)
else:
    print("Запрос не удался", response.status_code)