class Employee:
    """Ez egy alkalmazottat tárol"""
def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
def get_name(self):
    return self.first_name + " " + self.last_name

john = Employee("John", "Doe", 30)

print(john.first_name)
print(john.last_name)
print(john.age)

