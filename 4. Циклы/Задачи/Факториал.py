number = int(input("Введите число N: "))
answer = 1
for i in range(1, number):
    answer *= number
print(f"{number}! = {answer}")
