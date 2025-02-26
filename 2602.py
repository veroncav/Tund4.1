from tkinter import *
def Lahenda():
deg Graafik():
def aken():
 aken=Tk()
 aken.geometry("650x260")
 aken.title("Ruutvorrand")
 f1=Frame(aken,width=650,height=260)
 f1.pack()
 lbl=Label(f1,text="Ruutvorrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
 lb.pack(side=TOP)
 lbl_vastus=Label(f1,text="Lahendamine",height=4, width=60, bg="yellow")
 lbl_vastus.pack(side=BOTTOM)
 lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
 lbl_a.pack(side=LEFT)
 x2=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
 x2.pack(side=LEFT)
 lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
 lbl_a.pack(side=LEFT)
 x=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
 x.pack(side=LEFT)
 lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
 lbl_a.pack(side=LEFT)
 y=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
 y.pack(side=LEFT)
 btn_lahenda=Button(f1,text="Lahenda", font="=Clibri 26", fg="green", command=Lahenda)
 btn_lahenda.pack(side=LEFT)
 btn_graafik=Button(f1,text="Graafik", font="=Clibri 26", fg="green", command=Graafik)
 btn_graafika.pack(side=LEFT)
 aken.mainloop()

 aken()



