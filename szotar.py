products = {"orange": 30, "apple": 50, "bread": 10}
print(products["orange"])
print(products["apple"])
print(products["bread"])

products["orange"] = 29
print(products)

products["milk"] = 16
print(products)

my_products = {}
print(my_products)
my_products["bread"] = 88
print(my_products)

del(products["orange"])
print(products)

print(products.keys())

for key in products.keys():
    print(key + ": " + str(products[key]))

if "apple" in products:
    print("Alma benne van")

if "phone" in products:
    print("telefon nincs benne")

for (key, value) in (products.items()):
    print(key + " " + str(value))