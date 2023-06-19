# Понятие ООП.
'''
Конкретным воплощением класса является объект.

Классы-Класс предназначен для описания некоторого типа объектов
Класс может определять переменные и константы для хранения состояния
 объекта и методы(функции) для определения поведения объекта.
 Переменные которые хранятся в классе мы будем называть полями,а функции внутри классa методами

Syntaxix:
class name_of_the_class:
    #methods
    #attributes

object = name_of_the_class()


#Особенности реализации ООП в Python, «утиная типизация».

Утиная типизация – это концепция, характерная для языков программирования с
 динамической типизацией(А это значит, что переменная не привязана жестко k определенному типу)
 согласно которой конкретный тип или класс объекта не важен, а важны лишь свойства и методы,
 которыми этот объект обладает

Экземпляр класса.
Экземпляр класса - переменная представитель класса, которая присваивает ее класс и работающая от его имени.
(Если класс является планом, то экземпляр – это объект, который построен по этому плану.)

Атрибуты или поля (свойства), методы класса.
Атрибут/Поле/Свойство - Это переменная, существующая внутри объекта этого класса
и содержащая в себе значение, отражающее некоторое свойство этого объекта.

методы (функции-члены) класса – это функции, описывающие, что умеют делать объекты класса.


self – общепринятое имя для ссылки на объект,
 в контексте которого вызывается метод.
 Этот параметр обязателен и отличает метод класса от обычной функции.

Конструктор - это специальный метод классов, который выступает в качестве
метода который вызывается автоматически, как только создается  класса.
Обычно используется для инциализации разного рода полей.объект
def __init__(self):

Деструктор - это специальный метод классов, который выступает в качестве
метода который вызывается автоматически, как только завершается работа класса.
Обычно используется для удалению данных(освобождении памяти)
def __del__(self):

Перегрузка методов.
Если два или более метода имеют одинаковые имена,
но разное количество параметров или разные типы параметров, или и то, и другое,
то это называется перегрузкой методов.

Python является динамически типизированным языком и следовательно,
перегрузка методов здесь невозможна, тем не менее,
есть простой способ реализовать такое поведение в Python.

'''

'''
Magic-методы
В Python имена методов, которые имеют ведущее и последующее двойное подчеркивание - называют магическими методами
Эти методы известны как dunder методы("Double Under (Underscores)")

https://habr.com/ru/post/186608/

'''

# example. Dice game
'''
from random import randint

class Dice:
    def __init__(self,sides = 4):
        self.dice_sides = sides

    def __str__(self):
        return f'Dice with {self.dice_sides} sides'

    def __len__(self):
        return self.dice_sides

    def __eq__(self, other):
        return self.roll() == other.roll()

    def __ne__(self, other):
        return self.roll != other.roll()

    def __lt__(self, other):
        return self.roll() < other.roll()

    def __le__(self, other):
        return self.roll() <= other.roll()

    def __gt__(self, other):
        return self.roll() > other.roll()

    def __ge__(self, other):
        return self.roll() >= other.roll()

    def __add__(self, other):
       return Dice(self.dice_sides + other.dice_sides)


    def __sub__(self, other):
        return Dice(self.dice_sides - other.dice_sides)

    def roll(self):
        return randint(1,self.dice_sides+1)

    def __del__(self):
        del self.dice_sides

d4 = Dice()
d12 = Dice(12)

print(d4)
print(d12)

print(len(d12))

d16 = d4 + d12
d8 = d12 - d4

print(d16 > d8)
print(d16 < d12)
print(d16 >= d4)
print(d12 != d4)
print(d12 <= d4)


print(d16)
print(d12)
print(type(d16))
print(type(d12))
'''

# Practise:
'''
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО, дату рождения,
 контактный телефон, город, страну, домашний адрес.
  Реализуйте методы класса для ввода данных, вывода данных.
'''

'''

class Teacher:
    def __init__(self,name,surname,age,subject):
        self.teacher_name = name
        self.teacher_surname = surname
        self.teacher_age = age
        self.teacher_subject = subject

    def print_info(self):
        return f'{self.teacher_name} {self.teacher_surname} is under {self.teacher_age} and he is teaching {self.teacher_subject}'

    def __del__(self):
        del self.teacher_subject
        del self.teacher_name
        del self.teacher_surname
        del self.teacher_age

name = input()
surname = input()
teacher = Teacher(name,surname,21, 'Python')
print(teacher)


print(teacher.print_info())
'''
