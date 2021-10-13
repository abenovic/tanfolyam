name = "Kuflik a reten"
print(len(name)) #karakterszam
print(name[4]) #hanyadik karakter, nullaval kezdi:  K a nulladik , u a masodik...

lorem = """s simply dummy text of the printing and 
typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s 
with the release of Letraset sheets containing Lorem"""

print(lorem)

print(lorem[55])

en_nevem = "Benovics Andras"
for c in en_nevem: #definiál egy c változót s az en_nevem értékét felveszi
    print(c)

nev = "Sanyi"
age = 35
# A Sanyi máma 35 éves
print("A", nev, "máma", age,"éves") #ez a gagyi
print(f"A {nev} máma {age} éves") #ez a jobb

nevek = "Sanyi Sanyi"
print(nevek[1:7])
print(nevek[1:5:2])
print(nevek[9:0:-1])

