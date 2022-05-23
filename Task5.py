# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open('task5.txt', 'w', encoding='UTF-8') as f:
    import random

    rand_list = [str(random.randint(1, 10)) for _ in range(10)]
    my_str = ' '.join(rand_list)
    f.write(my_str)
with open('task5.txt', 'r', encoding='UTF-8') as f2:
    values = f2.read().split()
    print(f'Сумма значений в файле равна {sum(map(int, values))}')
