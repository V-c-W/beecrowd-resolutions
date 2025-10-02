cartas = input()
carta_um, carta_dois = map(int, cartas.split())

if carta_um == carta_dois:
    print(carta_um)
elif carta_um > carta_dois:
    print(carta_um)
else:
    print(carta_dois)
