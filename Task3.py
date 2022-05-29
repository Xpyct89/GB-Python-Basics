# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
class Cell():
    def __init__(self, value: int):
        if value <= 0:
            raise Exception('Клетка не может не содержать ячеек! ')
        self.value = value

    def __add__(self, other):
        return f'Результат объединения клеток: {self.value + other.value}'

    def __sub__(self, other):
        result = self.value - other.value
        if result > 0:
            return f'Результат вычитания клеток: {result}'
        else:
            raise Exception(f'Ошибка! Вычитание невозможно!')

    def __mul__(self, other):
        return f'Результат умножения клеток: {self.value * other.value}'

    def __truediv__(self, other):
        return f'Результат деления клеток: {self.value // other.value}'

    def make_order(self, row_len: int):
        rows = ['*' * row_len for _ in range(self.value // row_len)]
        row = '*' * (self.value % row_len)
        rows.append(row)
        return '\n'.join(rows)


my_cell1 = Cell(15)
my_cell2 = Cell(5)
print(my_cell1 + my_cell2)
print(my_cell1 - my_cell2)
print(my_cell1 * my_cell2)
print(my_cell1 / my_cell2)
print(my_cell1.make_order(5))
