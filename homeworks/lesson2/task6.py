"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

count = 0

while True:
    count = input('Enter items count ')
    if count.isnumeric():
        count = int(count)
        break
    else:
        print('Please enter valid count')

meta = {
    'name': str,
    'price': int,
    'count': int,
    'unit': str
}

items = []

for num in range(1, count + 1):
    item = {}
    print(f'Entering values for item {num}')
    for key, value_type in meta.items():
        while True:
            value = input(f'Enter {key} ')
            # using try block it can be written more concisely: use type as converter,
            # otherwise catch exception with message
            if value_type is int and value.isnumeric():
                item[key] = int(value)
                break
            elif value_type is str:
                item[key] = value
                break
            else:
                print('Please enter valid value')
    items.append(item)

analytics = {}

for idx, item in enumerate(items):
    for key, value in item.items():
        if key not in analytics:
            analytics[key] = set()
        analytics[key].add(value)

print('Result:')
print(analytics)
