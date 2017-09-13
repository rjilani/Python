__author__ = 'rjilani'

from collections import namedtuple

symbols = 'aAbBcCdDeEfF'

symbol_ord = tuple(ord(symbol) for symbol in symbols)

print symbol_ord

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print tokyo