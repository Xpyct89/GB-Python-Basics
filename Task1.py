# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
import random # Импортирую библиотеку рандомных чисел
a = None # a = пустая переменная
b = 3 # Задаю переменную
c = 20 # Задаю переменную
d = random.randint(1,10) # Переменная d = рандомно целому числу от 1 до 10 (без шага)
e = int(input('Пожалуйста, введите число ')) # e = целому числу, что введет пользователь
some_str = input('Введите рыбный текст ') # Переменная строки с рыбным текстом, который введет пользователь
f = b + c # f = 3 + 20 = 23
g = c % b # Остаток от деления 20 на 3
print(f'Переменная F равна {f}') # Вывод на экран текста, с форматированной строкой
print(c / b) # Вывод на экран результата операции
print('Компьютер загадал число {}' .format(d)) # 2й способ форматирования строки
print(some_str) # Напечатать строку, сохраненную в переменной
print(type(e)) # Вывести на экран тип переменной e