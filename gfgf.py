import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)

app = tk.Tk()
app.geometry('1920x1080')
buttonExample = tk.Button(app,
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()