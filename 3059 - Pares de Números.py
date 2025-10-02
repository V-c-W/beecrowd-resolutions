pares = 0
dados = input()
N, I, F = map(int, dados.split())
lista_numeros = input()
lista_numeros = list(map(int, lista_numeros.split()))
lista_t = []

for j in range(N):
    for h in range(j, N):
        if j == h:
            pass
        elif (lista_numeros[j] + lista_numeros[h]) <= F and (lista_numeros[j] + lista_numeros[h]) >= I:
            pares += 1

print(pares)
