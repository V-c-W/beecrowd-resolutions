dados = input()
dados = list(map(float, dados.split()))

if dados[2] / dados[0] > dados[3] / dados[1]:
    print("A")
else:
    print("G")
