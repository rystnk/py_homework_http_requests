import requests


url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)

data = response.json()


def smartest_hero(obj):
    dict_hero = {}
    for hero in data:
        if hero['name'] not in obj:
            continue
        else:
            intelligence = int(hero['powerstats']['intelligence'])
            dict_hero[hero['name']] = intelligence
    sort_dict_hero = sorted(dict_hero.items(), key=lambda x: x[1], reverse=True)
    print(f'Самый умный супергерой: {sort_dict_hero[0][0]}')


list_hero = ['Hulk', 'Captain America', 'Thanos']

smartest_hero(list_hero)
