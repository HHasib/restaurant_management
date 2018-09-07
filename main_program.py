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


#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="MASTERMIND FOOD FEST",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)



status = Label(f2 ,font=('aria', 15, 'bold'),width = 20, text="-By Abu Hasnat Hasib",bd=2,relief=SUNKEN)

status.grid(row=7,column=2)	


text_Input=IntVar()
operator =""






def qexit():
    root.destroy()

def reset():
    Pizza.set(0)
    Sub.set(0)
    Burger.set(0)
    Donut.set(0)
    Sumis.set(0)
    Set_menu.set(0)
    Chicken.set(0)
    Drinks.set(0)
    Cold_coffee.set(0)
    Total.set(0)
    
  
	
def Ref():
   
#receives the total price
    copi =float(Pizza.get())
    cosub= float(Sub.get())
    cobu= float(Burger.get())
    codo= float(Donut.get())
    cosumi= float(Sumis.get())
    coset= float(Set_menu.get())
    coch= float(Chicken.get())
    codr= float(Drinks.get())
    coco= float(Cold_coffee.get())
	
#change the price of meals here
    costofpizza = copi*150
    costofsub =  cosub*150
    costofburger = cobu*200
    costofdonut = codo*120
    costofsumis = cosumi*120
    costofsetmenu = coset*300
    costofchicken = coch*120
    costofdrinks = codr*20
    costofcoldcoffee = coco*80
#cost of total meal
    costofmeal = "Tk.",float('%.2f'% (costofpizza +  costofsub + costofburger + costofdonut + costofsumis + costofsetmenu + costofchicken + costofdrinks + costofcoldcoffee))
    
    
    Total.set(costofmeal)	
	
	
#---------------------------------------------------------------------------------------

Pizza = IntVar()
Sub = IntVar()
Burger = IntVar()
Donut = IntVar()
Sumis = IntVar()
Set_menu = IntVar()
Chicken = IntVar()
Drinks = IntVar()
Cold_coffee = IntVar()
Total = IntVar()



lblPizza = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza",fg="steel blue",bd=10,anchor='w')
lblPizza.grid(row=1,column=0)
txtPizza = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pizza , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtPizza.grid(row=1,column=1)

lblSub = Label(f1, font=( 'aria' ,16, 'bold' ),text="Sub",fg="steel blue",bd=10,anchor='w')
lblSub.grid(row=2,column=0)
txtSub = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Sub , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtSub.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtburger.grid(row=3,column=1)

lblDonut = Label(f1, font=( 'aria' ,16, 'bold' ),text="Doughnut",fg="steel blue",bd=10,anchor='w')
lblDonut.grid(row=4,column=0)
txtDonut = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Donut , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtDonut.grid(row=4,column=1)

lblSumis = Label(f1, font=( 'aria' ,16, 'bold' ),text="Sumi's",fg="steel blue",bd=10,anchor='w')
lblSumis.grid(row=5,column=0)
txtSumis = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Sumis , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtSumis.grid(row=5,column=1)


lblSet_menu = Label(f1, font=( 'aria' ,16, 'bold' ),text="Set_menu",fg="steel blue",bd=10,anchor='w')
lblSet_menu.grid(row=1,column=2)
txtSet_menu = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Set_menu , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtSet_menu.grid(row=1,column=3)

lblChicken = Label(f1, font=( 'aria' ,16, 'bold' ),text="Chicken",fg="steel blue",bd=10,anchor='w')
lblChicken.grid(row=2,column=2)
txtChicken = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Chicken , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtChicken.grid(row=2,column=3)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=3,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtDrinks.grid(row=3,column=3)



#--------------------------------------------------------------------------------------
lblCold_coffee = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cold coffee",fg="steel blue",bd=10,anchor='w')
lblCold_coffee.grid(row=4,column=2)
txtCold_coffee = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cold_coffee , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtCold_coffee.grid(row=4,column=3)



lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)
	
	


	



root.mainloop()
	

