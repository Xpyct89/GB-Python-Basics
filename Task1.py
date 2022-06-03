# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extraction(cls, self):
        day = int(self.date[0:2])
        month = int(self.date[3:5])
        year = int(self.date[6:10])
        return Date.validation(day, month, year)

    @staticmethod
    def validation(day, month, year):
        if 0 < day < 32:
            if 0 < month < 13:
                if 0 < year <= 2022:
                    return f'День {day} Месяц {month} Год {year}'


my_date = Date('01-06-2022')
print(Date.extraction(my_date))
