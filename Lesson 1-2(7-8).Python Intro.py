#Тип и значения.
'''
int - integer(целые числа) (1,11,123,12412...)

float - floating (числа с плавующей запятой)( 2.5, 3.14, 123.9231 .....)

str - string(строка) ('Hello', 'Your name' ....)

bool - boolean( это логический тип данных он имеет два значения :
    True(имеет целочисленное представление = 1) и False(имеет целочисленное представление = 0))

complex - complexity(комплексные числа)
'''

#Переменные.Имена переменных и зарезервированные слова.
'''
Переменная - именованная область памяти, хранящая какое-либо значение. 
Хранится в оперативной памяти.
Объевление переменной - это все равно что создать ее и задать ей название
Инициализация переменной - это присваивание переменной какое-либо значение
number = 10
Number = 5.2
User_Data = 20
teacher1 = True #False
_NameStudent = 'Yashar'

'''

#Операторы, операнды и операция.Операции над переменными.
'''
+ - addition
number_1 = 6
number_2 = 19
number_3 = number_2 + number_1
print(number_3)

- - substraction
number_1 = 6
number_2 = 19
number_3 = number_2 - number_1
print(number_3)

* - multiplication
number_1 = 6
number_2 = 9.2
number_3 = number_1 * number_2
number_3 = int(number_3)
print(number_3)

/ - float devision 
number_1 = 25
number_2 = 4
number_3 = number_1/number_2
print(number_3)

// - integer devision
number_1 = 25
number_2 = 2
number_3 = number_1//number_2
print(number_3)
print(type(number_3))

% - remaining from devision
number_1 = 324
number_2 = 7
number_3 = number_1 % number_2
print(number_3)
print(type(number_3))

** -  exponentiation (возведение в степень)   
number_1 = 2
number_2 = 7
number_3 = number_1 ** number_2
print(number_3)

'''

#Приоритеты операторов.
'''
1.(выражения...) - Круглые скобки

2. ** Возведение в степень

3. +x, -x  Унарные плюс и минус

4. *, /, //, %  Умножение, деление, целочисленное деление, взятие остатка от деления. Слева направо

5. +, -  Сложение и вычитание

result = 10*100+11//2 - 2**5 * 10 + (11*2)
print(result)


'''

#Ввод/вывод.
'''
print() - output data 
sep - seperate with symbol
end - add to end symbol
print('12 heLLO True')
print(12,"heLLO",True)
print(type('12 heLLO True'))

input()
line = input()
print('Your result is:', line)
print(type(line))

number = int(input())
print('Your result is:', number)
print(type(number))

number_2 = float(input())
print('Your result is:', number_2)
print(type(number_2))

logic_1 = bool(input())
logic_2 = bool(input())
print('Your result is:', logic_1)
print('Your result is:', logic_2)
print(type(logic_1))
print(type(logic_2))
print(logic_1+logic_2)

'''




#Преобразование типов.(Type casting)
'''
1. Неявное преобразование- это то преобразование которое происходит в момент выполнения программы
num_1= 10
num_2= 12.3
num_3 = num_1+num_2

2. Явное преобразование - это то преобразование которое мы сами явно указываем
num_1= 10
num_2= 12.3
num_3 = float(num_1)+int(num_2)
'''

