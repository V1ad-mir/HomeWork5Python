# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
def degree(number_a, number_b):
    if number_b == 0:
        return 1
    return number_a * degree(number_a, abs(number_b) - 1)


number_a = float(input('Введите число: '))
number_b = int(input('Введите степень числа: '))
if number_b < 0:
    print(f'{number_a} в {number_b}й степени равно {1 / degree(number_a, number_b)}')
else:
    print(f'{number_a} в {number_b}й степени равно {degree(number_a, number_b)}')
