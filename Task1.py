# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def __str__(self):
        result = []
        for line in self.my_list:
            result.append(' '.join([str(i) for i in line]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            result = []
            for i, line in enumerate(self.my_list):
                new_list = list(map(lambda x, y: x + y, line, other.my_list[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return


first_list = [[3, 5, 32], [2, 4, 6], [1, 64, 8]]
second_list = [[6, 10, 64], [4, 8, 12], [2, 128, 16]]
matrix1 = Matrix(first_list)
matrix2 = Matrix(second_list)
matrix_new = matrix1 + matrix2
print(f'{matrix1}''\n')
print(f'{matrix2}''\n')
print(f'{matrix_new}''\n')
