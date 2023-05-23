li = [8,10,4,5]
li.append(7) # 7 is append in li list
print(li)

li.reverse() # li list get reversed
print(li)

li.sort() # li list get sorted in ascending order
print(li)

li.sort(reverse=True) # lis list get sorted in descending order
print(li)

print(li.index(7)) #return the index of element

li.append(7) # 7 is appended in this list 2 times
print(li.count(7))

a =[1,2,3]
l = a  # l is having the reference of a (swallow copy)
l.append(4)
print(a)

a = [1,2,3]
l = a.copy() # l is new list having all element that a have (deep copy)
l.append(4)
print(a)

li.insert(2,5) # at index 2, 5 is inserted
print(li)

a=[1]
b=[2,3,4]
l = a+b
print(l) # b get concatenate in the end of a and get stored in new list
a.extend(b) # b get append in the end of a
print(a)