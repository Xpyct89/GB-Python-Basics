# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


    def divider(a, b):
        if b == 0:
            raise DivisionByZeroError('Ошибка при делении на ноль!')
        return a / b


try:
    DivisionByZeroError.divider(15, 0)
except DivisionByZeroError as e:
    print(e)
print(round(DivisionByZeroError.divider(18, 6)))
