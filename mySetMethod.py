s1 = {1,True,"Tokyo",5}
s2 = {True,5,"Akash",36}

print(s1.union(s2))
s1.update(s2)
print(s1,s2)

s1 = {1,True,"Tokyo",5}

print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)

s1 = {1,True,"Tokyo",5}

print(s1.difference(s2))
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1,s2)

s1 = {1,2,5,6}
s2 = {5,6}

print(s1.issuperset(s2))
print(s2.issubset(s1))

s1.remove(1) # throw error if not present
s1.discard(1)

print(s1.pop()) # randomly remove any element

del s1 # delete s1
s2.clear() #clear s2
print(s2)

s1 = {1,2,4}

if 1 in s1:
    print("present")
else:
    print("not present")
