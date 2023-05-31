from functools import reduce

# MAP

li = [1, 2, 3, 4, 5]

cub = lambda x: x ** 3

newli = list(map(cub, li))
print(newli)

# FILTER

def greaterthan2(x):
    return x>2

newli = list(filter(greaterthan2,li))
print(newli)


# REDUCE
# from functools import reduce

def sum(x,y):
    return x+y

s = reduce(sum,li)
print(s)
