star = 0
while star < 7:
    print("*" * star)
    star = star + 1


    while star < 7:
        line = ""
        number = 0
        while number < star:
            line += "*"
            number = number + 1
        print(line)
    star = star + 1



