import requests


cities = ['Череповец','london','svo']
for number in cities:
    url = f'https://wttr.in/{number}?mnqTM&lang=ru'
    response = requests.get(url)
    print(response.text)