# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите число => "))
i = 0
n = 0
while n < number:
    n = 2**i
    i += 1
    if n < number:
        print(n, end = ' ')
    