import json
import requests

from APIclasses.creatures import monster
from APIclasses.creatureData import abilities, getAlignment, getSenses, getSize, getSpeed

base_url = "https://www.dnd5eapi.co/api/"

def getInfo(request):
    sub_url = "/".join(request.split(" "))
    if sub_url.startswith('/api/'):
        sub_url = sub_url[5:]

    url = base_url + sub_url

    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def searchInfo(request):
    url_parts = request.split(" ")
    sub_url = "/".join(url_parts[:-1]) + "?name=" + url_parts[-1]
    url = base_url + sub_url

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def searchMonster(name):
    return searchInfo(f'monsters {name}')

def getMonster(url):
    monster_data = getInfo(url)
    if monster_data == None:
        print('returned nothing')
        return


    size = getSize(monster_data['size'])
    alignment = getAlignment(monster_data['alignment'])
    speed = getSpeed(monster_data['speed'])
    senses = getSenses(monster_data['senses'])

    ability_scores = abilities(
        monster_data['strength'],
        monster_data['dexterity'],
        monster_data['constitution'],
        monster_data['intelligence'],
        monster_data['wisdom'],
        monster_data['charisma']
    )

    return monster(
        monster_data['name'],
        size,
        alignment,
        monster_data['armor_class'],
        monster_data['hit_points'],
        monster_data['hit_points'],
        monster_data['hit_dice'],
        speed,
        ability_scores,
        list(),
        list(),
        list(),
        list(),
        list(),
        senses,
        list(),
        list(),
        list(),
        monster_data['type'],
        monster_data['subtype'],
        monster_data['challenge_rating'],
        monster_data['xp']
    )
