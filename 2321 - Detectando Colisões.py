retangulo_um = input()
retangulo_dois = input()
retangulo_um = list(map(int, retangulo_um.split()))
retangulo_dois = list(map(int, retangulo_dois.split()))

if retangulo_um[0] <= retangulo_dois[0] and retangulo_um[2] >= retangulo_dois[0] or retangulo_um[0] <= retangulo_dois[2] and retangulo_um[2] >= retangulo_dois[2]:
    print(1)
else:
    print(0)