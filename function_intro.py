def print_emp(): #függvény deklaráció
    print("Sanyi bácsi")
    print("asztalos")
    print("88")


def print_emp_name(emp_name="Teszt Jakab"):  #formális paraméter - a TesztJakab a default paraméter
    print("Az alkalmazott neve: " + emp_name)


def print_emp_details(name, position, age):
    print(f"""
        Alkalmazott neve: {name}
        Alkalmazott pozíciója: {position}
        Alkalmazott életkora: {age}
""")


print_emp()  #függvény hívás
print_emp_name("Sanyi")  #aktuális paraméter
print_emp_name("Gizike")

print_emp_name()


print_emp_details("Sanyi","asztalos",88)