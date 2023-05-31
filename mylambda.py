
sqr = lambda x: x*x
cube = lambda x: x**3
avg = lambda *x: sum(x)/len(x);

def apply(fx,value):
    return fx(value)

print(sqr(5))
print(cube(5))
print(apply(sqr,9))
print(avg(1,2,4,5))

