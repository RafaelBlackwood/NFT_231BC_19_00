# 1.Файлы.
'''
Файл — это именованная область, расположенная во внешней памяти,
и обладающая следующими характеристиками:
■ имя файла (на определенном диске), которое позволяет программам идентифицировать файл
■ длина файла может быть ограничена только объемом диска.
'''

# 1.1Типы файлов, текстовые и бинарные.
'''
Текстовые файлы — это файлы хранящий в себе последовательность символов.
При передаче символов из потока на экран, часть из
них не выводится (например, символ сдвига на табуляцию, перевода строки).
Бинарные файлы - это файлы хранящие в себе  последовательность байтов,
которые однозначно соответствуют тому, что находится на внешнем устройстве
'''

# 1.2.Файловая система, особенности реализации форматов.
'''
Примеры текстовых файлов: (человек способен прочитать в любом текстовом редакторе)
■ web документы, стандарты: html, XML, CSS, JSON etc.
■ файлы исходных кодов: c, app, js, py, java etc.
■ текстовые документы: txt, tex, RTF etc.
■ текстовые представления табличных данных (файлы
с разделителями): csv, tsv etc.
■ файлы настроек и конфигураций: ini, cfg, reg etc

Примеры двоичных файлов:(человек не способен прочитать  в любом текстовом редакторе)
■ документы и электронные таблицы: .pdf, .doc, .xls etc.;
■ изображения: .png, .jpg, .gif, .bmp etc.;
■ видео: .mp4, .3gp, .mkv, .avi etc.;
■ аудио: .mp3, .wav, .mka, .aac etc.;
■ базы данных: .mdb, .accde, .frm, .sqlite etc.;
■ архивы: .zip, .rar, .iso, .7z etc.;
■ исполняемые файлы программ: .exe, .dll, .class etc.
'''

# 1.3.Работа с файлами:
'''
#открытие:
open(путь_к_файлу или переменная хранящая путь, режим открытия файла)
fileObj = open(fileName, mode)
fileName — это имя файла (или путь к нему), который вы хотите открыть.
При этом с именем вы должны указать и расширение. 
#закрытие;

#чтение:
read()
#запись:
write()
#закрытие:
close()

Режимы(моды):
Text file:
r - Открытие текстового файла только для
чтения. Если такого файла не существует, то
будет сгенерировано исключение
(обработка данных начинается с начала файла)

w - Открытие текстового файла только для
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

a - Открытие текстового файла для добавления текста в конец файла.
Если такой файл не существует, то он будет
создан.
(обработка данных начинается с конца файла)

r+ - Открытие текстового файла для чтения и
записи. Если такого файла не существует, то
будет выведена ошибка.
(обработка данных начинается с начала файла)

w+ - Открытие текстового файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

a+ - Открытие текстового файла для чтения и
добавления текста в конец файла. Если такой файл не существует,
то он будет создан.
(обработка данных начинается с конца файла)


Binary file:
rb - Открытие двоичного файла для чтения.
Если такого файла не существует, то будет
выведена ошибка.
(обработка данных начинается с начала файла)

wb - Открытие двоичного файла для записи.
Если такой файл не существует, то он
будет создан. Иначе его содержимое будет
удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)


ab - Открытие двоичного файла для добавления.
Если такой файл не существует, то он будет
создан. Иначе данные из него будут удалены
(обработка данных начинается с конца файла) 

wb+ - Открытие двоичного файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

ab+ - Открытие двоичного файла для чтения и
добавления. Если такой файл не существует,
то он будет создан. Иначе его содержимое
будет удалено
(обработка данных начинается с конца файла)
'''

# 1.4.Менеджер контекста with.
'''
Оператор with используется при обработке исключений, чтобы сделать код более чистым и читабельным.
 Это упрощает управление общими ресурсами, такими как файловые потоки.
Преимущество использования ключевого слова with перед вызовом функции open() в том, что функция file.close() 
 вызовется автоматически и освободит занятые ресурсы после того, как отработает код.

 без with:
try:
    somefile = open("test.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

с with:
with open(file, mode) as file_obj:
    инструкции

#Porblem of coding 
with open(filename, encoding="utf8") as file:
'''

# 2.Бинарные файлы
'''
Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт.
'''
# from pickle import dump,load
# car = 'Tesla'
# year = 2016
#
# with open(r"", "wb") as fileHandler:
#     dump(car,fileHandler)
#     dump(year,fileHandler)
#
# with open(r"", "rb") as fileHandler:
#     print(load(fileHandler))
#     second = load(fileHandler)
#     print(f'{second} this type has value = {second}')

