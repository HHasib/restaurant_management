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


lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Mastermind Food Fest",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text="-By Hasnat",fg="steel blue",anchor='center')
lblinfo.grid(row=1,column=1)


text_Input=IntVar()

def Clear():
	global Pizza
	global Burger
	global Sumi
	global Doughnut
	global Set_menu
	global Sub
	global Chicken
	global Fuchka
	global Cold_coffee
	global Drink
	Pizza = int()
	Burger = int()
	Sumi = int()
	Doughnut = int()
	Set_menu = int()
	Sub = int()
	Chicken = int()
	Fuchka = int()
	Cold_coffee = int()
	Drink = int()
	Return = int()
	Paid.set("")
	lblReturn.config(text = Return)

	txtBurger.config(text = Burger)
	txtPizza.config(text = Pizza)
	Ref()

def Ref():
	
	global total_cost
	global costofburger
	costofburger = Burger*250
	costofpizza=Pizza*100
	costofsumi = Sumi*80
	costofdoughnut = Doughnut*100
	costofset = Set_menu*300
	costofsub = Sub*120
	costofchick = Chicken*100
	costoffuchka = Fuchka*50
	costofcoffee = Cold_coffee*100
	costofdrink = Drink*40

	
	total_cost = int(costofburger + costofpizza + costofsumi + costofdoughnut + costofset + costofsub + costofchick + costoffuchka + costofcoffee + costofdrink)
	Total = "Tk. %d" %(total_cost)
	lblTotal.config(text = Total)
	lblBurger.config(text = costofburger)
	lblPizza.config(text = costofpizza)
	
	
def Return_money():
	
	pay = int(Paid.get())
	Return = "Tk. %d" %(pay - total_cost)
	lblReturn.config(text = Return)
	
def Burger_add():
	global Burger
	Burger += 1
	txtBurger.config(text = Burger)
	Ref()
	
def Pizza_add():
	global Pizza
	Pizza += 1
	txtPizza.config(text = Pizza)
	
	Ref()
def Sumi_add():
	global Sumi
	Sumi += 1
	txtSumi.config(text = Sumi)
	Ref()
	
def Doughnut_add():
	global Doughnut
	Doughnut += 1
	txtDoughnut.config(text = Doughnut)
	Ref()
	
def Set_menu_add():
	global Set_menu
	Set_menu += 1
	txtSet_menu.config(text = Set_menu)
	Ref()
def Sub_add():
	global Sub
	Sub += 1
	txtSub.config(text = Sub)
	Ref()
def Chicken_add():
	global Chicken
	Chicken += 1
	txtChicken.config(text = Chicken)
	Ref()
def Fuchka_add():
	global Fuchka
	Fuchka += 1
	txtFuchka.config(text = Fuchka)
	Ref()
def Cold_coffee_add():
	global Cold_coffee
	Cold_coffee += 1
	txtCold_coffee.config(text = Cold_coffee)
	Ref()
def Drink_add():
	global Drink
	Drink += 1
	txtDrink.config(text = Drink)
	Ref()


	
def Burger_subtract():
	global Burger
	Burger -= 1
	txtBurger.config(text = Burger)
	Ref()
	
def Pizza_subtract():
	global Pizza
	Pizza -= 1
	txtPizza.config(text = Pizza)
	
	Ref()
def Sumi_subtract():
	global Sumi
	Sumi -= 1
	txtSumi.config(text = Sumi)
	Ref()
def Doughnut_subtract():
	global Doughnut
	Doughnut -= 1
	txtDoughnut.config(text = Doughnut)
	Ref()
def Set_menu_subtract():
	global Set_menu
	Set_menu -= 1
	txtSet_menu.config(text = Set_menu)
	Ref()
def Sub_subtract():
	global Sub
	Sub -= 1
	txtSub.config(text = Sub)
	Ref()
def Chicken_subtract():
	global Chicken
	Chicken -= 1
	txtChicken.config(text = Chicken)
	Ref()
def Fuchka_subtract():
	global Fuchka
	Fuchka -= 1
	txtFuchka.config(text = Fuchka)
	Ref()
def Cold_coffee_subtract():
	global Cold_coffee
	Cold_coffee -= 1
	txtCold_coffee.config(text = Cold_coffee)
	Ref()
def Drink_subtract():
	global Drink
	Drink -= 1
	txtDrink.config(text = Drink)
	Ref()


Pizza = int()
Burger = int()
Sumi = int()
Doughnut = int()
Set_menu = int()
Sub = int()
Chicken = int()
Fuchka = int()
Cold_coffee = int()
Drink = int()
total_cost = int()
Total = int()
Paid = StringVar()
Return = int()

costofburger = int()


