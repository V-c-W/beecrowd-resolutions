dados = input()
dados = list(map(int, dados.split()))
x, y = (dados[0] - dados[2]), (dados[1] - dados[3])

if x < 0:
    x *= (-1)
if y < 0:
    y *= (-1)

cruzamentos = x + y

if cruzamentos >= 0:
    print(cruzamentos)
else:
    print((-1) * cruzamentos)
