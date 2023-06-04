# List Comprehension - генератор списков
'''
newlist = [expression for item in iterable (if condition)]

Синтаксис list comprehension состоит из следующих компонентов:

iterable: перебираемый источник данных, в качестве которого может выступать список,
 множество, последовательность, либо  функция,
 которая возвращает набор данных, например, range()

item: извлекаемый из источника данных элемент

expression: выражение, которое возвращает некоторое значение. Это значение  попадает в список

condition: условие, которому должны соответствовать извлекаемые из источника данных элементы.
'''

'''list_elements= [-22,33,-44,55,-66,77,-88,99]
new_list = []
for i in list_elements:
    if i>0:
        new_list.append(i)
    print(new_list)


new_second_list = [i*2 for i in list_elements]
print(new_second_list)


new_third_list = [i*2 for i in list_elements if i>0]
print(new_third_list)
from random import *
new_forth_list = [randint(-100,100) for i in range(10)]
print(new_forth_list)
'''

#Nested List. Матрицы.
'''
list_cars = [
             ['BMW',        'm-5 cs',   2023, 4.4],

             ['Rollce Royce', 'Cullina',2022, 4.5],

             ['Porshe', '       Taycan',2022, 200.5],
            ]

print(list_cars[2][1])

for i in list_cars:
    for j in i:
        print(j, end = ' ')
    print()

'''
'''
from random import *

m = int(input('strings'))
n = int(input('columns'))

out_list = []
for i in range(m):
    nested_list = []
    for j in range(n):
        nested_list.append()
    out_list.append(nested_list)

summ = 0
for i in out_list:
    for j in i:
       summ+=j
    print(summ)

list_elements = [[randint(-10,10) for j in range(n)] for i in range(m)]

for i in list_elements:
    for j in i:
       print(j, end= ' ')
    print()
'''

#Practise:
# 1.Вводится двумерный список(список внутри которого еще один список) размера m на n. Его значения заполнены случайными числами.
#   1.1. Найти сумму элементов всех его чисел.
#   1.2. Найти сумму всех положительных.
#   1.3. Найти сумму всех отрицательных.
#   1.4. Найти сумму всех четных.
#   1.5. Найти сумму всех не четных.
#   1.6. Найти сумму всех простых чисел
#   1.7. Определить количество простых чисел в списке.