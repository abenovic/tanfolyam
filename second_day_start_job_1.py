char = 0
mondat = input("Adja meg a kifejezést: ")
for c in mondat:
    if c == "e":
        print("Van benne e")
    else:
        print(" ")


for c in mondat:
    if c == "e":
        break
        print("Van benne e")
for c in mondat:
    if (c == "e") or (c == "E"):
        break
        print("Van benne e")
print("End")

for c in mondat:
    if (c == "e") or (c == "E"):
        char = char + 1
print(char)
