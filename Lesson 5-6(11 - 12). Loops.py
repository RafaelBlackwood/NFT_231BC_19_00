#Reapeating IF/ELSE
'''
Вы являетесь сотрудником. Наступает конец месяца,
вы получаете зарплату в размере 1000 манат. Вы живете на квартире
вам нужно распределить зарплату так, чтобы и покушать вкусно могли
и в спортзал сходить и с друзьями погулять и себе отложить на будущее немного.
Если к концу месяца у вас останется 0 манат, к счастью вы пережили месяц,
если зарплата закончилась раньше, то вы, мой друг, не живете!

Напишите код который сбалансирует вашу жизнь.
'''



#Loops (Циклы)
#while and For

#while - цикл с уловием
'''
Syntaxix:

while условие:        #До тех пор пока условие True выполняй тело цикла
    инструкции цикла(тело цикла)

else:(else блок писать не обязательно.)
    последнее слова цикла, когда условие перестало быть True

#Бесконечный цикл    
while True:
    инструкции Цикла
'''

'''
backet = False #Переменная отвечающая за то, пустая ли бочка или нет
count = 0 #Переменная отвечающая за то, сколько раз будет заполнена бочка
Full_Backet = int(input('Enter the capacity of Bochka'))#Переменная отвечающая за то, сколько ведер нужно для заполнения бочки

while backet!=True:
    count+=1
    print('Заполнили бочку',count,' раз')
    if count==Full_Backet:
        backet=True
'''

'''
while True:
    print('Big Tasty Tripple menu')
    '''

argument_1 = 1
argument_2 = 1
while argument_1 != 11:
    while argument_2 != 7:
        print(argument_1,'*',argument_2,'=',argument_1*argument_2)
        argument_2+=1
    argument_1 += 1
    argument_2 = 1
    print('_____________')
