import numpy as np
import random

# Ввод чисел в формате a + b
def calc(a,sign,b):
    if sign == "+":
        return (a+b)
    if sign == "-":
        return (a-b)
    if sign == "*":
        return (a*b)
    if sign == "/":
        return (a/b)

def bubble(way):
    a = [5,3,6,7,2,4,1,8]
    # Сортируем по возрастанию
    if way == 1:
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    # Сортируем по возрастанию
    elif way == 2:
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    else:
        return -1
    # Выводим

    return a

def Fibonacci(n):
    a = np.zeros(n)
    # Инициализируем первые 3 числа
    a[0] = 1
    a[1] = 1

    i = int(2)

    # Считаем числа
    while i < n:
        a[i] = a[i - 1] + a[i - 2]
        i = i + 1

    # Возвращаем массив
    return a.tolist()

