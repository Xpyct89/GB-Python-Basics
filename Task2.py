# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_value = int(input('Введите количество секунд ')) # Пользователь задает количество секунд
hours = time_value // 3600 # Получаем количество часов
minutes = (time_value - hours * 3600) // 60 # Получаем количество минут
seconds = time_value - (hours * 3600 + minutes * 60) # Получаем оставшееся количество секунд
print(f'Введенное количество секунд, равно {hours}:{minutes}:{seconds} (чч:мм:сс).') # Вывод значения на экран