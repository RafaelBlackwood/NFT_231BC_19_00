#Понятие классического массива.Понятие коллекции объектов.
'''
Массив - это структура данных, состоящая из набора элементов (значений или переменных),
каждый из которых идентифицируется по крайней мере одним индексом или ключом массива.

Коллекция - структура объектов с динамически изменяющейся
размерностью массивы следует применять там, где
будет строго фиксированное оличество элементов;
если предполагается изменение количества
элементов, следует применять коллекции.

две области в оперативной памяти — стек(stack)
и кучу(heap).

Stack:
Стек используется для статичного выделения памяти.
Heap:
Куча используется для динамического выделения памяти

'''


#Ссылочный тип данных list.
'''
Ссылочными типами называются такие, для которых в ячейке памяти 
(ссылочной переменной) содержатся не сами данные,
 а только адреса этих данных, то есть ссылки на данные.
 
List - это ссылачный тип данных, способный хранить
некоторый набор разнатипных данных.
'''

#Создание списков.
'''
list_elements = [12,True,2.5,'Hello world']
print(list_elements)
list_el = [] #объявили пустой список
print(list_el)
second_list = list()
third_list = list('Hello')
print(second_list)
'''

#Работа со списками.Особенности списков, ссылки и клонирование.Оператор принадлежности in.
'''
#Сравнение списков
#Получение части списка
#Обращение к элементам списка
#Разложение списка

people = ["Tom", "Bob", "Sam"]
tom, bob, sam = people
'''
'''
list_el = ['Khinkhali',1,2.5,False]
#print(list_el[0][-1][0])
second_list = [1,10,True,30.1]
#print(list_el==second_list)
#print(list_el>=second_list)#Error
third_list = [2,9,False,22.5]
print(second_list>third_list)
print(second_list<third_list)
forth_list = ['Hachapuri',1,2.9,False]
print(list_el>forth_list)


list_el = [123,6543,'Hello', True,123,7887,12]
for i in range(len(list_el)):#range(4)
    print(i)

print(list_el[0:5:2])
print(list_el[::-1])

new_list=[11,22,33]
first,third= new_list
print(first,third)


list_el = [1,2,3,4,5,66]

summ = 0
for i in list_el:
    summ+=i

print(summ)

'''

#Методы списков.
#https://pythontutor.com/visualize.html#mode=display
'''
append(item): добавляет элемент item в конец списка
list_el.append()

insert(index, item): добавляет элемент item в список по индексу index
list_el.insert(2, 'Python')

extend(items): добавляет набор элементов items в конец списка
list_new = [12,23,5,233,46,'hello']
list_el.extend(list_new)

remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
list_el.remove('hello')

clear(): удаление всех элементов из списка
list_el.clear()

pop(index): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
a = list_el.pop(8)

index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
print(list_el.index(' '))

count(item): возвращает количество вхождений элемента item в список
print(list_el.count(1))

sort(reverse = False,key): сортирует элементы.
Optional. reverse=True отсортирует в обратном порядке. По умолчанию reverse=False(по возростаниө)
Optional. key - функцию сортировки.

people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort()
people = ["Tom", "Alina", "bob", "alice", "Sam", "Bill" ]
people.sort(key=str.lower)

reverse(): расставляет все элементы в списке в обратном порядке

copy(): копирует список


'''

'''
str_el = 'Hello this world full of cool food'
list_el = str_el.split(' ')
print(list_el)

list_el = [1,1,1,1,123,123,123]


list_el.sort(reverse=False)
print(list_el)


people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
print(people)

list_names = people
list_names.append('11212')
print(list_names)
print(people)
new_list = people.copy()
new_list.append('c# one love')
print(new_list)
print(people)

'''

#Practise
'''
В списке целых, заполненном случайными числами 
вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и 
максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами.
'''
'''from random import *

list_el = [randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100),randint(-100,100)]
min_el = 0
max_el = 0
for i in range(len(list_el)):#range(5)
    print(list_el[i])#list_el[0],list_el[1],list_el[2],list_el[3],list_el[4]
    if min_el>=list_el[i]:
        min_el = list_el[i]
    if max_el<=list_el[i]:
        max_el= list_el[i]

print(f'Min = {min_el} and Max = {max_el}')'''


#Генераторы списков.

#Поиск элемента.

#Матрицы.

