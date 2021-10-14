names = ["alma", "korte", "szilva"]
print(len(names))

print(names[1])
#szeletelés
print(names[::-1])

fruits = ["orange"]
veggies = ["carrot", "bean"]
fruits.append("apple") #csak egy értéket fogad
fruits.insert(0, veggies)
print(fruits)

empty =[]
print(empty)
empty +=["a"]
print(empty)

letters = []
letters += "JOHN"
print(letters)

numbers = ["x", "y", "z","x", "y", "z","x", "y", "z"]
numbers[1] = "a"
print(numbers)
del(numbers[0])
print(numbers)
numbers.remove("z")
print(numbers)

print("x" in numbers)
print("z" in numbers)
print("a" in veggies)
print("z" in veggies)

while "z" in numbers:
    numbers.remove("z")
print(numbers)