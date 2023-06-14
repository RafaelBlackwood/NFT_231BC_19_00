# Tuple(кортеж)
'''
Кортеж (tuple) представляет последовательность элементов,
 которая во многом похожа на список за тем исключением,
 что кортеж является неизменяемым (immutable) типом.
Мы не можем добавлять или удалять элементы в кортеже, изменять его.


Кортеж очень часто используется для защиты хранимых данных приложения от незапланированных или непреднамеренных изменений.
Кортеж также требует выделения значительно меньшего количества памяти.

'''


# Set(множество)
'''
Set(множество) представляют очередной вид набора элементов, который хранит только уникальные элементы.
names = {"Raf", "Ne Raf", "Raf", "Rafael"}
print(names)
print(type(names))

add() -	Добавляет элемент в набор
clear() -	Удаляет все элементы из набора
copy() - Возвращает копию набора
difference() -	Возвращает набор, содержащий разницу между двумя или более наборами
difference_update() -	Удаляет элементы в этом наборе, которые также входят в другой указанный набор
intersection() -	Возвращает набор, являющийся пересечением двух других наборов
intersection_update() -	Удаляет элементы в этом наборе, которых нет в других указанных наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)
z = x.difference_update(y)
print(z)
z = x.intersection(y)
print(z)
x.intersection_update(y)
print(x)

discard() -	Удалить указанный элемент
remove() -	Удалить указанный элемент
pop() - Удаляет и возвращает произвольный элемент набора.
isdisjoint() -	Возвращает, имеют ли два набора пересечение или нет
issubset() -	Возвращает, содержит ли другой набор этот набор или нет
issuperset() -	Возвращает, содержит ли этот набор другой набор или нет

union() -	Вернуть объединение наборов как новый набор.
update() -	Обновить набор с объединением себя и других
'''


# Frozen set
'''
Frozen set является видом множеств, которое не может быть изменено.
В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся.
names = frozenset({"Rafael", "Tengiz", "Orhan"})
'''


# Dictionary(словарь)
'''
Словарь (dictionary) тип данных который хранит коллекцию элементов,
 где каждый элемент имеет уникальный ключ и некоторое значение,которое хранится за ключом.

#Синтаксис:
dictionary = { ключ1:значение1, ключ2:значение2, ....}
Ключом может быть int, string,float ,tuple,frozenset(все хешируемые типы данных)  (не может быть дубликатов ключей)
Значением могут быть -  int,str,float,bool and other collections (могут быть дубликаты значений)

#Комлпексные словари
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}

#Преобразований списков/кортежей в словари и добавление элементов вручную:


#Loops in Dictionaries

#Dictionary methods
clear()	Удаляет все элементы из словаря
copy()	Возвращает копию словаря
fromkeys() Возвращает словарь с указанными ключами и значением
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

get()	Возвращает значение указанного ключа
items()	Возвращает список, содержащий кортеж для каждой пары ключ-значение.
for key,value in dict.items():
    print(x,y)

keys()	Возвращает список, содержащий ключи словаря
values()	Возвращает список всех значений в словаре
pop()	Удаляет элемент с указанным ключом
popitem()	Удаляет последний элемент
setdefault()	Возвращает значение указанного ключа. Если ключ не существует: вставьте ключ с указанным значением
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

update()	Обновляет словарь указанными парами ключ-значение.
car.update({"color": "White"})

'''


'''set_el = {True,1,2,3,'Hello',(1,2,3),1,2,3,'hello','Hello'}
print(set_el)
print(set_el)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)
print(z)


# x.difference_update(y)
# print(x)

z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)


x.discard('ape')
print(x)

z = x.union(y)
print(z)

x.update(y)
print(x)

for i in x:
    print(i)

names = frozenset({"Rafael", "Tengiz", "Orhan"})
print(*names)

'''