# 2.1.Binary methods

#Binary file:
'''
rb - Открытие файла для чтения.
Если такого файла не существует, то будет
выведена ошибка.
(обработка данных начинается с начала файла)

wb - Открытие файла для перезаписи.
Если такой файл не существует, то он
будет создан. Иначе его содержимое будет
удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)


ab - Открытие файла для добавления элементов в конец. 
Если такой файл не существует, то он будет
создан. Иначе данные из него будут удалены
(обработка данных начинается с конца файла) 

wb+ - Открытие файла для чтения и
перезаписи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

ab+ - Открытие файла для чтения и
добавления элементов в конец . Если такой файл не существует,
то он будет создан. Иначе его содержимое
будет удалено
(обработка данных начинается с конца файла)
'''
'''
import pickle - модуль необходимый для работы с бинарными файлами

dump(obj, file): записывает объект obj в бинарный файл file
load(file): считывает данные из бинарного файла в объект
'''

'''
from pickle import *

with open('Files/user_data.json','wb') as FileHandler:
    dump('Hello', FileHandler)
    dump('Khinkhali', FileHandler)

with open('Files/user_data.json','ab') as FileHandler:
    dump('Rafael', FileHandler)
    dump('Hasan', FileHandler)


with open('Files/user_data.json','rb') as FileHandler:
    temp = load(FileHandler)
    print(temp)
    print(load(FileHandler))'''



from tkinter import *
from tkinter.messagebox import *
from pickle import *

class Person:
    def __init__(self,email,login,password):
        self.__email = email
        self.__login = login
        self.__password = password

    def get_email(self):
        return self.__email
    def get_login(self):
        return self.__login
    def get_password(self):
        return self.__password

    def set_email(self,item):
        self.__email = item
    def set_email(self,item):
        self.__login = item
    def set_email(self,item):
        self.__password = item


def SaveRegInfo():
    login = entry_login.get()
    email = entry_email.get()
    password = entry_password.get()

    person = Person(email,login,password)

    person_data = {
        'login': person.get_login(),
        'email': person.get_email(),
        'password': person.get_password()
    }

    with open('Files/user_data.json','wb') as FileHandler:
        dump(person_data,FileHandler)
    showinfo('Success', 'You registered')

def LoadRegInfo():
    with open('Files/user_data.json','rb') as FileHandler:
        temp = load(FileHandler)

    person = Person(
        temp['email'],
        temp['login'],
        temp['password']
    )
    return person


def choose_option():
    temp = entry_menu.get()

    if temp == '1':
        frame_menu.forget()
        frame_registration.place(relx=0, rely=0)
    elif temp =='2':
        ...
    elif temp ==  '3':
        root.destroy()
    else:
        showerror('Wrong option', 'Please choose options from 1 to 3')

def BackToMenu():
    frame_registration.place_forget()
    frame_menu.place(rely=0,relx=0)


root = Tk()
root.iconbitmap(default='icons/computer.ico')
root.geometry('650x650+600+200')
root.resizable(False,False)


#First Menu
frame_menu = Frame(width=650,height=650, bg= '#a36739')
frame_menu.place(relx = 0,rely = 0)

lbl_menu = Label(frame_menu, text = 'Choose option: 1) New User. 2)Login. 3) Exit', font='Arial 18')
lbl_menu.place(relx=0.1 , rely=0.3)

entry_menu = Entry(frame_menu, bd = 5, width= 40)
entry_menu.place(relx=0.3,rely=0.38)

btn_menu = Button(frame_menu, bd = 2, text='Select option',height=3,width=20, command=choose_option)
btn_menu.place(relx = 0.75,rely=0.38)

#Second menu

frame_registration = Frame(width=650,height=650, bg= '#733f18')

label_email = Label(frame_registration, text="Email:")
label_email.place(x=20, y=140)
entry_email = Entry(frame_registration, bd=5)
entry_email.place(x=100, y=140)

label_login = Label(frame_registration, text="Login:")
label_login.place(x=20, y=180)
entry_login = Entry(frame_registration, bd=5)
entry_login.place(x=100, y=180)

label_password = Label(frame_registration, text="Password:")
label_password.place(x=20, y=220)
entry_password = Entry(frame_registration, bd=5, show='*')
entry_password.place(x=100, y=220)

btn_save = Button(frame_registration, text="Save", bg="brown", fg="white", command=SaveRegInfo)
btn_save.place(x=20, y=300)

btnPrevious = Button(frame_registration, text="Previous", bg="brown", fg="white", height=6, command=BackToMenu)
btnPrevious.place(x=592, y=544)

root.mainloop()
