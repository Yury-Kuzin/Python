def sum_divisors(number):
    answer = 0
    for i in range(1, number):
        if number % i == 0:
            answer += i
    return answer


number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))
if sum_divisors(number_one) == number_two and sum_divisors(number_two) == number_one:
    print('YES')
else:
    print('NO')
