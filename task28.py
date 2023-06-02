#
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#  4

def summa_n(number_a, number_b):
    if number_a == 0:
        return number_b
    return summa_n(number_a - 1, number_b + 1)


number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))
print(f'Сумма числа {number_a} и числа {number_b} равна {summa_n(number_a, number_b)}')
