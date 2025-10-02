i = int(input())
copos_quebrados = 0

for j in range(i):
    bandeja = input()
    latas, copos = map(int, bandeja.split())
    if latas > copos:
        copos_quebrados += copos

print(copos_quebrados)
