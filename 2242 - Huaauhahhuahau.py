vogais = ['a', 'e', 'i', 'o', 'u']
engracado = 'N'
risada = input()
vogais_risada= ''.join([letra for letra in risada if letra in vogais])
vogais_reversa = vogais_risada[::-1]

if vogais_risada == vogais_reversa:
    engracado = 'S'
    
print(engracado)
