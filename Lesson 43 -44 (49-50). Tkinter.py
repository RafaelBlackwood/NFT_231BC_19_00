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
int_var = IntVar()

def switch():
    print(int_var.get())
    if int_var.get() == 1:
        btn['state'] = DISABLED
    else:
        btn['state'] = ACTIVE



btn = Button(root, text = 'Check', state= ACTIVE)
btn.pack()
check_btn = Checkbutton(root,text = 'Switch states',variable=int_var,command=switch)
check_btn.pack()

entr = Entry(root, show = '*')
entr.pack()
#ListBox
'''

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

#Grid



root.mainloop()
