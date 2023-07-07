#Events. Binding
'''from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('Test')
root.iconbitmap(default='icons\computer.ico')
root.geometry('400x400+300+250')


def switch():
    if int_var.get()==1:
        entry_password['show']=''
    else:
        entry_password['show'] = '*'

def clear():
    entry_password.delete(first=0, last=END)
    entry_name.delete(first=0, last=END)

def log(event):
    if entry_password.get()== 'admin' and entry_name.get()== 'admin':
        clear()
        showinfo('Success','You entered right data')
    else:
        clear()
        showerror('Wrong data','Please Try again')


def joker(event):
    btn_log['text'] = 'Haha, you are fooled'
def anti_joker(event):
    btn_log['text'] = 'Login'

def info():
    if entry_password.get() == 'admin' and entry_name.get() == 'admin':
        clear()
        showinfo('Success', 'You entered right data')
    else:
        clear()
        showerror('Wrong data', 'Please Try again')

Lbl_name = Label(root, text='Username: ').place(relx = 0.09, rely = 0.09)
Lbl_password = Label(root, text='Password: ').place(relx = 0.09, rely = 0.29)

entry_name = Entry(root)
entry_name.place(relx = 0.09, rely=0.19)
entry_password = Entry(root, show = '*')
entry_password.bind("<Return>",log)
entry_password.place(relx= 0.09, rely=0.39)

int_var = IntVar()
check_btn = Checkbutton(root,text = 'Switch states',variable=int_var,command=switch)
check_btn.place(relx = 0.39, rely= 0.39 )

btn_log = Button(root, text= 'Login',command=info)
btn_log.bind('<Enter>', joker)
btn_log.bind('<Leave>', anti_joker)
btn_log.place(rely=0.47,relx=0.39)

root.mainloop()'''

from tkinter import *
from tkinter.messagebox import *
class Login(Frame):
    def __init__(self,master): #master = root
        super().__init__(master)
        master.title('Login window')
        master.iconbitmap(default='icons\computer.ico')
        master.geometry('300x150+600+200')
        self.widgets()

    def widgets(self):
        lbl_name = Label(self.master, text = 'Username\Email').grid(row = 0, column = 0, padx= 10,pady=20)
        lbl_pass = Label(self.master, text = 'Password').grid(row = 1, column = 0, padx= 10)


        self.entry_name = Entry(self.master)

        self.entry_password = Entry(self.master)


        self.btn_log = Button(self.master,text='Login', command = self.log)

        self.btn_reg = Button(self.master,text='Registration', command = self.reg)

        self.check_pass = Checkbutton(self.master, text='Show password',command=self.show)

    def log(self):
        ...

    def reg(self):
        ...

    def show(self):
        ...

class Registration(Frame):

    ...

class Menu(Frame):
    ...


if __name__ == '__main__':
    root = Tk()
    log = Login(root)
    log.mainloop()
