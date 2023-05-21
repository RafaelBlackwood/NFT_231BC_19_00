'''
while условие:
    инструкции цикла

ЕСЛИ УСЛОВИЕ цикла возвращает  TRUE тогда тело цикла начинает свою работу
УСЛОВИЕ ЦИКЛА может быть абсолютно любым, но вы должны исходить из условия вашей задачи.
'''

#Range between 1 and 50 по возрастания
'''num_1,num_2 = int(input()),int(input())

while num_1<=num_2:
    print(num_1)
    num_1+=1

'''
#Диапазон по убывающей
'''num_1,num_2 = int(input()),int(input())

while num_1<=num_2:
    print(num_2)
    num_2-=1'''

#With condition
'''number = int(input())

while number!=0:
    print(number)
    number-=1'''

#Example
#Вводится целое число, посчитать сколько цифр в числе
'''
num_1=int(input())
count = 0
while num_1>0:
    print('Do:',num_1)
    num_1//=10
    print('Posle:',num_1)
    count+=1
print(count)
'''

#Вводится целое число, посчитать сколько десятков,сотен и тысяч в числе
'''
number= int(input())

_1 = number%10
_2 = number//10%10
_3 = number//100%10
_4 = number//1000%10

print(_1)
print(_2)
print(_3)
print(_4)
'''

#Вводится целое число, вывести в консоль числа отдельные по разрядам
#К примеру, вы вводите 5431, вам выводится : 5000, 400, 30 ,1
'''number = int(input())
multiply = 1
while number!=0:
    remain = number%10
    print('remaining: ',remain)
    result=remain*multiply
    print(result)
    multiply*=10
    print('Multiply: ', multiply)
    number//=10
    print('Number: ', number)
    print('\nNEW ITERATION\n_____________')

'''


'''Пользователь вводит число. 
Определить количество цифр в этом числе, 
посчитать их сумму и среднее арифметическое.
 Определить количество нулей в этом числе.
 Общение с пользователем организовать через меню'''
