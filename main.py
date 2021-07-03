from tkinter import *
window=Tk()
window.geometry("700x500")

def calculate():
    Ambuja=e1.get()
    Altratech=e2.get()
    ACC=e3.get()
    Birla=e4.get()



    total=((int(Ambuja)*400+int(Altratech)*350+int(ACC)*370+int(Birla)*390))


    label12 = Label(window, text=total, font="times 28 bold")
    label12.place(x=100, y=400)

    label13 = Label(window, text="total", font="times 28 bold")
    label13.place(x=100, y=360)


label1=Label(window,text="Kaushik Cement Retailers and Suplier",font="times 30 bold")
label1.place(x=350,y=20,anchor="center")
label14=Label(window,text="Note- The Rate Shown Below are Per Bag",font="times 18 bold")
label14.place(x=350,y=60,anchor="center")


#----------------Cement Brand section----------



label1=Label(window,text="Kaushik Cement Retailers and Suplier",font="times 30 bold")
label1.place(x=350,y=20,anchor="center")

label2=Label(window,text="Cement Brand",font="times 28 bold")
label2.place(x=550,y=70)



label3=Label(window,text="Ambuja            400 Rs",font="times 18 bold")
label3.place(x=450,y=120)

label4=Label(window,text="Ultratech         350 Rs",font="times 18 bold")
label4.place(x=450,y=150)


label5=Label(window,text="ACC                 370 Rs",font="times 18 bold")
label5.place(x=450,y=180)


label6=Label(window,text="Birla                 390 Rs",font="times 18 bold")
label6.place(x=450,y=210)

#-------------billing section----------------
label7=Label(window,text="Select the items",font="times 20 bold")
label7.place(x=70,y=70)

label8=Label(window,text="Ambuja",font="times 18 bold")
label8.place(x=20,y=120)

e1=Entry(window)
e1.insert(0,"0")
e1.place(x=20,y=150)

label9=Label(window,text="Ultratech",font="times 18 bold")
label9.place(x=250,y=120)

e2=Entry(window)
e2.insert(0,"0")
e2.place(x=250,y=150)

label10=Label(window,text="ACC",font="times 18 bold")
label10.place(x=20,y=200)

e3=Entry(window)
e3.insert(0,"0")
e3.place(x=20,y=230)

label11=Label(window,text="Birla",font="times 18 bold")
label11.place(x=250,y=200)

e4=Entry(window)
e4.insert(0,"0")
e4.place(x=250,y=230)

b2=Button(window,text="bill",width=20,command=calculate)
b2.place(x=100,y=300)
window.mainloop()

