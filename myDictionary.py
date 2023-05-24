dic = {
    "Akash":10,
    "Kiran":30,
    "Jyoti":20,
    "Mamata":50,
    "Rama":70
}

print(dic["Akash"])
print(dic.get("Akash"))

print(dic.keys())
print(dic.values())
print(dic.items())

for key,value in dic.items():
    print(key,value)
