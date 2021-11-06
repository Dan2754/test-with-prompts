from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x100')
root.title("контрольная")

window = Tk()
window.title("Контрольная работа по физике")
window.geometry('1920x1080')
#window.attributes('-fullscreen', True) потом включить
window1 = Tk()
window1.title("Подсказки")
window1.geometry('800x800')
window1.withdraw()

lbl5 = StringVar()
lbl5_label = Label(window, text="Введите ответ в числовом виде", font=("Arial Bold", 20))
lbl5_label.place(relx=.02, rely=.4)
lbl5_entry = Entry(window, textvariable=lbl5)
lbl5_entry.place(relx=.02, rely=.45)
window.withdraw()
name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

n=0
def click_button():
    name = name_entry.get() # переменной name задается введеное выражение
    surname = surname_entry.get()
    root.destroy()
    window.deiconify()
    l1=[]
    file = open('C:/2/data.txt','r')
    for line in file:
        l1.append(line)
    msg = Message(window, width=500, pady=10)
    msg.config(text=l1[5], bg="white", bd=10, relief=GROOVE, font=("times",16, "italic"))
    msg.place(relx=.5, rely=.1, anchor="c")
    lbl3 = Label(window, text="Задача 1", font=("Arial Bold", 30))
    lbl3.place(relx=.0, rely=.0)
    l2=[]
    newButton = Button(window, text="Подсказка", command=lambda:(open('C:/2/data1.txt','r'), open_window1()))
    for line1 in newButton:
        l2.append(line1)
    msg = Message(window1, width=500, pady=10)
    msg.config(text=l2[5], bg="white", bd=10, relief=GROOVE, font=("times", 16, "italic"))
    msg.place(relx=.5, rely=.1, anchor="c")
    newButton.place(relx=.6, rely=.6)
    lbl5 = lbl5_entry.get()
btn = Button(root, text="Продолжить",padx="40", pady="40", command=click_button)
btn.place(relx=.8, rely=.8, anchor="c",width=130, height=30)
def click_btn1():
    global n
    n += 1
    a = "Задача " + str(n)
# задача, а номер после каждого клика увеличивается на 1
    lbl2 = Label(window, text=a, font=("Arial Bold", 30))
    lbl2.place(relx=.0, rely=.0)
    l3=[]
    file = open('C:/2/data.txt', 'r')
    for line in file:
        l3.append(line)
    msg1 = Message(window, width=500, pady=10)
    msg1.config(text=l3[4], bg="white", bd=10, relief=GROOVE, font=("times", 16, "italic"))
    msg1.pack()
btn1 = Button(window, text="Далее", padx="40", pady="40", command=click_btn1)
btn1.place(relx=.8, rely=.8, anchor="c",width=130, height=30)
root.mainloop()
window.mainloop()