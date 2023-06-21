# Статические методы и методы класса.
'''
Статический метод - это метод класса, который связан с классом, а не с его экземплярами.
Он не требует создания экземпляра класса для вызова и может быть вызван напрямую из класса.

В отличие от обычных методов класса, статический метод не получает первым аргументом ссылку
на экземпляр класса self. Вместо этого, он может принимать параметры так же, как и обычная функция.

Статические методы обычно используются для группирования функциональности,
которая связана с классом, но не зависит от состояния его экземпляров.

 Такие методы предваряются аннотацией @staticmethod и относятся в целом к классу

 class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y

print(MyClass.my_static_method(1, 2)) # выведет 3
'''


# Инкапсуляция.
'''
Инкапсуляция в Python - это механизм, который позволяет предотвратить
изменение реализованных данных внутри класса.(сторонее изменения ваших полей)

В Python есть три типа видимости: public, protected и private.

Переменные и функции, объявленные внутри класса и доступные извне, являются публичными (public).


Переменные и функции, объявленные внутри класса с использованием префикса _ (одно нижнее подчеркивание),
 являются защищенными (protected) и доступны только внутри класса и его наследников. 
 Однако, защищенные члены могут быть доступны извне, если к ним обратиться напрямую.
 

 Переменные и функции, объявленные внутри класса с использованием префикса __ (двойное нижнее подчеркивание),
  являются приватными (private) и не доступны извне класса.


class Animal:

    def __init__(self,breed,name):
        #self.breed = breed - public
        #self.name = name - public
        #self._breed = breed - protected
        #self._name = name - protected
        self.__breed = breed # private
        self.__name = name # private

    def get_breed(self):
        return self.__breed

    def get_name(self):
        return self.__name

    def set_breed(self, elem):
        self.__breed = elem

# class Dog(Animal):
#
#     def print_info(self):
#         super()._breed = 'Pikegnese' - protected

anim = Animal('Teryer', 'Bob' )
anim.set_breed('Golden Retriver')

print(anim.get_breed())

'''


# Exercises:
'''
Реализуйте класс BankAccount, который будет иметь закрытый атрибут balance.
 Реализуйте методы deposit и withdraw, которые будут изменять баланс счета, 
 но не давайте возможность напрямую изменять его значение извне класса.

Создайте класс Employee, который будет иметь закрытый атрибут salary.
Реализуйте метод get_salary, который будет возвращать значение атрибута salary.
Но не давайте возможность изменять его значение извне класса.

Реализуйте класс Student, который будет иметь закрытый атрибут grades.
 Реализуйте методы set_grade и get_grades, которые будут изменять и 
 возвращать значения атрибута grades соответственно, но не давайте возможность 
 напрямую изменять его значение извне класса.

Реализуйте класс Car, который будет иметь закрытые атрибуты brand, model и year. 
Реализуйте метод get_car_info, который будет возвращать информацию о машине в виде 
строки, но не давайте возможность изменять значения атрибутов извне класса.

Создайте класс Game, который будет иметь закрытый атрибут score. 
Реализуйте методы update_score и get_score, которые будут изменять и возвращать
значение атрибута score соответственно, но не давайте возможность напрямую изменять 
его значение извне класса.

class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def set_balance(self,elem):
        self.__balance = elem

    def get_balance(self):
        return self.__balance

    def deposit(self,drop):
        self.__drop = drop
        self.__balance -=drop
        print(f'Your current balance = {self.__balance}')

    def withdraw(self,days_past):
        if days_past<365:
            return self.__balance+self.__drop
        elif days_past>365 and days_past<730:
            return self.__balance+self.__drop*1.5
        else:
            return self.__balance+self.__drop*2

bankAccaunt = BankAccount(1000000)
bankAccaunt.deposit(425000)
print(bankAccaunt.withdraw(1460))
'''



#Ассоциация.Агрегация.Композиция
'''

Tермин "Aссоциация" означает связь или отношение между двумя или более объектами.


1. Агрегация

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Classroom:
    def __init__(self, students):
        self.students = students

    def get_average_age(self):
        total_age = 0
        for student in self.students:
            total_age += student.age
        average_age = total_age / len(self.students)
        return average_age

# Создаем объекты студентов
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("John", 21)

# Создаем объект класса и передаем список студентов
classroom = Classroom([student1, student2, student3])

# Вызываем метод класса, который использует агрегированный список студентов
average_age = classroom.get_average_age()
print("Средний возраст студентов:", average_age)


2. Композиция
class Room:
    def __init__(self, room_number):
        self.room_number = room_number

class House:
    def init(self, address, room):
        self.address = address
        self.room = room

    def get_room_number(self):
        return self.room.room_number

# Создаем объект комнаты
room = Room(101)

# Создаем объект дома и передаем объект комнаты в конструктор
house = House("123 Main Street", room)

# Вызываем метод класса House, который использует объект комнаты
room_number = house.get_room_number()
print("Номер комнаты:", room_number)

'''

