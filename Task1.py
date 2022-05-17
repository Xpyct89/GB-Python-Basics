# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script, hours, pay_per_hour, bonus = argv


def calc(hours, pay_per_hour, bonus):
    salary = (float(hours) * float(pay_per_hour)) + float(bonus)
    return print(f'Заработная плата сотрудника составляет: {salary}')


if __name__ == '__main__':
    calc(hours, pay_per_hour, bonus)
