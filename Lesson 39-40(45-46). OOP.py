# Полиморфизм.
'''
Полиморфизм - это принцип объектно-ориентированного программирования, который позволяет объектам
 одного класса иметь различное поведение при вызове одного и того же метода,
в зависимости от типа объекта, с которым он работает.

1.Метод одного класса, реализация которого происходит в других классах



2. Перегрузка операторов.Реализация магических методов.
https://habr.com/ru/post/186608/



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3.x, p3.y)  # Output: 4 6
'''

'''
class Operation:
    def execute(self,x,y):
        pass

class Addition(Operation):
    def execute(self,x,y):
        return x+y

class Subtraction(Operation):
    def execute(self,x,y):
        return x-y

class Multiply(Operation):
    def execute(self,x,y):
        return x*y

class Division(Operation ):
    def execute(self,x,y):
        if y ==0:
            raise Exception('Cannot divide by zero')
        else:
            return x/y

class Calculator:
    def __init__(self,operation):
        self.op = operation

    def calculate(self,x,y):
        return  self.op.execute(x,y)

add =Addition()
sub = Subtraction()
mult = Multiply()
div = Division()

calc = Calculator(div)
print(calc.calculate(2,5))'''

#Practise
'''
1.Улучшить код с урока добавив проверку типов, если два типа не соответствуют друг другу, генерировать ошибку.
Если пользователь ввел число в виде строки, также, сделать преобразование из строки в число

2. Используя механизм множественного наследования 
разработайте класс “Автомобиль”. Должны быть классы 
«Колеса», «Двигатель», «Двери» и т.д

3.Создать базовый класс Employer (служащий) с функцией Print().
 Она должна выводить информацию о служащем. В случае базового класса это может быть строка 
с надписью This is Employer class. Создайте от него три производных класса: President, 
Manager, Worker. Переопределите функцию Print() для 
вывода информации, соответствующей каждому типу 
служащего.

4. Создать базовый класс «Домашнее животное» и производные классы «Собака», «Кошка», «Попугай», «Хомяк». 
С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого 
из классов методы: 
■ Sound — издает звук животного (пишем текстом в 
консоль);
■ Show — отображает имя животного;
■ Type — отображает название его подвида

5. Создать класс Flat (квартира). Реализовать перегруженные операторы:
■ Проверка на равенство площадей квартир (операция ==);
■ Проверка на неравенство площадей квартир (операция !=);
■ Сравнение двух квартир по цене (операции > < <= >=).
'''

