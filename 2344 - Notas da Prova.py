nota = int(input())

match nota:
    case 0:
        print('E')
    case _ if nota >= 1 and nota <= 35:
        print('D')
    case _ if nota >= 36 and nota <= 60:
        print('C')
    case _ if nota >= 61 and nota <= 85:
        print('B')
    case _ if nota >= 86 and nota <= 100:
        print('A')
