# Створити три рядки.
# 	Створити алгоритм виведення на екран
# 	середини(мається на увазі символ або символи які стоять в середині рядка)
# 	кожного із трьох рядків введених з клавіатури.

str_1, str_2, str_3 = str(input("Введіть рядок 1: ")), str(input("Введіть рядок 2: ")), str(input("Введіть рядок 3: "))
s_1 = len(str_1) // 2           #визначимо номер середини рядка і округлимо до найменшого цілого
if len(str_1) % 2 == 0:         #пропишемо умову перевірки чи довжина рядка парне чи непарне значення, якщо парне, то в консолі буде виводитись два середніх символа
    print(str_1[s_1 - 1] + str_1[s_1])
else:                           #якщо непарне, то в консолі буде виводитись один середній символ
    print(str_1[s_1])

s_2 = len(str_2) // 2
if len(str_2) % 2 == 0:
    print(str_2[s_2 - 1] + str_2[s_2])
else:
    print(str_2[s_2])

s_3 = len(str_3) // 2
if len(str_3) % 2 == 0:
    print(str_3[s_3 - 1] + str_3[s_3])
else:
    print(str_3[s_3])