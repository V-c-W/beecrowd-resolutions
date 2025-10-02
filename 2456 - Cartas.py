valores = input()
sequencia = list(map(int, valores.split()))

if sequencia[0] < sequencia[1] and sequencia[1] < sequencia[2] and sequencia[2] < sequencia[3] and sequencia[3] < sequencia[4]:
    print("C")
elif sequencia[0] > sequencia[1] and sequencia[1] > sequencia[2] and sequencia[2] > sequencia[3] and sequencia[3] > sequencia[4]:
    print("D")
else:
    print("N")
