from tkinter import *

root = Tk()
root.title('Test')
root.iconbitmap(default='icons\computer.ico')
root.geometry('400x400+300+250')


def switch():
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
check_btn.place(relx = 0.39, rely= 0.39 )


root.mainloop()