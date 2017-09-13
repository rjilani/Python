__author__ = 'rjilani'

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print (factorial(42))

print factorial.__doc__

print dir(factorial)

fact = factorial


print list(map(fact, range(11)))


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits,key=len))