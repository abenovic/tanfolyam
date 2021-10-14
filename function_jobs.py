# Írj egy függvényt ami kiírja hogy "Hello Functions!"

def koszonto():
    print("Hello Functions!")

koszonto()

# Írj egy függvényt ami két paramétert kap és összeadja azokat!


def osszaadas(a, b):
      return a + b

osszaadas(5,6)

# Írj egy függvényt ami vissszaadja hogy a paraméterként átadott szöveg hány sapce karaktert tartalmaz

def mennyi_space(s):
    count = 0
    for c in s:
        if C == " ":
            count +=1


# Írj egy függvényt ami a paraméterként átadott list átlagát adja vissza

def calc_avarg(numbers):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)

# Írj egy függvényt ami visszaadja hogy hány magánhangzó van a paraméterként átadott szövegben

def count_params(s):
    count = 0
    for c in s:
        if c in "aAeEiIoOuU":
            count +=1
    return count

