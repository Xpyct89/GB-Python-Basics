# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, name: str, color: str, speed: int, is_police: bool):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn_right(self):
        return f'Машина повернула направо'

    def turn_left(self):
        return f'Машина повернула налево'

    def show_speed(self):
        return f'Текущая скорость составляет {self.speed}'


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили разрешенную скорость на {self.speed - 60}'
        else:
            return f'Текущая скорость составляет {self.speed}'


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили разрешенную скорость на {self.speed - 40}'
        else:
            return f'Текущая скорость составляет {self.speed}'


class SportCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = True


toyota = Car('Mark2', 'Black', 140, False)
print(
    f'Машина {toyota.name} цвета {toyota.color}. {toyota.show_speed()}. Утверждение, что это полиция == {toyota.is_police}.')
hyundai = TownCar('Tucson', 'Silver', 79)
print(
    f'Машина {hyundai.name} цвета {hyundai.color}. {hyundai.show_speed()}. Утверждение, что это полиция == {hyundai.is_police}. {hyundai.turn_right()}')
kamaz = WorkCar('Камаз 53501', 'Orange', 39)
print(
    f'Машина {kamaz.name} цвета {kamaz.color}. {kamaz.show_speed()}. Утверждение, что это полиция == {kamaz.is_police}.')
supra = SportCar('Supra', 'Green', 240)
print(
    f'Машина {supra.name} цвета {supra.color}. {supra.show_speed()}. Утверждение, что это полиция == {supra.is_police}. {supra.turn_left()}')
ford = PoliceCar('Crown Victoria', 'White-Blue', 0)
print(f'Машина {ford.name} цвета {ford.color}. {ford.stop()}. Утверждение, что это полиция == {ford.is_police}.')
