# Створити алгоритм, який дозволить вивести на екран
# 	(порожній, тобто лише межі квадрата) квадрат із символів #
# 	Можна використовувати лише(всі інші можна окрім операторів виводу) наступні оператори print:
# 	print("#",end="")
# 	print(" ",end="")
# 	print("") #перехід на новий рядок, якщо треба.
# 	Вище буде оцінено рішення з введенням розміру квадрата з клавіатури)

x = int(input("Введіть ширину квадрату: "))

for i in range(x):
    for j in range(x):
        if i in [0, x-1] or j in [0, x-1]:
            print("#", end="")
        else:
            print(" ", end="")
    print()
