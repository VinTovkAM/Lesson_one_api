import requests


def main():
    cities = ['Череповец','Лондон','SVO']
    params = {"lang": "ru", "MTnq": ""}
    for city in cities:
        url = f'https://wttr.in/{city}'
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()