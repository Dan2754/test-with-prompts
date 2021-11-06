from tkinter import *

window = Tk()
window.title("Контрольная работа по физике")
window.geometry('1920x1080')
lbl = Label(window, text="Привет", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
btn = Button(window, text="Далее", command=open file)
btn.grid(column=0, row=20)
window.mainloop()