import sys
import requests


def best_hero(heroes_list):
    heroes_dict = {}
    url ='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit('К сожалению в запросе ошибка')
    jsonify_response = response.json()
    for hero in jsonify_response:
        name = hero['name']
        if name in heroes_list:
            heroes_dict[name] = int(hero['powerstats']['intelligence'])
    result = max(heroes_dict.items(), key=lambda x: x[1])
    return f'Самый умный супер герой {result[0]} - его интеллект {result[1]}'


if __name__ == "__main__":
     print(best_hero(['Hulk', 'Captain America', 'Thanos']))