'''
dict_el = {1 : [0,1,2,3,44], 'Rafael':"+994558392341" ,(1,2,3):'Tortik',frozenset({1,2,3}):'Khinkhali'}
print(dict_el[frozenset({1,2,3})])
print(dict_el[1])


dict_cars = {
   'Bentli':{
       'motor':4.5,
       'price':300000,
       'Model':'GT'
   } ,
    'BMW':{
        'motor': 4.4,
        'price': 100000,
        'Model': 'M5'

    }
}

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Tom1": {
        "phone": "+1231441414",
        "email": "tom1Khinkhalnaya@gmail.com"
    }

}

users['Tom']['phone'] = '-12314151'

print(users['Tom'])

for i in dict_cars:
    print(i)


x = ('key1', 'key2', 'key3')
y = [1,2,3]
thisdict = dict.fromkeys(x, y)
print(thisdict)

print(dict_cars.get('BMW'))



dict_el = {'Raf':21,'Gasan':14,'Samir':24}

for key,value in dict_el.items():
    print(key,value)
print(dict_el.items())

for key in dict_el.keys():
    print(key)

for value in dict_el.values():
    print(value)



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("modellll",'Bronco')
print(x)
car.update({"color": "White"})
print(car)
'''


'''
Создайте программу «Англо-Русский словарь».
Нужно хранить слово на английском языке и его перевод
на русском. Требуется реализовать возможность добавления,
удаления, поиска, замены данных в словаре. Используйте
словарь для хранения информации.
'''
'''
# Создаем пустой словарь
dictionary = {}

# Определяем функцию для добавления новых слов
def add_word():
    pass
# Определяем функцию для удаления слов
def remove_word():
    pass

# Определяем функцию для поиска слов
def search_word():
    pass

# Определяем функцию для замены перевода слова
def replace_word():
    pass

# Определяем функцию main c бесконечным циклом для взаимодействия с пользователем (menu)
def main():
    pass
'''
'''

dictionary = {}

def main():
    while True:
        choice = int(input('\nChoose operation:\n'
                       '1. Add element to the dictionary\n'
                       '2. Remove element from the dictionary\n'
                       '3. Find element at the dictionary\n'
                       '4. Replace element at the dictionary\n'
                       '5. Print dictionary\n'
                       '6. Exit\n'))

        if choice==1:
            add_element()
        elif choice==2:
            delete_element()
        elif choice==3:
            find_element()
        elif choice==4:
            replace_element()
        elif choice==5:
            print_dictionary()
        elif choice==6:
            return -1


def add_element():
    eng_word = input('Write the word in English: ')
    rus_word = input('Write the translation of this word: ')

    dictionary[eng_word] = rus_word

    print(f'Word {eng_word} has defenition in russian = {dictionary[eng_word]}')

def delete_element():
    eng_word = input('Write the word in English that you want to remove: ')

    del dictionary[eng_word]

    print(f'Word {eng_word} was deleted from the dictionary')


def find_element():
    eng_word = input('Write the word in English: ')

    if eng_word in dictionary:
        print(f'Word {eng_word} was found in dictionary')
    else:
        print(f'Word {eng_word} was not found in dictionary')



def replace_element():
    eng_word = input('Write the word in English: ')
    new_rus_word = input('Write the translation of this word: ')

    dictionary[eng_word] = new_rus_word

    print(f'Word {eng_word} has changed its defenition on {dictionary[eng_word]}')



def print_dictionary():
    for key,value in dictionary.items():
        print(key,value)



main()

'''


# Practise
'''
Задание 1.
Пользователь вводит с клавиатуры название фрукта.
Необходимо вывести на экран количество раз, сколько
фрукт встречается в кортеже в качестве элемента.

Задание 2.
Добавьте к заданию 1 подсчет количества раз, когда
название фрукта является частью элемента. Например:
banana, apple, bananamango, mango, strawberry-banana.
В примере выше banana встречается три раза.

Задание 3.
Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0
до N раз). Пользователь вводит с клавиатуры название
производителя и слово для замены. Необходимо заменить
в кортеже все элементы с этим названием на слово для
замены. Совпадение по названию должно быть полным.

Задание 4.
Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;
■ Удаления стран;
■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множества

Задание 5.
Существует два множества, содержащие названия
городов. Необходимо создать третье множество: 
■  содержащее названия, которые есть в обоих множествах.
■  содержащее названия, которые есть в первом множестве, но
нет во втором.
■ содержащее названия, которые есть во втором множестве, но
нет в первом.
■ содержащее уникальные названия для каждого множества

Задание 6.
Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.

Задание 7.
Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
название должности, номер кабинета, skype. Требуется
реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
информации.

Задание 8.
Создайте программу «Книжная коллекция». Нужно
хранить информацию о книгах: автор, название книги,
жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
хранения информации.
'''

