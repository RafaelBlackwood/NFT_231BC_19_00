from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('Test')
root.iconbitmap(default='icons\computer.ico')
root.geometry('400x400+300+250')

#PhotoImage
'''
img = Image.open('images\img.png')
resize_img = img.resize((200,100))
image = ImageTk.PhotoImage(resize_img)
lbl = Label(root, image = image)
lbl.pack()
btn = Button(root, image = image)
btn.pack()
'''

#CheckButton


# def switch():
#     print(int_var.get())
#     if int_var.get() == 1:
#         btn['state'] = DISABLED
#     else:
#         btn['state'] = ACTIVE



#btn = Button(root, text = 'Check', state= ACTIVE)
#btn.pack()

'''def switch():
    if int_var.get()==1:
        entry_password['show']=''
    else:
        entry_password['show'] = '*'

Lbl_name = Label(root, text='Username: ')
Lbl_name.place(relx = 0.09, rely = 0.09)
Lbl_password = Label(root, text='Password: ')
Lbl_password.place(relx = 0.09, rely = 0.29)

entry_name = Entry(root)
entry_name.place(relx = 0.09, rely=0.19)
entry_password = Entry(root, show = '*')
entry_password.place(relx= 0.09, rely=0.39)

int_var = IntVar()
check_btn = Checkbutton(root,text = 'Switch states',variable=int_var,command=switch)
check_btn.place(relx = 0.39, rely= 0.39 )'''

#ListBox
'''def save():
     select  = lst_box.curselection()
     print(select)
     select_list = [lst_box.get(i) for i in select]

     lst_box.delete(select)
     return select_list

lst_box = Listbox(root,selectmode=SINGLE)

for i in range(5):
    lst_box.insert(i,input())

lst_box.pack()
btn_save = Button(root, text ='save info', command= save)
btn_save.pack()
'''

#MessageBox
'''
showinfo(): выводит информационное сообщение.
showwarning(): выводит сообщение предупреждения.
showerror(): выводит сообщение об ошибке.
askquestion(): выводит диалоговое окно с вопросом и двумя кнопками "Да" и "Нет".
askokcancel(): выводит диалоговое окно с вопросом и двумя кнопками "ОК" и "Отмена".
askyesno(): выводит диалоговое окно с вопросом и двумя кнопками "Да" и "Нет".
'''

'''from tkinter.messagebox import *

def message():
    showerror('Games','Dont play games')
    while True:
        answer = askquestion('Ensure', 'Do you understand?')
        if answer == 'yes':
            showinfo('Congrats', 'Good job man')
            break
        else:
            showerror('Incorrect', 'You are not allowed to say no')
            


btn_warning = Button(root,text='Show warning' ,command=message)
btn_warning.pack()'''
#Grid
def vvod(symbol):
    entry.insert(END,symbol)

btn_c = Button(text= 'C',width=13,height=2)


entry = Entry(width=45,bd = 3)
entry.grid(row = 0,column=0,columnspan=3,padx=10)

btn_1 = Button(text= '1',width=13,height=2,command=lambda : vvod('1')).grid(row=1,column=0)

btn_2 = Button(text= '2',width=13,height=2,command=lambda : vvod('2')).grid(row=1,column=1)

btn_3 = Button(text= '3',width=13,height=2,command=lambda : vvod('3')).grid(row=1,column=2)

btn_4 = Button(text= '4',width=13,height=2,command=lambda : vvod('4')).grid(row=2,column=0)

btn_5 = Button(text= '5',width=13,height=2,command=lambda : vvod('5')).grid(row=2,column=1)

btn_6 = Button(text= '6',width=13,height=2,command=lambda : vvod('6')).grid(row=2,column=2)

btn_7 = Button(text= '7',width=13,height=2,command=lambda : vvod('7')).grid(row=3,column=0)

btn_8 = Button(text= '8',width=13,height=2,command=lambda : vvod('8')).grid(row=3,column=1)

btn_9 = Button(text= '9',width=13,height=2,command=lambda : vvod('9')).grid(row=3,column=2)

btn_0 = Button(text= '0',width=13,height=2,command=lambda : vvod('0')).grid(row=4,column=1)

btn_eq = Button(text= '=',width=13,height=2,command=lambda : equal()).grid(row=4,column=2)

btn_plus = Button(text= '+',width=13,height=2,command= lambda: vvod('+')).grid(row=4,column=3)

btn_minus = Button(text= '-',width=13,height=2,command= lambda: vvod('-')).grid(row=3,column=3)

btn_umnozh = Button(text= '*',width=13,height=2,command= lambda: vvod('*')).grid(row=2,column=3)

btn_deleniye = Button(text= '/',width=13,height=2,command= lambda: vvod('/')).grid(row=1,column=3)
root.mainloop()

'''
Peppironi
Cheese
Pizza
Spagetti
Tomato 
'''