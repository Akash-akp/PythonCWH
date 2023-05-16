a = "!!Akash!! Akash!!!!"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.capitalize())

print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.strip("!"))

print(a.count("Akash"))

print(a.split())
print(a.split("!"))

print(a.center(50))

b="Hello World 99"

print(b.endswith("99"))
print(b.startswith("Hello"))
print()

print(b.find("World"))
print(b.find("ej")) # find function push -1 if not present
print(b.index("World")) # index function push error if not present
# print(b.index("ej"))
print()

c = "HelloWorld23"

print(c.isalnum()) # contain a-z A-Z 0-9
print(c.isalpha()) # contain a-z A-Z
print(c.isspace()) # no space
print(c.isupper())
print(c.islower())
print(c.title())
print(c.istitle())