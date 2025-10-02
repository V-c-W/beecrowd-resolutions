while True:
    try:
        primo = 'Super'
        num = int(input())
        if num != 1 and num != 0:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    primo = 'Nada'
                    break
            
            num = str(num)
            
            if primo != 'Nada':
                for char in num:
                    if char not in '2357':
                        primo = 'Primo'
                        break
        else:
            primo = 'Nada'
        print(primo)
    except EOFError:
        break