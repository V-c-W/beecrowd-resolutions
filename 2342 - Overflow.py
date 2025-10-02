maximo = int(input())
expressao = input()
expressao = list(map(str, expressao.split()))

if expressao[1] == '+':
    resultado = int(expressao[0]) + int(expressao[2])

else:
    resultado = int(expressao[0]) * int(expressao[2])
    
if resultado > maximo:
    print('OVERFLOW')
else:
    print('OK')
