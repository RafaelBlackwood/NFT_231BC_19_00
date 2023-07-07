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
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Login')
        self.master.iconbitmap(default='icons/computer.ico')
        self.master.geometry('400x100+600+220')
        self.create_widgets()

    def create_widgets(self):
        self.var = IntVar()

        lbl_login = Label(self.master, text='Login').grid(row=0, column=0, padx=10)
        lbl_password = Label(self.master, text='Password').grid(row=1, column=0, padx=10)

        self.entry_login = Entry(self.master, bd=5)
        self.entry_login.grid(row=0, column=1, padx=10)

        self.entry_password = Entry(self.master, bd=5, show='*')
        self.entry_password.grid(row=1, column=1, padx=10)

        self.check_btn = Checkbutton(self.master, text='Show password', variable=self.var, command=self.show)
        self.check_btn.grid(row=1, column=2, padx=5)

        self.btn_login = Button(self.master, text='Login', command=self.login)
        self.btn_login.grid(row=2, column=2)


    def login(self):
        log = self.entry_login.get()
        psw = self.entry_password.get()

        if log == 'Admin' and psw == 'admin':
            self.master.withdraw()
            self.menu_window = Menu(self.master)
            self.menu_window.return_to_login = self.return_to_login

    def show(self):
        if self.var.get() == 1:
            self.entry_password['show'] = ''
        else:
            self.entry_password['show'] = '*'

    def return_to_login(self):

        self.master.deiconify()



class Menu(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Menu')
        self.geometry('300x400+600+220')
        self.create()

    def create(self):
        lbl = Label(self, text='Logged').pack()
        btn = Button(self, text='Return', command=self.return_to_login).pack()

    def return_to_login(self):
        self.destroy()
        self.return_to_login()


if __name__ == '__main__':
    root = Tk()
    log = Login(root)
    log.mainloop()
