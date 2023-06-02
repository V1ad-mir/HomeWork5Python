# Даны два числа A и B:
# Выяснить какакое из них больше не используя не единой операции сравнения

number1 = float(input('Введите число "A": '))
number2 = float(input('Введите число "B": '))
sign = str(number1 - number2)
print(f'A({number1}) > B({number2}) {not bool("-" in sign) and (bool(number1 - number2))}')
print(f'A({number1}) < B({number2}) {bool("-" in sign)}')
print(f'A({number1}) = B({number2}) {not bool(number1 - number2)}')
