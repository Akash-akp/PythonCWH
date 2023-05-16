name = input("Enter your name : ")
firstchar = name[0]
about = """
My name is \"{}\"
The first Alphabet of my name is {}
I love programming
My favourite programming language is python
I want to be a successful man
""".format(name,firstchar)
print(about)

# print every alphabet of my name

for character in name:
    print(character)