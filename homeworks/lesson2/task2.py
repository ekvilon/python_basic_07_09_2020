"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

a_list = []

while (value := input('Enter a next value or hit Enter to finish ')) and value != '':
    a_list.append(value)

for idx in range(1, len(a_list), 2):
    a_list[idx], a_list[idx - 1] = a_list[idx - 1], a_list[idx]

print('Result:', a_list)
