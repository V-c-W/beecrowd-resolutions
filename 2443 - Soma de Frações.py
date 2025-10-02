import math

dados = input()
dados = list(map(int, dados.split()))
dividendo, divisor = 0, 0

if dados[1] == dados[3]:
    dividendo = dados[0] + dados[2]
    divisor = dados[1]
    gcd = int(math.gcd(dividendo, divisor))
    dividendo = int(dividendo / gcd)
    divisor = int(divisor / gcd)
else:
    divisor = dados[1] * dados[3]
    dividendo = (dados[0] * dados[3]) + (dados[2] * dados[1])
    gcd = int(math.gcd(dividendo, divisor))
    dividendo = int(dividendo / gcd)
    divisor = int(divisor / gcd)

print(f"{dividendo} {divisor}")
