#Экранированные последовательности.
'''
\n - perexod na novuyu stroku
\t - ставит табуляцию в строке после себя
\b - удаляет символ до себя
\\ - выводит \
\' - выводит '
\" - выводит "
'''
'''
print('Грехи других '
      '\nСудить вы так усердно рветесь '
      '\nНачните со своих '
      '\nИ до чужих не доберетесь'
      '\n\t\'Shekspir\'')

print('C:\\Users\\Aghashirinov_r\\Documents\\Visual Studio 2019')
'''

#«Сырые строки».
#print(r'C:\Users\Aghashirinov_r\Documents\Visual Studio 2019')


#Форматированный вывод.
'''
f"stroka....{x} stroka...  {y} stroka..." - 1 sposob


num_1 = int(input())
num_2 = int(input())

for i in range(num_1,num_2+1):
    for j in range(num_1,num_2+1):
        a = f'{i} * {j}  your result is = {i*j}'
        print(a)
    print()

text = "Hello, {first_name}.".format(first_name="Tom") - 2 sposob (immenovanniy)
info = "Name: {0}\t Age: {1}".format("Bob", 23) - takje vtoroy sposob(parametr po poziciyi)


text = "Hello, {first_name} {first_surname}".format(first_surname=  'Bublik',first_name="Tom")
print(text)
info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)


# placeholders:
s: для вставки строк
d: для вставки целых чисел
f: для вставки дробных чисел.
%: умножает значение на 100 и добавляет знак процента


{переменная:placeholder}
{:[количество_символов][запятая][.число_знаков_в_дробной_части] плейсхолдер}


string = "Hello {:s}"
name = "Tom"
formatted_string = string.format(name)
print(formatted_string)


number_1 = 11.213124142
print("{:.3f}".format(number_1))
print(f"{number_1:%}")
print(f"{number_1:.0%}")
print(f"{number_1:.1%}")


'''

#Модуль string.
'''from string import *

STR_text= '1234213 a,dADqE24'

for i in STR_text:
    if i in ascii_letters:
        print('yes')

print(punctuation)'''

#Sep,End
#print('Hello','World',111110,sep ='!!!!',end= 'IT IS THE END')

#Practise
'''
Task 1
Сделать примитивный калькулятор который выполняет операции: +-*/**// с двумя числами, которые вводятся с клавиатуры
Task 2
Пользователь вводит с клавиатуры арифметическое 
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения. 
В нашем примере это 35. Арифметическое выражение 
может состоять только из трёх частей: число, операция, 
число. Возможные операции: +, -,*,/

Task 3
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в 
тексте.
'''

'''
while True:
    num_1 = int(input())
    num_2 = int(input())
    symbol = input()
    if symbol =='+':
        print(num_1+num_2)

    elif symbol =='-':
        print(num_1-num_2)

    elif symbol =='/':
        print(num_1/num_2)

    elif symbol =='//':
        print(num_1//num_2)

    elif symbol =='*':
        print(num_1*num_2)

'''