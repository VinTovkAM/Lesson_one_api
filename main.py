import requests


cities = ['Череповец','Лондон','аэропорт Шереметьево']
params = {"lang": "ru", "MTnq": ""}
for city in cities:
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=params)
    print(response.text)