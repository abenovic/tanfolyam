name = "abba"
result = ""
counter = 0

for  c in name:
    result += c + "*"

print(result)

result = name[::-1]
print(result)

result = ""
for c in name:
    result = c + result
print(result)

print(name == name[::-1])
print(name == result)