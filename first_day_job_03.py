i = 1
while i < 21:
    result = (i * 7)
    
    if result % 3 == 0:
        print(str(result) + "*")
    else:
        print(result)

    i = i + 1

print("end")