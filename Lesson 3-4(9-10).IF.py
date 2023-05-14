#Condition operators
'''
> - больше
>= - больше и равно
< - меньше
<= - меньше и равно
== - равно ли?
!= - не равно ли?

num = 10
num_2 = 5
print(num == 10)#True
print(num == 11)#False
print(num != 11)#True
print(num > 11)#False
print(num >= 11)#False
print(num < 10)#False
print(num <= 10)#True
print(num > 10)#False
print(num >= 10)#True

bool_el_1 = True
bool_el_2 = False

print(bool_el_1 > bool_el_2)#True
print(bool_el_1 >= bool_el_2)#True

string_el_1 = "HELLO"
string_el_2 = 'HELLO'

print(string_el_1 == string_el_2) #False
print(string_el_1 >= string_el_2) #False
print(string_el_1 < string_el_2) #True
'''

#Logic operators
'''
and - и
or - или
not - не
in - в

num_1 = 12
num_2 = 10
num_3 = 6
a = num_1 > num_2 and num_1< num_3

print(num_1 == num_2 == num_3)
print(num_1 > num_2 and num_1< num_3)#False
print(num_1 > num_2 and num_1> num_3)#True
print(num_1 > 10 and num_3<num_1 or  num_2<num_1 and num_2>num_3)#True
print(a)#False
print(not num_1>num_2)#True

str_1 = 'Lambo'
str_2 = 'My favorite car is Lambo'
print(str_1 in str_2)

logic = 0 and 180>=0
print(logic)#0
'''


# condition constructions(if else/ if elif else)
'''
if условие:#Условие должно быть True чтобы выполнились инструкции этого условия
    инструкции(тело условия)
else:
    инструкции которые выполнятся если условие не сработало
'''

'''
num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))

#Проверяться все IF даже если одно из условий уже было True
if num_1>num_2:
    print('First is greater than second')
if num_1==num_2:
    print('Hakunana matata')
else:
    print('Second is greater than first')

# В случае с elif ,как только одно из условий True другие условия проверяться не будут
if num_1!= num_2:
    print(num_1)
elif num_1<num_2:
    print(num_2)
elif num_1:
    ...
else:
    print('я пошел спать')
'''

#Practice
'''
Task 1.
Вводятся 3 числа. Выведите на экран наибольшее из них и наименьшее из них


Task 2.
Вводятся два числа. Если они четные то найти их сумму, если они оба не четные то найти их разность,
если первое четное только, найти их произведение и если второе только четное, найти их деление.
 
Task 3.
Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
В зависимости от выбора пользователя посчитать, сколько часов, минут и секунд 
осталось до полуночи

Task 4. 
Пользователь вводит с клавиатуры диаметр окружности.
В зависимости от выбора пользователя посчитать площадь или периметр окружности

Task 5.
Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность.
Если число  четное требуется вывести на экран число и надпись Even number.
Если число нечетное выведите на экран число и надпись Odd number. 

Task 6. 
аписать программу, которая по выбору пользователя возводит
 введенное им число в степень от нулевой до седьмой включительно.

Task 7.
Пользователь вводит с клавиатуры номер дня недели 
(1-7). Необходимо вывести на экран названия дня недели.
Например, если 1, то на экране надпись понедельник, 
2 — вторник и т.д.

Task 8. 
ользователь вводит с клавиатуры количество метров.
В зависимости от выбора пользователя программа 
переводит метры в мили, дюймы или ярды.

Task 9.
Пользователь вводит с клавиатуры три числа.
 В зависимости от выбора пользователя программа выводит 
на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

Task 10. 
Пользователь с клавиатуры вводит количество часов. 
Если полученное значение находится в диапазоне от 0 до 
6 нужно вывести надпись Good Night, если в диапазоне от 
6 до 13 Good Morning, если в диапазоне от 13 до 17 Good 
Day, если в диапазоне от 17 до 0 Good Evening. Верхняя 
граница диапазона не включается. Например, число 6 
относится к 6 до 13
'''

#Task 1.
'''num_1 = int(input())#5
num_2 = int(input())#10
num_3 = int(input())#7

if num_1>num_2 and num_1>num_3:
    print('number 1 is greater')
    if num_2>num_3:
        print('number 3 is the smallest')
    else:
        print('number 2 is the smallest')
elif num_2>num_1 and num_2>num_3:
    print('number 2 is greater')
    if num_1>num_3:
        print('number 3 is the smallest')
    else:
        print('number 1 is the smallest')
else:
    print('number 3 is greater')
    if num_2>num_1:
        print('number 1 is the smallest')
    else:
        print('number 2 is the smallest')
'''
