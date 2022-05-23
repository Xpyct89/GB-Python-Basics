# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_list = []
with open('task4en.txt', 'r', encoding='UTF-8') as f_en:
    my_list = f_en.read()
for en, ru in my_dict.items():
    my_list = my_list.replace(en, ru)
with open('task4ru.txt', 'w', encoding='UTF-8') as f_ru:
    f_ru.writelines(my_list)
