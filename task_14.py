# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input("Введите число N: "))
k = 0
n = 2**k
while (n < N):
    k = k + 1
    n = 2**k
    if n < N:
        print(n)
    if n > N:
        print("Число N меньше n в квадрате")
