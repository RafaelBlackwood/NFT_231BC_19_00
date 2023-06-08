# Организация функций
'''
def main():
    say_hello()
    say_goodbye()

def say_hello():
    print("Hello")

def say_goodbye():
    print("Good Bye")

# Вызов функции main
main()


def main():
    choice = int(input('Choose the option:\n1.Math func\n2.Students list'))
    if choice==1:
        number=int(input())
        math(number)
    elif choice==2:
        stud_list = ['Hasan','Samir','Amil']
        students(stud_list)


def math(number_1):
    if number_1%2==0:
        print('Even number')
    else:
        print('odd number')

def students(list_el):
    for i in list_el:
        print(f'Students in the class {i}')

main()
'''

#	Распаковка и упаковка аргументов.
'''
Распаковка 
Мы можем использовать * для распаковки списка, чтобы все его элементы можно было передавать как разные параметры.

Упаковка 
Когда мы не знаем, сколько аргументов нужно передать функции


#Распаковка
def calc(a,b,c,d,e):
    return a+b+c+d+e

list_el = [11,22,33,44,55]
print(calc(*list_el))

#Упаковка

def calc(*args):
    summ=0
    for i in args:
        summ+=i
     
    print(summ)
    print(type(args))

calc(1,2,3,4,4,45,5,5,344,124,141,341324,134,1234,1234,1324)
calc(1,2,3,4,4,45,5,5)
calc(1,2,3)
calc(1,2,3,22222222)
calc(1,2,3,5435235,1423)
'''

#	Аргументы по умолчанию, аргументы-ключи.
'''
def user(name,fathers_name,surname = 'Aliyev'):
    
    return f'Hello mr\\mrs {fathers_name} {name} {surname}'

print(user('Ali','Qosa'))
'''


#	Область видимости, правило LEGB.
'''
ОБЛАСТЬ ВИДИМОСТИ
LEGB
Интерпретатор начинает поиски имени изнутри, последовательно переходя от локальной 
области видимости к объемлющей, затем к глобальной и в завершении к встроенной.

Local -> Enclosed -> Global -> Built-in
def foo():
    name ='Raf' #local

print(name)#Error

Local - inside fun-s. Удаляется, когда функция или блок кода завершают свое выполнение.

Global - free space

Enclosed - подобная область видимости относится к переменным которые созданы в функция, которые были созданы внутри других
функций lambda(частный пример)

def user():
    global name
    name = 'Ronaldo'
    def print_info():
        print(f'Hello {name}')

    return print_info()

Built-in - все встроенные по типу pi, punctuation, and etc.


'''






#	Локальные и глобальные переменные в функциях.
'''
global название переменной

nonlocal 
Имена, перечисленные в инструкции nonlocal, в отличие от тех, что перечислены в инструкции global,
должны ссылаться на ранее существовавшие переменные в охватывающей области.



name= 'Messi'
def user():
    global name
    name = 'Ronaldo'

    print(f'Hello {name}')

a = user()
print(name)




def user():
    num = 1
    def calc():
        nonlocal num
        num+=10
        print(num)

a = user()
'''

#	Функции как объекты первого класса.
'''
Это означает, что функции можно передавать и использовать в качестве аргументов, 
как и любой другой объект(string, int, float, list и т.Д.).

Особенности функций как объектов первого класса:

Функции можно присваивать переменным.
Функцию можно вернуть из функции.
У функций те же свойства и методы, что и у объектов(OOП).
Функцию можно передать в качестве аргумента при вызове другой функции.

def math(number_1,number_2):
    return number_1+number_2


def func(function,num_1,num_2):
    return function(num_1,num_2)    

number_1=10
number_2=10

print(func(math(number_2,number_1),number_2,number_1))
'''

#	Рекурсия.
''' 
#Рекурсивная функция - та функция, что вызывает саму же себя.
Ограничение на вызов рекурсии = 996


def fact(num):
    if num == 1:
        return 1

    return num* fact(num-1)

print(fact(5))
'''


#Practise
'''
1.Реализовать рекурсивную функцию возведения элементов в степень. 
Функция принимает два параметра х и у.
Функция должна вернуть реузльтат в виде возведения чисел от 1 до х в степень у.

2. Реализовать рекурсивную функцию для нахождения последовательности Фибоначчи.
Функция принимает один параметр, она должна вернуть результат конечной суммы.
Последовательность Фиббоначи -элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,…
в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Подсказка:
Если число равно 0, то возвращаем 0
Если число равно 1, то возвращаем 1
В ином случае возвращаем рекурсию в виде сумме двух предыдущих чисел'''