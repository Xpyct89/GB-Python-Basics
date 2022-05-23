# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open('task2.txt', 'r') as my_f:
    lines = my_f.readlines()
    print(f'Количество строк составляет {len(lines)}')
    my_f.seek(0)
    for i in range(len(lines)):
        line = my_f.readline()
        words = line.split()
        print(f'количество слов в {i + 1} строке {len(words)}')
