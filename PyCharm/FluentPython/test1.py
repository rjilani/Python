import array

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print tshirts

symbols = 'avbcvf%A'

print tuple(ord(symbol) for symbol in symbols)

print array.array('I', (ord(symbol) for symbol in symbols))