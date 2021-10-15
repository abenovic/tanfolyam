from json import load

file = open("got.json")
content = load(file)

chars = content["characters"]
for char in chars:
    print(char["characterName"])

