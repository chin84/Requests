import requests
import random

url = requests.get('https://akabab.github.io/superhero-api/api/all.json')
jsoni_url = url.json()


def iq_hero(name):
    name_lst = []
    stats_lst = []
    for nam in jsoni_url:
        for value, stats in nam.items():
            if value == 'name':
                name_lst.append(stats)
        for mind, intel in nam['powerstats'].items():
            if mind == 'intelligence':
                stats_lst.append(intel)
    heroes_dict = dict(zip(name_lst, stats_lst))
    return f'Самый умный герой {name} с интеллектом {heroes_dict[name]}'


def max_intellect():
    name_lst = []
    for nam in jsoni_url:
        for value, stats in nam.items():
            if value == 'name':
                name_lst.append(stats)
    return name_lst


choice_hero = random.choice(max_intellect())
result = iq_hero(choice_hero), iq_hero(choice_hero), iq_hero(choice_hero)
max_result = max(result)

if __name__ == "__main__":
    print(max_result)
