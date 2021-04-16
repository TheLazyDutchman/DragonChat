import json
import requests

from APIclasses.creatureData import abilities

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


def getMonster(url):
    monster = getInfo(url)
    if monster == None:
        print('returned nothing')
        return

    ability_scores = abilities(
        monster['strength'],
        monster['dexterity'],
        monster['constitution'],
        monster['intelligence'],
        monster['wisdom'],
        monster['charisma'])

    print(ability_scores)

getMonster('monsters/bandit')