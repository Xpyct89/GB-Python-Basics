# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    return (a + b + c) - min(a, b, c)
print(my_func(int(input('Введите первое число ')), int(input('Введите второе число ')), int(input('Введите третье число '))))