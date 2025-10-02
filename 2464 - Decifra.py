abc = 'abcdefghijklmnopqrstuvwxyz'
cifra = input()
frase = input()
frase_final = ''

for i in range(len(frase)):
    for j in range(26):
        if cifra[j] == frase[i]:
            frase_final = frase_final + abc[j]
            break

print(frase_final)
