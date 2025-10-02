n = 1

while True:
    num_ingressos = input()
    if int(num_ingressos) == 0:
        break
    ingressos = input()
    ingressos = [int(x) for x in ingressos.split(" ")]
    print(f"Teste {n}")
    for i in range(1, int(num_ingressos) + 1):
        if i == ingressos[i - 1]:
            print(i)
            print("")
            break
        
    n += 1