btnBurger=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Burger", bg="powder blue",command= Burger_add)
btnBurger.grid(row=1, column=1)
txtBurger = Label(f1,font=('ariel' ,16,'bold'), text=Pizza , bd=6,fg="powder blue" ,anchor='center', relief=GROOVE)
txtBurger.grid(row=1,column=2)
btnsubtract_burger=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Burger_subtract)
btnsubtract_burger.grid(row=1, column=3)

btnPizza=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Pizza", bg="powder blue",command= Pizza_add)
btnPizza.grid(row=2, column=1)
txtPizza = Label(f1,font=('ariel' ,16,'bold'), text=Pizza , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE )
txtPizza.grid(row=2,column=2)
btnsubtract_pizza=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Pizza_subtract)
btnsubtract_pizza.grid(row=2, column=3)

btnSumi=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Sumi", bg="powder blue",command= Sumi_add)
btnSumi.grid(row=3, column=1)
txtSumi = Label(f1,font=('ariel' ,16,'bold'), text=Sumi , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE )
txtSumi.grid(row=3,column=2)
btnsubtract_sumi=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Sumi_subtract)
btnsubtract_sumi.grid(row=3, column=3)

btnDoughnut=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Doughnut", bg="powder blue",command= Doughnut_add)
btnDoughnut.grid(row=4, column=1)
txtDoughnut = Label(f1,font=('ariel' ,16,'bold'), text=Doughnut , bd=6,fg="powder blue" ,anchor='center', relief=GROOVE)
txtDoughnut.grid(row=4,column=2)
btnsubtract_doughnut=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Doughnut_subtract)
btnsubtract_doughnut.grid(row=4, column=3)

btnSet_menu=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Set menu", bg="powder blue",command= Set_menu_add)
btnSet_menu.grid(row=5, column=1)
txtSet_menu = Label(f1,font=('ariel' ,16,'bold'), text=Set_menu , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtSet_menu.grid(row=5,column=2)
btnsubtract_set=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Set_menu_subtract)
btnsubtract_set.grid(row=5, column=3)

btnSub=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Sub", bg="powder blue",command= Sub_add)
btnSub.grid(row=6, column=1)
txtSub = Label(f1,font=('ariel' ,16,'bold'), text=Sub , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtSub.grid(row=6,column=2)
btnsubtract_sub=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Sub_subtract)
btnsubtract_sub.grid(row=6, column=3)

btnChicken=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Chicken", bg="powder blue",command= Chicken_add)
btnChicken.grid(row=7, column=1)
txtChicken = Label(f1,font=('ariel' ,16,'bold'), text=Chicken , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtChicken.grid(row=7,column=2)
btnsubtract_chick=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Chicken_subtract)
btnsubtract_chick.grid(row=7, column=3)

btnFuchka=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Fuchka", bg="powder blue",command= Fuchka_add)
btnFuchka.grid(row=8, column=1)
txtFuchka = Label(f1,font=('ariel' ,16,'bold'), text=Fuchka , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtFuchka.grid(row=8,column=2)
btnsubtract_fuchka=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Fuchka_subtract)
btnsubtract_fuchka.grid(row=8, column=3)

btnCold_coffee=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Cold coffee", bg="powder blue",command= Cold_coffee_add)
btnCold_coffee.grid(row=9, column=1)
txtCold_coffee = Label(f1,font=('ariel' ,16,'bold'), text=Cold_coffee , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtCold_coffee.grid(row=9,column=2)
btnsubtract_coffee=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Cold_coffee_subtract)
btnsubtract_coffee.grid(row=9, column=3)

btnDrink=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Drink", bg="powder blue",command= Drink_add)
btnDrink.grid(row=10, column=1)
txtDrink = Label(f1,font=('ariel' ,16,'bold'), text=Drink , bd=6,fg="powder blue" ,anchor='center',relief=GROOVE)
txtDrink.grid(row=10,column=2)
btnsubtract_drink=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=2, text="-", bg="powder blue",command= Drink_subtract)
btnsubtract_drink.grid(row=10, column=3)

lblspace = Label(f1,font=('ariel' ,16,'bold'), text="-----------------------" , bd=6,fg="white" ,anchor='e')
lblspace.grid(row=12,column=1)

lblspace = Label(f1,font=('ariel' ,16,'bold'), text="-------------" , bd=6,fg="white" ,anchor='e')
lblspace.grid(row=12,column=3)

btnclear=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Clear", bg="powder blue",command=Clear)
btnclear.grid(row=3, column=5)
#-------RIFHT SIDE------

