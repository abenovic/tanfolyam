from requests import get

#response = get("https://training360.com/")
#print(response.text)

        # Letölti az index főoldalát és megszámolja hogy hány
        # sorban szerepel a koronavírus szó

        #Ezt hozzáfűzi a korona.txt állományba
        #ez legyen a formátum: 2021-10-15 13:14 - 3

response = get("https://index.hu/")
body = response.text
lines = body.splitlines()
count = 0
for line in lines:
    if "koronavírus" in line.lower():
        count += 1
now = datetime.now()
with open("korona.txt", mode="a") as f:
    f.write(f"{now} - {count}\n")


