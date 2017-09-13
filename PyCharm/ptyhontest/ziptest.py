
import collections

x = [1, 2, 3]
y = [4, 5, 6]

print (zip(x, y))

test = [a - b for a, b in zip(x, y)]

print (test)

print collections.Counter(x)

i = [100,1,24,56,6,4,87,6]

j = sorted(i)

for k in j:
    print k


def test(a,b,c):
    return a + b + c


a,b,c = x

print a