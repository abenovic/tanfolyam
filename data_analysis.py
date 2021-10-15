from json import load

file = open("mock_data.json", encoding="utf-8")
content = load(file)


for ip in content:
    print(ip["ip_address"])

min = 255
for ip in content:
    ips = ip ["ip_address"]
    prefix = int(ips.split(".")[0])
    if prefix < min:
        min = prefix
print(min)

