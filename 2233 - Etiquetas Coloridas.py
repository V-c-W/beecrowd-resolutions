import math
r = input()
r = int(r, 16)
g = input()
g = int(g, 16)
b = input()
b = int(b, 16)

resultado = 1 + (math.floor(r / g)**2 + (math.floor(r / g)**2 * math.floor(g / b)**2))

resultado = hex(resultado)

print(f'{resultado[2:]}')
