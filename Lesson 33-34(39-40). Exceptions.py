# Исключения (Exception)
'''
Исключения - это ошибки, обнаруженные при исполнении программы.(или реакция программы на исключительные ситуации в ходе ее выполнения.)
2 типа ошибок:
1. Синтаксические - ошибки указывающие на нарушения синтаксиса языка
2. Ошибки выполнения - ошибки появляющиеся уже в запущенной программе в процессе ее выполнения
другими словами подобные ошибки - исключения.
'''


# Типы исключений
'''
2 типа исключений
1. Явные - через команду raise
2. Скрытые - те что спрятаны в функциях,классах, методах(те что трудно заметить)
'''

# Конструкция try except finally.
'''
Чтобы избежать резкого прерывания программы 
и обрабатывать исключения есть конструкция try..except.

try: - сюда помещается основной код, в котором потенциально может возникнуть исключение
    инструкции
except [Тип_исключения]: - Если в коде генерируется исключение, то работа кода в блоке try прерывается, и выполнение переходит сюда. Тип исключения не обязательно указывать
    инструкции
else:
    если не было исключений


Блок finally
Данный блок работает как последнее слово исключения,само же исключение может и не сработать, данный блок в любом случае отработает,если он будет присутствовать 
В основном используется для освобождения данных или закрытия файлов


while True:
    try:
        num_1 = int(input())
        num_2 = int(input())

        print(num_1//num_2)

    except:
        print('Cannot devide by zero')
        
        
    
    
while True:
    try:
        num_1 = int(input())
        num_2 = int(input())

        print(num_1//num_2)

    except ZeroDivisionError:
        print('Cannot devide by zero')
    except ValueError:
        print('Cannot calculate words, please write digits')
    else:
        print('Hakuna matata')
    finally:
        print('ya nagliy ya srabotal')
'''

# Базовые типы исключений.
'''
all exceptions in documentation https://docs.python.org/3/library/exceptions.html
•	BaseException - базовый тип для всех встроенных исключений
•	Exception - базовый тип, который обычно применяется для создания своих типов исключений
•	ArithmeticError -  базовый тип для исключений, связанных с арифметическими операциями (OverflowError, ZeroDivisionError, FloatingPointError).
•	BufferError - тип исключения, которое возникает при невозможности выполнить операцию с буффером
•	LookupError -  базовый тип для исключений, которое возникают при обращении в коллекциях по некорректному ключу или индексу (например, IndexError, KeyError)
выше были перечислены одни из основных классов от которых наследуются исключения
•	IndexError - исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона
•	KeyError - возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.
•	OverflowError - возникает, если результат арифметической операции не может быть представлен текущим числовым типом (обычно типом float).
•   RecursionError: возникает, если превышена допустимая глубина рекурсии.
•   ValueError - возникает, если операция или функция получают объект корректного типа с некорректным значением.
•   TypeError: возникает, если операция или функция применяется к значению недопустимого типа.

и т.д.
'''

# Получение информации об исключении через оператор as
'''
С помощью оператора as передается вся информация об исключении в переменную, которую затем используется в блоке except


try:
    element = input()
    number = int(input())

    print(element+number)

except Exception as e:
    print(f'{e}')
'''

# Примеры использования.
'''
1. Написать функцию которая обработает исключение при делении двух чисел.
2. Обработайте исключение при работе с математическими операциями(например корни отрицательных чисел)
3. Обработайте исключенийе при работе со списками( выход за пределы индексации списка)
4. Обработайте исключение при работе с типами данных(например ввод не тех типов данных или работа с несовместимыми типами)
5. Обработайте исключение при работе со строками(допустим выход за пределы индексации или не корректный ввод)
6. Обработайте исключение при работе с конвертацией типов данных.
'''
from math import sqrt

try:
    number = int(input())

    print(sqrt(number))

except Exception as e:
    print(f'Your error is {e}\nYou cannot have a negative number under a square root')



# Генерация исключений.
'''
Оператор raise нужен,чтобы вручную сгенерировать то или иное исключение

'''


# Practise:
'''
1. Создайте функцию, которая принимает список и выводит
на экран все элементы списка, пока не встретит элемент
с нулевым значением. Если в списке нет элемента со значением 0,
функция должна выводить сообщение об ошибке.

2. Напишите программу, которая запрашивает у пользователя свой возраст. 
Если пользователь ввел отрицательное число или ноль, программа должна 
выдавать ошибку и повторно запрашивать возраст.

3. Напишите программу, которая принимает на вход список чисел и выводит на экран их сумму.
 Если в списке есть некорректные данные, например, не числа, программа должна выдавать ошибку.

4. Напишите программу, которая запрашивает у пользователя строку и пытается преобразовать
 ее в число. Если это невозможно, выведите сообщение об ошибке.

5. Напишите программу, которая запрашивает у пользователя число и выводит его квадратный корень.
 Если квадратный корень отрицательный , программа должна выдать ошибку.
'''




