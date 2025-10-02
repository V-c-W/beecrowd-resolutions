lista_linhas = []

dados = input()
linhas, colunas = map(int, dados.split())
lista_colunas = [0] * colunas
for i in range(linhas):
    linha = input()
    lista_linhas.append(sum(map(int, linha.split())))
    colunas_temp = [a + b for a, b in zip(list(map(int, linha.split())), lista_colunas)]
    lista_colunas = colunas_temp
    
maior_lin_col = [max(lista_linhas), max(lista_colunas)]
print(max(maior_lin_col))
