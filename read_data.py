data = []
with open("mockdata.csv", encoding="utf-8") as f: #egész fájl kiiratása
    i = 0
    for line in f:
        parts = line.split(",")
        name = parts [0] + " " + parts[1]
        ip = parts [3]
        item = {"name": name, "ip": ip}
        data.append(item)
    i += 1
print(data)