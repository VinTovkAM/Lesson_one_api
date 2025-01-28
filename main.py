import requests


cities = ['Череповец','Лондон','сво']
params = {"lang": "ru", "MTnq": ""}
for city in cities:
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)