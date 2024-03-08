"""Модуль для отработки учебного кода"""
# temp.py


def stas_ai_blockchain_calc(operation, first, second):
    """F"""
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '*':
        result = first * second
    elif operation == '/':
        result = first / second
    elif operation == '**':
        result = first ** second
    else:
        return f'Не могу вычислить, операция {operation} не предусмотрена!'
    return result


first = float(input('Введите первый операнд: '))
second = float(input('Введите второй операнд: '))
operation = input('Введите действие (+, -, *, /): ')

print(stas_ai_blockchain_calc(operation, first, second))
