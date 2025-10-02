resposta = -1
numeros = input()
numeros = list(map(int, numeros.split()))
divisores = []
for i in range(1, int(numeros[2]**0.5) + 1):
    if numeros[2] % i == 0:
        divisores.append(i)
        if i != numeros[2] // i:
            divisores.append(numeros[2] // i)

divisores = sorted(divisores)

for n in divisores:
    if n % numeros[0] == 0 and n % numeros[1] != 0 and numeros[2] % n == 0 and numeros[3] % n != 0:
        resposta = n
        break

print(resposta)
