from tkinter import*
import xlsxwriter
from tkinter import messagebox
myw=Tk()
wb=xlsxwriter.Workbook('D:\\Hello2.xlsx')
ws=wb.add_worksheet()
myw.geometry("800x900")
myw.title("CAMBRIDGE INSTITUTE OF TECHNOLOGY")
lbl1=Label(text="ROLL NUMBER")
lbl1.place(x=20,y=20)
e1=Entry(myw)
e1.place(x=150,y=22)
lbl2=Label(text="STUDENT NAME")
lbl2.place(x=20,y=60)
e2=Entry(myw)
e2.place(x=150,y=60)
lbl3=Label(text="SUBJECT 1")
lbl3.place(x=20,y=100)
e3=Entry(myw)
e3.place(x=150,y=100)
lbl4=Label(text="SUBJECT 2")
lbl4.place(x=20,y=140)
e4=Entry(myw)
e4.place(x=150,y=140)
lbl5=Label(text="SUBJECT 3")
lbl5.place(x=20,y=180)
e5=Entry(myw)
e5.place(x=150,y=180)
lbl6=Label(text="TOTAL")
lbl6.place(x=20,y=220)
e6=Entry(myw)
e6.place(x=150,y=220)
lbl7=Label(text="AVERAGE")
lbl7.place(x=20,y=260)
e7=Entry(myw)
e7.place(x=150,y=260)
def f1():
 for i in range(0,5):
    rno = int(e1.get())
    name = e2.get()
    sub1 = int(e3.get())
    sub2 = int(e4.get())
    sub3 = int(e5.get())
    tot = sub1 + sub2 + sub3
    avg = tot / 3
    l1=[]
    l1.append(rno)
    l1.append(name)
    l1.append(sub1)
    l1.append(sub2)
    l1.append(sub3)
    l1.append(tot)
    l1.append(avg)
    for i, data in enumerate(l1):
        ws.write(i,0,data)
 if (i == 5):
    wb.close()

b1=Button(myw,text="BUTTON",fg="black",bg="red",command=f1)
b1.place(x=150,y=300)
myw.mainloop()

