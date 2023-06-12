#Сортировка элементов.
'''
Сортировки в Python используются для упорядочивания элементов в списке и других коллекциях
'''

#Сортировка пузырьком (Bubble Sort)
'''
Сортировка пузырьком (Bubble Sort) - это простой алгоритм, который проходит по списку несколько раз,
сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке.


def BubbleSort(list_el):
    length = len(list_el)
    for i in range(length):
       for j in range(length-i-1):
           if list_el[j]>list_el[j+1]:
               list_el[j],list_el[j+1]=list_el[j+1],list_el[j]

    return list_el

sequence = [8,5,2,4,9,7,1,0]
sequence = BubbleSort(sequence)
print(sequence)
'''

#Линейный поиск
'''
Линейный поиск - это простой алгоритм поиска элемента в списке.
Он проходится по всем элементам списка по очереди, пока не найдет нужный элемент.
Реализация может выглядеть так:

def LinearSearch(list_el,target):
    for i in range(len(list_el)):
        if list_el[i]==target:
            return i

sequence = [8,5,2,4,9,7,1,0]
print(LinearSearch(sequence,7))

'''

#Binary Search
'''
 Бинарный поиск -  это алгоритм поиска элемента в отсортированном списке.
 Он работает путем деления списка на половины и проверки целевого значения в каждой половине.
 Если значение присутствует в списке, алгоритм вернет его индекс, в противном случае вернет -1
 
 def BinarySearch(list_el,target):
    lower = 0
    upper = len(list_el)-1

    while lower<=upper:
        middle_index = (lower+upper)//2
        if list_el[middle_index]==target:
            return f'Element {list_el[middle_index]} is in {middle_index} index'
        elif list_el[middle_index]<target:
            lower = middle_index+1
        elif list_el[middle_index]>target:
            upper = middle_index-1
        else:
            return -1

sequence = [8,5,2,4,9,7,1,0]
print(BinarySearch(sorted(sequence),5))

'''


#Practise
'''
Написать функцию, которая принимает параметр reverse и если он равен True 
то функция отсортирует список в обратном порядке
в противном случае по возрастанию

def BubbleSort(list_el,reverse):
    length = len(list_el)
    for i in range(length):
       for j in range(length-i-1):
           if list_el[j]>list_el[j+1]:
               list_el[j],list_el[j+1]=list_el[j+1],list_el[j]
    if reverse:
        return list_el[::-1]
    else:
        return list_el

sequence = [8,5,2,4,9,7,1,0]
sequence = BubbleSort(sequence,reverse = True)
print(sequence)
'''


#Collections
'''
list - ссылочный тип данных , хранящий набор элементов
tuple(кортеж) - неизменяемый список 
set(множество) - набор УНИКАЛЬНЫХ элементов
|
--->frozenset(замороженное множество) - неизменяемый набор Уникальных элементов
dictionary(словарь) - набор элементов хранящий пары (ключ и значение)
'''

tuple_el = ([12,3,344],'Hello',True,2,3,45,6)
tuple_el_1 = 1,2,3,45,6
tuple_new = tuple(i for i in tuple_el_1)
print(tuple_new)
print(tuple_el[::-1])
