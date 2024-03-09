"""Модуль для отработки учебного кода"""
# temp_2.py


def aver(*args):
    """F"""
    return (sum(element for element in args)) / len(args) if args else 0


print(aver(2, 8))