lblBurger = Label(f2, font=( 'aria' ,16, 'bold' ),text="Burger",fg="steel blue",bd=10,anchor='w',width=10)
lblBurger.grid(row=1,column=1)
lblBurger = Label(f2, font=( 'aria' ,16, 'bold' ),text="0",fg="steel blue",bd=10,anchor='e')
lblBurger.grid(row=1,column=2)

lblPizza = Label(f2, font=( 'aria' ,16, 'bold' ),text="Pizza",fg="steel blue",bd=10,anchor='w',width=10)
lblPizza.grid(row=2,column=1)
lblPizza = Label(f2, font=( 'aria' ,16, 'bold' ),text=100*Pizza,fg="steel blue",bd=10,anchor='e')
lblPizza.grid(row=2,column=2)

lblSumi = Label(f2, font=( 'aria' ,16, 'bold' ),text="Sumi",fg="steel blue",bd=10,anchor='w',width=10)
lblSumi.grid(row=3,column=1)
lblSumi = Label(f2, font=( 'aria' ,16, 'bold' ),text=Sumi,fg="steel blue",bd=10,anchor='e')
lblSumi.grid(row=3,column=2)

lblDoughnut = Label(f2, font=( 'aria' ,16, 'bold' ),text="Doughnut",fg="steel blue",bd=10,anchor='w',width=10)
lblDoughnut.grid(row=4,column=1)
lblDoughnut = Label(f2, font=( 'aria' ,16, 'bold' ),text=Doughnut,fg="steel blue",bd=10,anchor='e')
lblDoughnut.grid(row=4,column=2)

lblSet_menu = Label(f2, font=( 'aria' ,16, 'bold' ),text="Set menu",fg="steel blue",bd=10,anchor='w',width=10)
lblSet_menu.grid(row=5,column=1)
lblSet_menu = Label(f2, font=( 'aria' ,16, 'bold' ),text=Set_menu,fg="steel blue",bd=10,anchor='e')
lblSet_menu.grid(row=5,column=2)

lblSub = Label(f2, font=( 'aria' ,16, 'bold' ),text="Sub",fg="steel blue",bd=10,anchor='w',width=10)
lblSub.grid(row=6,column=1)
lblSub = Label(f2, font=( 'aria' ,16, 'bold' ),text=Sub,fg="steel blue",bd=10,anchor='e')
lblSub.grid(row=6,column=2)

lblChicken = Label(f2, font=( 'aria' ,16, 'bold' ),text="Chicken",fg="steel blue",bd=10,anchor='w',width=10)
lblChicken.grid(row=7,column=1)
lblChicken = Label(f2, font=( 'aria' ,16, 'bold' ),text=Chicken,fg="steel blue",bd=10,anchor='e')
lblChicken.grid(row=7,column=2)

lblFuchka = Label(f2, font=( 'aria' ,16, 'bold' ),text="Fuchka",fg="steel blue",bd=10,anchor='w',width=10)
lblFuchka.grid(row=8,column=1)
lblFuchka = Label(f2, font=( 'aria' ,16, 'bold' ),text=Fuchka,fg="steel blue",bd=10,anchor='e')
lblFuchka.grid(row=8,column=2)

lblCold_coffee = Label(f2, font=( 'aria' ,16, 'bold' ),text="Cold coffee",fg="steel blue",bd=10,anchor='w',width=10)
lblCold_coffee.grid(row=9,column=1)
lblCold_coffee = Label(f2, font=( 'aria' ,16, 'bold' ),text=Cold_coffee,fg="steel blue",bd=10,anchor='e')
lblCold_coffee.grid(row=9,column=2)

lblDrink = Label(f2, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w',width=10)
lblDrink.grid(row=10,column=1)
lblDrink = Label(f2, font=( 'aria' ,16, 'bold' ),text=Drink,fg="steel blue",bd=10,anchor='e')
lblDrink.grid(row=10,column=2)


lblPaid = Label(f2, font=( 'aria' ,16, 'bold' ),text="Paid",fg="steel blue",bd=10,anchor='w',width=10)
lblPaid.grid(row=12,column=1)
txtPaid = Entry(f2,font=('ariel' ,16,'bold'), textvariable=Paid , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtPaid.grid(row=12,column=2)

lblTotal = Label(f2, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w',width=10)
lblTotal.grid(row=11,column=1)
lblTotal = Label(f2, font=( 'aria' ,16, 'bold' ),text=Total,fg="steel blue",bd=10,anchor='e')
lblTotal.grid(row=11,column=2)


btnReturn=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Return", bg="powder blue",command=Return_money)
btnReturn.grid(row=13, column=1)
lblReturn = Label(f2, font=( 'aria' ,16, 'bold' ),text=Return,fg="steel blue",bd=10,anchor='e')
lblReturn.grid(row=13,column=2)



root.mainloop()
