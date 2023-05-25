#Кодировка ASCII, Unicode, UTF-8, Byte-code.
'''ASCII (American Standard Code for Information Interchange) - это одна из самых старых и широко используемых кодировок. Она представляет каждый символ
(буквы верхнего и нижнего регистров, цифры и специальные символы) в виде 7-битного числа (0-127).

 Unicode - это стандарт, который предназначен для представления символов из всех письменных систем мира.
 Он расширяет ASCII и использует более широкий диапазон кодов для представления символов. Unicode может быть реализован различными способами кодирования, такими как UTF-8, UTF-16 и UTF-32.

UTF-8 (Unicode Transformation Format 8-bit) - это переменной длины кодировка Unicode, которая использует от 1 до 4 байтов для представления символов.
Она позволяет представлять все символы Unicode и обеспечивает обратную совместимость с ASCII.

Byte-code: Byte-code - это формат, в котором некоторые языки программирования (например, Python) компилируют свой исходный код в промежуточный код,
который затем выполняется виртуальной машиной. Byte-code обычно является платформо-независимым и может быть выполнен на разных операционных системах и архитектурах.
Промежуточный код (Intermediate code) - это форма представления программы или исходного кода, которая обычно создается в процессе компиляции программы.
 ASCII ограничен по количеству символов и не поддерживает многие символы из других письменных систем.
 Unicode и его различные кодировки, такие как UTF-8, позволяют представлять широкий набор символов, но требуют большего объема памяти для хранения символов с большими кодовыми значениями.

В Python, строки по умолчанию представлены в формате Unicode (обычно в кодировке UTF-8), что позволяет работать с текстом на разных языках и использовать различные символы
'''

#String. Особенности работы со строками.
'''
Строки - это неизменяемый тип данных.

str_el = 'hello world'
str_el_2= input()
str_el[3]= 'G'#Error!
print(str_el[1],str_el[-5])
for i in str_el:
    print(i)
print(type(str_el))

str_el = 'Khinkhali'
str_el_2 = 'adjika'
str_el_3 = str_el + ' ' + str_el_2
print(str_el_3)

print(str_el_3*5)


#str_el = '12'
#str_el = 'hello'
str_el = '5.6'
#element = int(str_el)
#element = int(str_el)
element = float(str_el)
print(element)
print(type(element))


str_el = 'hello'
for i in range(5):
    print(str_el[i])

'''


#Срез строки.
'''
string[:end]: начиная с 0-го индекса по индекс end

string[start:end]:  начиная с индекса start по индекс end 

string[start:end:step]: начиная с индекса start по индекс end через шаг step

food = 'The best food in the world is Khinkhali'
print(food[0:10])
print(food[:10])
print(food[5:10])
print(food[::2])
print(food[1:20:10])
print(str_el[0:])
'''

#Practise:
'''
Задание 1.
Пользователь вводит с клавиатуры строку. 
Произведите поворот строк и полученный результат выведите 
на экран

str_el = input()
print(str_el[::-1])

Задание 2.
Пользователь вводит с клавиатуры строку и символ 
для поиска. Посчитайте сколько раз в строке встречается 
искомый символ. Полученное число выведите на экран.
word = input()
element = input()
count=0
for i in word:
    if element in i:
        count+=1

print(count)

Задание 3.
Пользователь вводит с клавиатуры строку и число(инт) 
для поиска. Посчитайте сколько раз в строке встречается 
искомый число. Полученное число выведите на экран.
word = input()
element = int(input())
count=0
for i in word:
    if i in str(element):
        count+=1
print(count)

'''

#Методы строк.
'''
isalpha(): возвращает True, если строка состоит только из алфавитных символов
islower(): возвращает True, если строка состоит только из символов в нижнем регистре
isupper(): возвращает True, если все символы строки в верхнем регистр
isdigit(): возвращает True, если все символы строки - цифры

lower(): переводит строку в нижний регистр
upper(): переводит строку в вехний регистр
title(): начальные символы всех слов в строке переводятся в верхний регистр
capitalize(): переводит в верхний регистр первую букву только самого первого слова строки

lstrip(): удаляет начальные пробелы из строки
rstrip(): удаляет конечные пробелы из строки
strip(): удаляет начальные и конечные пробелы из строки

find(): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
replace(): заменяет в строке одну подстроку на другую
split(): разбивает строку на подстроки в зависимости от разделителя
join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
len(): определяет длину строки.
count(element): возвращает количество какого-то элемента в строке

str_el = 'hello world !!!!!!!!!!!!!!!!!!!'
str_el2 = 'hello world'

print(str_el.isalpha())
print(str_el.islower())

a = str_el.upper()
print(a)
print(str_el)
b = a.lower()
print(b)
print(a)
print(str_el.title())
print(str_el.capitalize())

print(str_el.strip())
print(str_el.count('ll'))

element  = '!!!!'
print(str_el.find(element))

c = str_el.replace('hello','Khinkhali')
print(c)

list_el = str_el.split()
print(list_el)

food = 'Ayran'
v = food.join(str_el)
print(v)

print(len(str_el))

for i in range(len(str_el)):
    print(str_el[i])

'''

#Экранированные последовательности.

#«Сырые строки».

#Форматированный вывод.

#Модуль string.

#Байты и кодировки.