# Наследование.
'''
Наследование - это механизм в ООП, позволяющий создавать новый класс
на основе существующего,  уже существующий класс при этом называется базовым (или родительским)
классом, а новый класс - производным (или дочерним) классом.

При наследовании дочерний класс получает все атрибуты и методы базового класса,
а также может добавлять свои собственные атрибуты и методы,
переопределять или дополнять базовые методы.

Наследование позволяет избежать дублирования кода, если несколько классов имеют общие свойства и методы

class суперкласс :
    методы_суперкласса


class подкласс (суперкласс):
    методы_подкласса



#Множественное наследование и MRO (порядок разрешения методов).
Множественное наследование (Multiple Inheritance) - это возможность создания класса,
 наследующего свойства и методы одновременно от двух или более родительских классов.


 MRO (Method Resolution Order) - это порядок, в котором Python ищет методы в множественном наследовании.

'''
'''
class Zoo:
    def __init__(self,region):
        self.region_zoo = region

    def animal_exists(self,name):
        
        if name:
            print('animal exists in the zoo')
        else:
            print('there is no animal like this')

class Animal(Zoo):

    def __init__(self,region_animal,pet,name,age):
        super().__init__(region_animal)
        self.pet = pet
        self.name = name
        self.age = age

    def __str__(self):
        return f'Your animal is {self.pet} it lives in {self.region_zoo} its name is {self.name} and it is {self.age} '
    
    def info(self):
        self.animal_exists(self.name)
    
    
animal = Animal('Arizona','Cayote','Bruno',4)
print(animal)
animal.animal_exists('Bruno')


class Shop:
    def __init__(self,shop_name):
        self.shop = shop_name

class Toy(Shop):
    def __init__(self,shop_name,toy_name):
        super().__init__(shop_name)
        self.toy_name = toy_name

class Fruit(Shop):
    def __init__(self, shop_name, fruit_name):
        super().__init__(shop_name)
        self.fruit_name = fruit_name
'''


class Father:
    def __init__(self, f_name, eye_color):
        self.f_name = f_name
        self.eye_color = eye_color

class Mother:
    def __init__(self, m_name, hair_color):
        self.m_name = m_name
        self.hair_color = hair_color

class Child1(Father):
    def __init__(self, name, f_name, eye_color):
        super().__init__(f_name, eye_color)
        self.name = name

    def info(self):
        return f'\nFather: {self.f_name}, {self.eye_color}' \
               f'\nChild: {self.name}'

class Child2(Mother):
    def __init__(self, name, m_name, hair_color):
        super().__init__(m_name, hair_color)
        self.name = name

    def info(self):
        return f'\nMother: {self.m_name}, {self.hair_color}' \
               f'\nChild: {self.name}'


class Family(Child1, Child2):
    def __init__(self, name, f_name, eye_color, m_name, hair_color):
        Child1.__init__(self, name, f_name, eye_color)
        Child2.__init__(self, name, m_name, hair_color)

    def introduce(self):
        child1_info = Child1.info(self)  # вызов метода info() из Child1
        child2_info = Child2.info(self)  # вызов метода info() из Child2
        return f'Family Information:\n{child1_info}\n{child2_info}'

child1 = Child1('Pablo', 'Al\' Kapone', 'brown')
child2 = Child2('Migel', 'Tereza', 'black')

family = Family(child1.name, child1.f_name, child1.eye_color, child2.m_name, child2.hair_color)
print(family.introduce())

#Practise
'''
1. Создайте класс Human, который будет содержать информацию о человеке.
 С помощью механизма наследования, реализуйте класс Builder 
 (содержит информацию о строителе), класс Sailor (содержит информацию о моряке),
  класс Pilot (содержит информацию о летчике). 
 Каждый из классов должен содержать необходимые для работы методы



2.Создайте класс Число (или используйте уже ранее созданный вами).
 Класс число хранит внутри одно значение.
  Используя перегрузку операторов реализуйте для него арифметические 
  операции для работы с числом (операции +, -, *, /)
  
3.	Создайте класс Passport (паспорт), который будет содержать паспортную информацию о гражданине заданной страны.
 С помощью механизма наследования, реализуйте класс ForeignPassport (загран.паспорт) производный от Passport. 
 Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах,
  номер заграничного паспорта(то есть нужно создать новый конструктор)

4.	Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем.
 В случае базового класса это может быть строка с надписью This is Employer class. 
 Создайте от него три производных класса: President, Manager, Worker. 
 Переопределите функцию Print() для вывода информации, соответствующей каждому типу служащего


'''


