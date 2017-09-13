a = lambda x,y : x+y

print a (2,3)

a = [1, 2, 3, 4, 5, 6]

def foo(x):
    return 4*x

b = map(foo,a)

print b

c = map(lambda x: 3*x, a)

print c