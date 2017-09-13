__author__ = 'rjilani'

symbols = '$12'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

# print codes

code = [ord(symbol) for symbol in symbols]

# print code

x = 'my precious'

dummy = [x for x in 'ABC']

# print dummy

print x

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print tshirts

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

tshirts = [(size, color) for size in sizes for color in colors ]

print tshirts

for shirts in tshirts:
    print shirts