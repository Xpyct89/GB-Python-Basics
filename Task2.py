# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
def func (name, surname, birth, city, email, phone):
    return dict(Имя=name, Фамилия=surname, Год=birth, Город=city, Почта=email, Телефон=phone)
print(func(name=input('Имя '), surname=input('Фамилия '), birth=int(input('Год рождения ')), city=input('Город '), email=input('Почта '), phone=int(input('Телефон '))))