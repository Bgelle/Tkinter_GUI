from tkinter import*
from tkinter import messagebox
myw=Tk()
myw.geometry("800x900")
myw.title("Welcome to SBI Bank")
myw.config(bg="yellow")
lb1=Label(myw,text="username",fg="red",font=('arial',15),bg="yellow")
lb1.place(x=10,y=20)
tf1=Entry(myw)
tf1.place(x=150,y=22)
lb2=Label(myw,text="password",fg="blue",font=('arial',15),bg="yellow")
lb2.place(x=11,y=60)
tf2=Entry(myw,show="*")
tf2.place(x=150,y=65)
def f1():
    name=tf1.get()
    pwd=tf2.get()
    if(name=="xyz" and pwd=="123"):
        messagebox.showinfo("correct UN and PWD","correct UN and PWD")
    else:
        messagebox.showwarning("Incorrect UN or PWD","Incorrect UN or PWD")
b1=Button(myw,text="click here",fg="red",bg="yellow",command=f1)
b1.place(x=150,y=150)
myw.mainloop()