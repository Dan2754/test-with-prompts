from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Контрольная работа по физике")
window.geometry('1920x1080')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab11 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='ФИО')
lbl1 = Label(tab1,text="Введите имя:",font=("Arial Bold",20))
lbl1.grid(column=25, row=0)
lbl1 = Label(tab1, text="Введите фамилию:",font=("Arial Bold",20))
lbl1.grid(column=25, row=25)
tab1 = Entry(tab1,width=20)
tab1.grid(column=2, row=0)
tab11 = Entry(tab1,width=20)
tab11.grid(column=2, row=3)
tab_control.add(tab2, text='Первая задача')
n=0

lbl2 = Label(tab2, text='Автомобиль, двигаясь с ускорением -0,5 м/с2, уменьшил свою скорость от 54 до 18 км/ч. Сколько времени ему для этого понадобилось?\n' "В решении запишите формулу с подставленными значениями",font=("Arial Bold",20))
lbl2.place(relx=.1, rely=.1)



def click_button():
    global n
    n += 1
    a="Задача "+str(n)
    lbl3=Label(tab2, text=a, font=("Arial Bold",30))
    lbl3.place(relx=.005, rely=.005)
def
btn = Button(text="Подсказка",padx="40", pady="40", command=click_button)
btn.place(relx=.9, rely=.9, anchor="c",width=130, height=30)
tab_control.pack(expand=1, fill='both')
window.mainloop()