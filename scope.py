def print_info():
    name = "Sanyi"
    print("függvényen belül: " + name)
    return name


def append_chars(name):
    print("tralala")
    return "xxx" + name + "xxx"


print_info()
emp = append_chars("Gizi")
print(emp)
