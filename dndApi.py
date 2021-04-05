import json
import requests

base_url = "https://www.dnd5eapi.co/api/"

def getInfo(request):
    sub_url = "/".join(request.split(" "))
    url = base_url + sub_url

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

# def findOptions(obj):
#     options = list()
#     if type(obj) is list:
#         for item in obj:
#             options.extend(findOptions(item))

#     if type(obj) is dict:
#         hasUrl = False

#         if 'url' in obj:
#             value = "!rule check " + obj['url'][5:]

#             name = obj['index']

#             if 'name' in obj:
#                 name = obj['name']
#             elif 'class' in obj:
#                 name = obj['class']

#             if type(name) is str:
#                 options.append((name, value))
                
#             hasUrl = True

#         for key, value in obj.items():
#             if not hasUrl:
#                 if type(value) is str and '/' in value:
#                     url = "!rule check " + value[5:]
#                     options.append((key, url))

#     return options