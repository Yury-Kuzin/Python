from math import sqrt


def prime_number_check(number) -> bool:
    j = 2
    while j < sqrt(number) + 1:
        if number % j == 0:
            return False
        j += 1
    return True


amount = int(input('Введите количество простых чисел: '))
i = 1
c = 2
while i <= amount:
    if prime_number_check(c):
        print(c)
        i += 1
    c += 1
