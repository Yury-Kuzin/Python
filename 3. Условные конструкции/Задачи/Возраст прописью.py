age = int(input("Enter you age: "))
match age//10:
    case 2:
        print('Двадцать ')
    case 3:
        print('Тридцать ')
    case 4:
        print('Сорок ')
    case 5:
        print('Пятьдесят ')
    case 6:
        print('Шестьдесят ')

match age%10:
    case 1:
        print('один год')
    case 2:
        print('два года')
    case 3:
        print('три года')
    case 4:
        print('четыре года')
    case 5:
        print('пять лет')
    case 6:
        print('шесть лет')
    case 7:
        print('семь лет')
    case 8:
        print('восемь лет')
    case 9:
        print('девять лет')
    case 0:
        print('лет')
