teste = 1
while True:
    N = int(input())
    if N == 0:
        break
    nome_um = input()
    nome_dois = input()
    print(f"Teste {teste}")
    for i in range(0, N):
        num_um, num_dois = input().split(" ")
        soma = int(num_um) + int(num_dois)
        if soma % 2 == 0:
            print(nome_um)
        else:
            print(nome_dois)
    print("")
    teste += 1
