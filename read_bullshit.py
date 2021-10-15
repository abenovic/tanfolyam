with open("sample.txt") as f: #egész fájl kiiratása
    for line in f:
        print(line)


with open("sample.txt") as f: #első sor kiiratása 
    for line in f:
        print(line)
        break

