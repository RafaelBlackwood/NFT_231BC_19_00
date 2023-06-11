# Функциональное программирование.
# Что такое функциональное программирование?
'''Функциональное программирование представляет собой методику написания программного
обеспечения, в центре внимания которой находятся функции.
Функции могут присваиваться переменным, они могут передаваться в другие функции и порождать новые функции.

1. Bсе, что можно делать с «данными», можно делать и с функциями
2.Использование рекурсии в качестве основной структуры контроля потока управления.
3. «Чистые функции» функциональные языки избегают побочных эффектов. Это исключает присваивания
4.ФП не одобряет или совершенно запрещает инструкции, используя вместо этого вычисление выражений (т.е. функций с аргументами).
5. ФП акцентируется на том, что должно быть вычислено, а не как.

Чистая Функция — Функция которая является детерминированной и не обладает никакими побочными эффектами.
# детерминирована
def sum(a,b): детерминирована
  return a+b

# не  детерминирована
count = 0
a,b = int(input()),int(input())
if a>b:
    count+=1
else:
    count=0
def sum(a,b):
    global count
    if count==1:
        return a+b
    else:
        return a-b
print(sum(a,b))
'''


# Анонимные функции lambda.
'''
1. (lambda перечисляются аргументы через запятую : что то с ними делается)(передаем аргументы)
2. lambda параметры: выражение

a  = (lambda number_1,number_2: number_1+number_2 if number_1>number_2 else number_2-number_1)(12,24)
print(a)

'''


# Функции высших порядков.
'''
 Эти функции используют в качестве (некоторых) своих параметров другие функции - вот почему мы называем их функциями высшего порядка.
'''

# Функции map(), reduce(), filter(), zip().
# map() - позволяет обрабатывать одну или несколько последовательностей с использованием заданной функции.
'''

list_el = list(map(int, input().split(' ')))
print(list_el)
'''

# reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
'''
from functools import reduce

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])

print(result)

'''

# filter()- определяет нужно ли исключить конкретный элемент из последовательности или нет(если да  то фильтрует последовательность, если нет ничего не делает)
'''
list_el = [1,2,23,3,3,4,54,3]
print(list(filter(lambda number_1: number_1%2==0, list_el)))
'''

# zip()- oбъединяет отдельные элементы из каждой последовательности в итерируемую последовательность
'''
str_1 = 'abcds'
str_2 = 'efghi'

print(list(zip(str_1,str_2)))
'''


#Map
'''def my_map(function,sequence):
    new_list =[]
    for iterator in sequence:
        new_list.append(function(iterator))

    return new_list

list_el = [1,2,3,4,5]
print(my_map(lambda element: element**2,list_el))'''


#Reduce
'''
def my_reduce(function,sequence, initial = 0):
    for iterator in sequence:
        initial = function(initial,iterator)
        #sum+=i => sum= sum+i

    return initial

print(my_reduce(lambda first,second: first+second, list_el))
'''

#Filter
'''
def my_filter(function,sequence):
    new_list =[]
    for iterator in sequence:
        if function(iterator):
            new_list.append(iterator)

    return new_list

list_el = [1,2,3,4,5]
print(my_filter(lambda element: element%2==0,list_el))
'''