from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("MASTERMIND FOOD FEST")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

bottom = Frame(root,bg="white",width = 1600,height=20,relief=SUNKEN)
bottom.pack(side=BOTTOM)



text_Input=IntVar()

def Ref():
	
	global Total
	costofpizza = Pizza*200
	costofburger = Burger*150
	
	total_cost = float(costofburger +costofpizza)
	Total = total_cost
	lblTotal.config(text = Total)
	
	
def Burger_add():
	global Burger
	Burger += 1
	txtBurger.config(text = Burger)
	
def Pizza_add():
	global Pizza
	Pizza += 1
	txtPizza.config(text = Pizza)
	
global Pizza
global Burger
global Total
Pizza = 0
Burger = 0
Total = 0


lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text=Total,fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=1,column=3)

btnBurger=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Burger", bg="powder blue",command= Burger_add)
btnBurger.grid(row=1, column=0)

txtBurger = Label(f1,font=('ariel' ,16,'bold'), text=Pizza , bd=6,fg="powder blue" ,anchor='w')
txtBurger.grid(row=1,column=1)

btnPizza=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Pizza", bg="powder blue",command= Pizza_add)
btnPizza.grid(row=2, column=0)
txtPizza = Label(f1,font=('ariel' ,16,'bold'), text=Pizza , bd=6,fg="powder blue" ,anchor='w')
txtPizza.grid(row=2,column=1)


btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=1, column=2)


root.mainloop()