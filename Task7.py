# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

my_dict = []
with open('task7.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
    f.seek(0)
    profits = {}
    profit_sum = 0
    for line in f:
        items = line.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    my_dict.append(profits)
    my_dict.append({'average_profit': (profit_sum / len(profits))})
with open('task7.json', 'w', encoding='UTF-8') as jf:
    json.dump(my_dict, jf, ensure_ascii=False)
json_dict = json.dumps(my_dict, ensure_ascii=False)

print(f"Исходный файл:\n{text}\n")
print(f"Список:\n{my_dict}\n")
print(f"json-объект:\n{json_dict}")
