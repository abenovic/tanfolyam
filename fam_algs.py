#összegzés tétele
#egész számokat tartalmazó lista elemeit adjuk össze

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [9, 1, 20, 3, 40, 5, 60, 7]
sum = 0


for number in numbers:
    sum += number
print(sum)

min = numbers2[0]
for numbber in numbers2:
    if number < min:
        min = number
print(min)

#Van egy nevek listája, keresd ki belőle a leghoszabbat

names = ["Sanyi", "Gizi", "Ili", "Kati", "Barnabas", "Alabastrom", "Etel", "Marika"]
long = names[0]

for name in names:
    if len(name) > len(long):
        long = name
print(long)

#számlálás tétele
#Adott egész számok listája
#írd ki hány páros szám van benne

szamok = [5, 6, 2, 99, 110, 543, 3242532, 22]
paros = 0

for szam in szamok:
    if szam % 2 == 0:
        paros += 1
print(paros)

#Eldöntés tétele
#A nevek között megtalálható e Kati
names = ["Sanyi", "Gizi", "Ili", "Kati", "Barnabas", "Alabastrom", "Etel", "Marika"]
for name in names:
    if name == "Sanyi":
        print("Van Sanyi")
        break

# Szűrés
#Számok listájából egy másik listába a páros számokat
szamok = [5, 6, 2, 99, 110, 543, 3242532, 22]
lista_paros = []
lista_paratlan = []

for szam in szamok:
    if szam % 2 == 0:
        lista_paros.append(szam)
print(lista_paros) #ez a páros

for szam in szamok:
    if szam % 2 != 0:
        lista_paratlan.append(szam)
print(lista_paratlan) #ez a páratlan

#transzformáció (map)
#Hozz létre egy új listát ami a nevek hosszát tartalmazza
names = ["Sanyi", "Gizi", "Ili", "Kati", "Barnabas", "Alabastrom", "Etel", "Marika"]
hossz = []

for szo in names:
    hossz.append(len(szo))
print(hossz)

