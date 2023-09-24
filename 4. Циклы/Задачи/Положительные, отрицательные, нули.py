countNumbers = int(input("Введите количество цифр: "))
positiveNumber = negativeNumber = zeroNumber = 0

for i in range(1, countNumbers + 1):
    number = int(input("Введите число: "))
    if number > 0:
        positiveNumber += 1
    elif number == 0:
        zeroNumber += 1
    elif number < 0:
        negativeNumber += 1
    else :
        print("Некоректное число")
print(f"Положительных: {positiveNumber}")
print(f"Отрицательных: {negativeNumber}")
print(f"Нулей: {zeroNumber}")
