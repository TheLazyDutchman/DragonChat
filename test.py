import dndApi

url = "monsters"

monsters = dndApi.getInfo(url)['results']

keys = dict()
for monster in monsters:
    for key in dndApi.getInfo(monster['url'][5:]).keys():
        if key in keys:
            keys[key] += 1
        else:
            keys[key] = 1

    print(keys)
