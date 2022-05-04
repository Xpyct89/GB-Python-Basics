# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
value = (input('Введите число для задачи ')) # Запрашиваю число
result = int(value) + int(value + value) + int(value + value + value) # Получаю результат
print(f'{value} + {value}{value} + {value}{value}{value} = {result}') # Вывожу данные на экран