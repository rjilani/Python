symbols = 'avbcvf%A'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print codes

codes1 = [ord(symbol1) for symbol1 in symbols if ord(symbol1) > 37]

print codes1

