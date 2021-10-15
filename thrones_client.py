import requests

response = requests.get("https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json")
content = response.json()

chars = content["characters"]
for char in chars:
    print(char["characterName"])