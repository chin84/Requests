import sys
import requests


def best_hero(heroes_list:['Hulk', 'Capitan America', 'Thanos']):
    heroes_dict = {}
    url ='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit('К сожалению в запросе ошибка')
    jsonify_response = response.json()
    for hero in jsonify_response:
        heroes_lst = ['Hulk', 'Capitan America', 'Thanos']
        if hero['name'] in heroes_lst:
            heroes = int(hero['powerstats']['intelligence'])
            heroes_dict = hero['name']
    result = f"\nСамый умный супергерой: {heroes_dict} - его интелект: {heroes}"
    return result


if __name__ == "__main__":
     print(best_hero(['Hulk', 'Captain America', 'Thanos']))
