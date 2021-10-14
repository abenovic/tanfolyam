#Válassz a menüpontok közül
#1. Új név rögzítése
#2. Nevek listázása
#3. Kilépés

#Add meg a nevet
#Listázza ki a neveket.

tevekenyseg = 0
nev=""
lista =[]
menu = """Válassz a menüpontok közül
#1. Új név rögzítése
#2. Nevek listázása
#3. Kilépés"""
print(menu)
while tevekenyseg != "3":
    tevekenyseg = input(menu)
    print("Valasztott menüpont: + tevekenyseg")
    if tevekenyseg == "1":
        nev = input("Ird be a nevet: \n")
        nev.append(lista)
    elif tevekenyseg == "2":
        for nev in lista:
            print(nev)
    else:
        print("Ismeretlen menupomnt")

        #megoldani