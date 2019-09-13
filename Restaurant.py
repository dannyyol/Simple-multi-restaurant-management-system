from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
#import addItem

def main():
    root = Tk()
    app = Restaurant(root)

class Restaurant():
    def __init__(self, master):

        self.master = master
        self.master.title("Restaurant Management Systems")
        self.master.geometry('1350x750+0+0')
        self.master.configure(background= "Cadet Blue")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Tops =Frame(self.frame, bg= 'Cadet Blue', bd=20, pady=15, padx=25, relief=RIDGE)
        self.Tops.pack(side = TOP)
        self.lblTitle = Label(self.Tops, font =('arial', 60, 'bold'), text = "Restaurant Managment Systems", bd=21, bg='Cadet Blue', fg ='CornSilk', justify=CENTER)
        self.lblTitle.grid(row=0, column=0)

        self.ReceiptCal_F = Frame(self.frame, bg="Powder Blue", bd=10, relief= RIDGE)
        self.ReceiptCal_F.pack(side=RIGHT)
        self.buttons_F = Frame(self.ReceiptCal_F, bg = "Powder Blue", bd=3, relief=RIDGE)
        self.buttons_F.pack(side=BOTTOM)
        self.Cal_F = Frame(self.ReceiptCal_F, bg = "Powder Blue", bd=6, relief=RIDGE)
        self.Cal_F.pack(side=TOP)
        self.Receipt_F = Frame(self.ReceiptCal_F, bg = "Powder Blue", bd=4, relief= RIDGE)
        self.Receipt_F.pack(side=BOTTOM)

        self.MenuFrame = Frame(self.frame, bg ='Cadet Blue', bd =10, relief= RIDGE)
        self.MenuFrame.pack(side=LEFT)
        self.Cost_F= Frame(self.MenuFrame, bg ='Powder Blue', bd=4, padx=60)
        self.Cost_F.pack(side=BOTTOM)
        self.Frame_1 = Frame(self.MenuFrame, bg = "Powder Blue", bd=10)
        self.Frame_1.pack(side= TOP)

        self.Frame_1 = Frame(self.MenuFrame, bg = "Powder Blue", bd=10, relief= RIDGE)
        self.Frame_1.pack(side= LEFT)
        self.Frame_2= Frame(self.MenuFrame, bg ='Powder Blue', width=300, height=20,bd=10, relief= RIDGE, pady=20)
        self.Frame_2.pack(side= TOP)


        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        # var12 = IntVar()
        # var13= IntVar()
        # var14= IntVar()
        # var15= IntVar()
        # var16 = IntVar()


        DateofOrder = StringVar()
        Receipt_ref = StringVar()
        PaidTax = StringVar()
        subTotal = StringVar()
        TotalCost = StringVar()
        CostofItems = StringVar()
        ServiceCharge = StringVar()

        text_input = StringVar()
        operator =""

        E_Item0 = StringVar()
        E_Item1 = StringVar()
        E_Item2 = StringVar()
        E_Item3 = StringVar()
        E_Item4 = StringVar()
        E_Item5 = StringVar()

        E_Item6 = StringVar()
        E_Item7 = StringVar()
        E_Item8= StringVar()
        E_Item9 = StringVar()
        E_Item10 = StringVar()

        E_Item0.set("0")
        E_Item1.set("0")
        E_Item2.set("0")
        E_Item3.set("0")
        E_Item4.set("0")
        E_Item5.set("0")

        E_Item6.set("0")
        E_Item7.set("0")
        E_Item8.set("0")
        E_Item9.set("0")
        E_Item10.set("0")




        E_Item01 = StringVar()
        E_Item11 = StringVar()
        E_Item21 = StringVar()
        E_Item31 = StringVar()
        E_Item41 = StringVar()
        E_Item51 = StringVar()

        E_Item61 = StringVar()
        E_Item71 = StringVar()
        E_Item81= StringVar()
        E_Item91 = StringVar()
        E_Item101 = StringVar()

        E_Item01.set("0")
        E_Item11.set("0")
        E_Item21.set("0")
        E_Item31.set("0")
        E_Item41.set("0")
        E_Item51.set("0")

        E_Item61.set("0")
        E_Item71.set("0")
        E_Item81.set("0")
        E_Item91.set("0")
        E_Item101.set("0")

        def Reset():
            PaidTax.set("")
            subTotal.set("")
            TotalCost.set("")
            CostofItems.set("")
            # Costofdrinks.set("")
            ServiceCharge.set("")
            self.txtReceipt.delete("1.0", END)

            E_Item0.set("0")
            E_Item1.set("0")
            E_Item2.set("0")
            E_Item3.set("0")
            E_Item4.set("0")
            E_Item5.set("0")

            E_Item6.set("0")
            E_Item7.set("0")
            E_Item8.set("0")
            E_Item9.set("0")
            E_Item10.set("0")

            E_Item01.set("0")
            E_Item11.set("0")
            E_Item21.set("0")
            E_Item31.set("0")
            E_Item41.set("0")
            E_Item51.set("0")

            E_Item61.set("0")
            E_Item71.set("0")
            E_Item81.set("0")
            E_Item91.set("0")
            E_Item101.set("0")

    

            self.Item0txt.configure(state=DISABLED)
            self.Item1txt.configure(state=DISABLED)
            self.Item2txt.configure(state=DISABLED)
            self.Item3txt.configure(state=DISABLED)
            self.Item4txt.configure(state=DISABLED)
            self.Item5txt.configure(state=DISABLED)

        # ++++++++++++++++++++++++++++++++++++calculator function===============
        def btnClick(numbers):
            global operator
            operator =operator + str(numbers)
            text_input.set(operator)

        def btnClear():
            global operator
            operator =""
            text_input.set("")

        def btnEquals():
            global operator
            sumup =str(eval(operator))
            text_input.set(sumup)
            operator=""

        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
            if( iExit > 0):
                self.master.destroy()
                return

        def CostofItem():
            Item1 = float(E_Item0.get())
            Item2 = float(E_Item1.get())
            Item3 = float(E_Item2.get())
            Item4 = float(E_Item3.get())
            Item5 = float(E_Item9.get())
            Item6 = float(E_Item5.get())
            Item7 = float(E_Item10.get())
            Item8 = float(E_Item6.get())
            Item9 = float(E_Item7.get())
            Item10 = float(E_Item4.get())
            Item11 = float(E_Item8.get())

            Item12 = float(E_Item01.get())
            Item13 = float(E_Item11.get())
            Item14= float(E_Item21.get())
            Item15 = float(E_Item31.get())
            Item16 = float(E_Item91.get())
            Item17= float(E_Item51.get())
            Item18 = float(E_Item101.get())
            Item19= float(E_Item61.get())
            Item20= float(E_Item71.get())
            Item21 = float(E_Item41.get())
            Item22 = float(E_Item81.get())


            PriceofItem = (Item1 * Item12) + (Item2 * Item13) + (Item3 * Item14) + (Item4 * Item15) + (Item5 * Item16) + (Item6 * Item17) \
                + (Item7 * Item18) + (Item8  * Item19) + (Item9 * Item20) + (Item10 * Item21 ) + (Item11 * Item22)

            ItemsPrice = "#"+str("%.2f"%(PriceofItem))
            CostofItems.set(ItemsPrice)
            SC = "#"+str('%.2f'%(10))
            ServiceCharge.set(SC)

            SubTotalofItems = "#"+str("%.2f"%(PriceofItem + 10))
            subTotal.set(SubTotalofItems)

            TT = ((PriceofItem + 10)* 5)
            TC = "#"+str("%.2f"%(PriceofItem + 10 + TT))
            TotalCost.set(TC)

        def chkwater():
            if (var1.get()==2):
                self.Item0txt.configure(state=NORMAL)
                self.Item0txt1.configure(state=NORMAL)
                self.Item0txt.focus()
                self.Item0txt1.focus()
                self.Item_1.delete('0', END)
                E_Item0.set("")
                E_Item01.set("")
            elif(var1.get()==0):
                self.Item0txt.configure(state=DISABLED)
                self.Item0txt1.configure(state=DISABLED)
                E_Item0.set("0")
                E_Item01.set("0")

        def chkafricancoffe():
            if (var2.get()==2):
                self.Item1txt.configure(state=NORMAL)
                self.Item1txt1.configure(state=NORMAL)
                self.Item1txt.focus()
                self.Item1txt1.focus()
                self.Item_2.delete('0', END)
                E_Item2.set("")
                E_Item21.set("")
            elif(var2.get()==0):
                self.Item1txt.configure(state=DISABLED)
                self.Item1txt1.configure(state=DISABLED)
                E_Item1.set("0")
                E_Item11.set("0")

        def chkamericacoffe():
            if (var3.get()==2):
                self.Item2txt.configure(state=NORMAL)
                self.Item2txt1.configure(state=NORMAL)
                self.Item2txt.focus()
                self.Item2txt1.focus()
                self.Item_3.delete('0', END)
                E_Item2.set("")
                E_Item21.set("")
            elif(var3.get()==0):
                self.Item2txt.configure(state=DISABLED)
                self.Item2txt1.configure(state=DISABLED)
                E_Item2.set("0")
                E_Item21.set("0")


        def chkIced_Cappuccino():
            if (var4.get()==2):
                self.Item3txt1.configure(state=NORMAL)
                self.Item3txt1.focus()
                self.Item3txt.configure(state=NORMAL)
                self.Item3txt.focus()
                self.Item_4.delete('0', END)
                E_Item3.set("")
                E_Item31.set("")
            elif(var4.get()==0):
                self.Item3txt.configure(state=DISABLED)
                self.Item3txt1.configure(state=DISABLED)
                E_Item3.set("0")
                E_Item31.set("0")

        def chkvale_coffee():
            if (var5.get()==2):
                self.Item4txt.configure(state=NORMAL)
                self.Item4txt.focus()
                self.Item4txt1.configure(state=NORMAL)
                self.Item4txt1.focus()
                self.Item_5.delete('0', END)
                E_Item4.set("")
                E_Item41.set("")
            elif(var6.get()==0):
                self.Item4txt.configure(state=DISABLED)
                self.Item4txt1.configure(state=DISABLED)
                E_Item4.set("0")
                E_Item41.set("0")

        def chklatta():
            if (var6.get()==2):
                self.Item5txt.configure(state=NORMAL)
                self.Item5txt.focus()
                self.Item5txt1.configure(state=NORMAL)
                self.Item5txt1.focus()
                self.Item_6.delete('0', END)
                E_Item5.set("")
                E_Item51.set("")
            elif(var6.get()==0):
                self.Item5txt.configure(state=DISABLED)
                self.Item5txt1.configure(state=DISABLED)
                E_Item5.set("0")
                E_Item51.set("0")

        def chkschoolcake():
            if (var7.get()==2):
                self.Item6txt.configure(state=NORMAL)
                self.Item6txt.focus()
                self.Item6txt1.configure(state=NORMAL)
                self.Item6txt1.focus()
                self.Item_7.delete('0', END)
                E_Item6.set("")
                E_Item61.set("")
            elif(var7.get()==0):
                self.Item6txt.configure(state=DISABLED)
                self.Item6txt1.configure(state=DISABLED)
                E_Item6.set("0")
                E_Item61.set("0")

        def AddItem():
            self.newWindow = Toplevel(self.master)
            self.app = Item(self.newWindow)
            self.master.withdraw()

        def chksunnycake():
            if(var8.get()==2):
                self.Item7txt.configure(state=NORMAL)
                self.Item7txt.focus()

                self.Item7txt1.configure(state=NORMAL)
                self.Item7txt1.focus()
                self.Item_8.delete('0', END)
                E_Item7.set("")
                E_Item71.set("")
            elif (var8.get()==0):
                self.Item7txt.configure(state= DISABLED)
                self.Item7txt1.configure(state= DISABLED)
                E_Item7.set("0")
                E_Item71.set("0")

        def chkwest_africa():
            if (var9.get()==2):
                self.Item8txt.configure(state=NORMAL)
                self.Item8txt.focus()
                self.Item8txt1.configure(state=NORMAL)
                self.Item8txt1.focus()
                self.Item_9.delete('0', END)
                E_Item8.set("")
                E_Item81.set("")
            elif(var9.get()==0):
                self.Item8txt.configure(state=DISABLED)
                self.Item8txt1.configure(state=DISABLED)
                E_Item8.set("0")
                E_Item81.set("0")

        def chkLagos_chhocolate_cake():
            if (var10.get()==2):
                self.Item9txt.configure(state=NORMAL)
                self.Item9txt.focus()
                self.Item9txt1.configure(state=NORMAL)
                self.Item9txt1.focus()
                self.Item_10.delete('0', END)
                E_Item9.set("")
                E_Item91.set("")
            elif(var10.get()==0):
                self.Item9txt.configure(state=DISABLED)
                self.Item9txt1.configure(state=DISABLED)
                E_Item9.set("0")
                E_Item91.set("0")

        def chkqueenCake():
            if (var11.get()==2):
                self.Item10txt.configure(state=NORMAL)
                self.Item10txt.focus()
                self.Item10txt1.configure(state=NORMAL)
                self.Item10txt1.focus()
                self.Item_11.delete('0', END)
                E_Item10.set("")
                E_Item101.set("")
            elif(var11.get()==0):
                self.Item10txt.configure(state=DISABLED)
                self.Item10txt1.configure(state=DISABLED)
                E_Item10.set("0")
                E_Item101.set("0")

        def Receipt():
            # txtReceipt.delete("1.0, END")
            x = random.randint(1021, 12390)
            randomRef = str(x)
            Receipt_ref.set("BILL" + randomRef)

            self.txtReceipt.insert(END, 'Receipt Ref:\t\t' + Receipt_ref.get()+'\t\t' + DateofOrder.get()+ "\n\n")
            self.txtReceipt.insert(END, 'Item:\t\t' + "Quantity\t\t" + "Price\t\t")
            self.txtReceipt.insert(END, 'Item 1:\t\t' + E_Item01.get() + '\t\t' +  E_Item0.get()+"\n")
            self.txtReceipt.insert(END, 'Item 2:\t\t' +  E_Item11.get() +'\t\t' + E_Item1.get()+"\n")
            self.txtReceipt.insert(END, 'Item 3:\t\t' + E_Item21.get() + '\t\t' + E_Item2.get()+"\n")
            self.txtReceipt.insert(END, 'Item 4:\t\t' + E_Item31.get() + '\t\t' + E_Item3.get()+"\n")
            self.txtReceipt.insert(END, 'Item 5:\t\t' + E_Item41.get() + '\t\t' + E_Item4.get()+"\n")
            self.txtReceipt.insert(END, 'Item 6:\t\t' + E_Item51.get() + '\t\t' + E_Item5.get()+"\n")
            self.txtReceipt.insert(END, 'Item 7:\t\t' + E_Item61.get() + '\t\t' + E_Item6.get()+"\n")
            self.txtReceipt.insert(END, 'Item 8:\t\t' + E_Item71.get() + '\t\t' +  E_Item7.get()+"\n")
            self.txtReceipt.insert(END, 'Item 9:\t\t' + E_Item81.get() + '\t\t' + E_Item8.get()+"\n")
            self.txtReceipt.insert(END, 'Item 10:\t\t' + E_Item91.get() + '\t\t' +  E_Item9.get()+"\n")
            self.txtReceipt.insert(END, 'Item 11:\t\t' + E_Item101.get() + '\t\t' + E_Item10.get()+"\n")


            self.txtReceipt.insert(END, 'subTotal:\t\t\t\t' + str(subTotal.get()) + "\nCost of Item:\t\t\t\t" + CostofItems.get()+"\n" )
            self.txtReceipt.insert(END, 'Total Cost of Items:\t\t\t\t' + TotalCost.get() + "\nService Charge:\t\t\t\t" + ServiceCharge.get()+"\n" )
            self.txtReceipt.configure(state=DISABLED)
            # txtReceipt.insert(END, 'Receipt Rf:')
        # =========================Calculator---------------------------------------
        self.txtDisplay =Entry(self.Cal_F, width = 45, justify=RIGHT, textvariable= text_input, bg="white", bd=4, font=('arial', 12, 'bold'))
        self.txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
        self.txtDisplay.insert(0, "0")


        DateofOrder.set(time.strftime("%d/%m/%Y"))



        self.Item_1 = Checkbutton(self.Frame_1, text='', variable = var1, onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chkwater).grid(row=1, sticky=W)
        self.Item_2 = Checkbutton(self.Frame_1, variable = var2, text='', onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chkafricancoffe).grid(row=2, sticky=W)
        self.Item_3 = Checkbutton(self.Frame_1, variable = var3, text='', onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chkamericacoffe).grid(row=3, sticky=W)
        self.Item_4 = Checkbutton(self.Frame_1,variable = var4, text='', onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chkIced_Cappuccino).grid(row=4, sticky=W)
        self.Item_5 = Checkbutton(self.Frame_1, variable = var5,text='\t\t', onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chkvale_coffee).grid(row=5, sticky=W)
        self.Item_6 = Checkbutton(self.Frame_1, variable = var6, text='\t\t', onvalue=2, offvalue=0, font=('arial', 18, 'bold'), \
            bg='Powder Blue', command= chklatta).grid(row=6, sticky=W)

        # -----------------------------------Entry for drinks-------------------
        self.title = Label(self.Frame_1, font =('arial', 14, 'bold'),text = "Quantity",  bd=21, bg='powder Blue', fg ='black')
        self.title.grid(row=0, column=0)

        self.title = Label(self.Frame_1, font =('arial', 14, 'bold'),text = "Price",  bd=21, bg='powder Blue', fg ='black')
        self.title.grid(row=0, column=1, sticky=W, padx=(100,0))


        self.Item0txt1 = Entry(self.Frame_1, font=('arial', 16, 'bold'), textvariable= E_Item01, bd=8, width=6, justify=LEFT, state = DISABLED)
        self.Item0txt1.grid(row =1, column = 0)

        self.Item0txt = Entry(self.Frame_1, font=('arial', 16, 'bold'), textvariable= E_Item0, bd=8, width=6, justify=LEFT, state = DISABLED)
        self.Item0txt.grid(row =1, column = 1,sticky=E)

        self.Item1txt1= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item11, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item1txt1.grid(row =2, column = 0)

        self.Item1txt= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item1, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item1txt.grid(row =2, column = 1,sticky=E)

        self.Item2txt1= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item21, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item2txt1.grid(row =3, column = 0)

        self.Item2txt= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item2, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item2txt.grid(row =3, column = 1,sticky=E)


        self.Item3txt1 = Entry(self.Frame_1, font=('arial', 16, 'bold'),textvariable= E_Item31, bd=8, width=6, justify=LEFT, state = DISABLED)
        self.Item3txt1.grid(row =4, column = 0)

        self.Item3txt = Entry(self.Frame_1, font=('arial', 16, 'bold'),textvariable= E_Item3, bd=8, width=6, justify=LEFT, state = DISABLED)
        self.Item3txt.grid(row =4, column = 1,sticky=E)

        self.Item4txt1= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item41, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item4txt1.grid(row =5, column = 0)

        self.Item4txt= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item4, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item4txt.grid(row =5, column = 1,sticky=E)

        self.Item5txt1= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item51, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item5txt1.grid(row =6, column = 0)

        self.Item5txt= Entry(self.Frame_1, font=('arial', 16, "bold"), textvariable= E_Item5, bd=8, width= 6, justify=LEFT, state= DISABLED)
        self.Item5txt.grid(row =6, column = 1,sticky=E)


        #------------------------------ Food------------------------------

        self.Item_7 = Checkbutton(self.Frame_2, text='\t \t', variable = var7, onvalue=2, offvalue=0, font=('arial', 16, 'bold'), \
            bg='Powder Blue', command= chkschoolcake).grid(row=1, sticky=W)
        self.Item_8 = Checkbutton(self.Frame_2, text='', variable = var8, onvalue=2, offvalue=0, font=('arial', 16, 'bold'), \
            bg='Powder Blue', command= chksunnycake).grid(row=2, sticky=W)
        self.Item_9 = Checkbutton(self.Frame_2, text='\t', variable = var9, onvalue=2, offvalue=0, font=('arial', 16, 'bold'), \
            bg='Powder Blue', command= chkwest_africa).grid(row=3, sticky=W)
        self.Item_10 = Checkbutton(self.Frame_2, text='\t', variable = var10, onvalue=2, offvalue=0, font=('arial', 16, 'bold'), \
            bg='Powder Blue', command= chkLagos_chhocolate_cake).grid(row=4, sticky=W)
        self.Item_11 = Checkbutton(self.Frame_2, text='\t', variable = var11, onvalue=2, offvalue=0, font=('arial', 16, 'bold'), \
            bg='Powder Blue', command= chkqueenCake).grid(row=5, sticky=W)
        # -----------------------------------------------cake txet-----------------


        self.title = Label(self.Frame_2, font =('arial', 14, 'bold'),text = "Quantity",  bd=21, bg='powder Blue', fg ='black')
        self.title.grid(row=0, column=0)

        self.title = Label(self.Frame_2, font =('arial', 14, 'bold'),text = "Price",  bd=21, bg='powder Blue', fg ='black')
        self.title.grid(row=0, column=1, sticky=W , padx=(100,0))

        self.Item6txt = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item6, bd=8, width=6, justify='left', state= DISABLED)
        self.Item6txt.grid(row =1, column=1,sticky=E)

        self.Item6txt1 = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item61, bd=8, width=6, justify='left', state= DISABLED)
        self.Item6txt1.grid(row =1, column=0)

        self.Item7txt = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item7, bd=8, width=6, justify='left', state= DISABLED)
        self.Item7txt.grid(row =2, column=1,sticky=E)

        self.Item7txt1 = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item71, bd=8, width=6, justify='left', state= DISABLED)
        self.Item7txt1.grid(row =2, column=0)

        self.Item8txt = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item8, bd=8, width=6, justify='left', state=DISABLED)
        self.Item8txt.grid(row =3, column=1,sticky=E)

        self.Item8txt1 = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item81, bd=8, width=6, justify='left', state=DISABLED)
        self.Item8txt1.grid(row =3, column=0)

        self.Item9txt = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item9, bd=8, width=6, justify='left', state= DISABLED)
        self.Item9txt.grid(row =4, column=1,sticky=E)

        self.Item9txt1 = Entry(self.Frame_2, font=('arial', 16, 'bold'), textvariable= E_Item91, bd=8, width=6, justify='left', state= DISABLED)
        self.Item9txt1.grid(row =4, column=0)

        self.Item10txt = Entry(self.Frame_2, font=('arial', 16, 'bold'),textvariable= E_Item10, bd=8, width=6, justify='left', state=DISABLED)
        self.Item10txt.grid(row =5, column=1,sticky=E)

        self.Item10txt1 = Entry(self.Frame_2, font=('arial', 16, 'bold'),textvariable= E_Item101, bd=8, width=6, justify='left', state=DISABLED)
        self.Item10txt1.grid(row =5, column=0)


        # =========================Total Cost---------------------------------------

        self.lblCostofItems = Label(self.Cost_F, font =('arial', 14, 'bold'), text = "Cost of Cakes", bd=21, bg='powder Blue', fg ='black')
        self.lblCostofItems.grid(row=1, column=0, sticky=W)
        self.txtCostofItems = Entry(self.Cost_F, font =('arial', 14, 'bold'), bd=7, bg='white', insertwidth=2, justify= RIGHT, textvariable=CostofItems)
        self.txtCostofItems.grid(row=1, column=1)

        self.lblServiceCharge = Label(self.Cost_F, font =('arial', 14, 'bold'), text = "Serivice Charge", bd=21, bg='powder Blue', fg ='black')
        self.lblServiceCharge.grid(row=2, column=0, sticky=W)
        self.txtServiceCharge = Entry(self.Cost_F, font =('arial', 14, 'bold'),  bd=7, bg='white', insertwidth=2, justify= RIGHT, textvariable=ServiceCharge)
        self.txtServiceCharge.grid(row=2, column=1)

        # ++++++++++++++++++++++++++++++++++++ Payment Infomation==================

        self.lblSubTotal = Label(self.Cost_F, font=("arial", 14, 'bold'), text= "Sub Total", bd=7, bg="powder blue", fg="black")
        self.lblSubTotal.grid(row =1, column=2, sticky=E)
        self.txtSubTotal  = Entry(self.Cost_F, font =('arial', 14, 'bold'),  bd=7, bg='white', insertwidth=2, justify= RIGHT, textvariable=subTotal)
        self.txtSubTotal.grid(row=1, column=3)

        self.lbltotalCost = Label(self.Cost_F, font=("arial", 14, 'bold'), text= "Total Cost", bd=7, bg="powder blue", fg="black")
        self.lbltotalCost.grid(row =2, column=2, sticky=E)
        self.txtTotalCost = Entry(self.Cost_F, font=("arial", 14, 'bold'), bd =7, bg="white", insertwidth=2, justify=RIGHT, textvariable=TotalCost)
        self.txtTotalCost.grid(row =2, column=3)
        # =========================receipt---------------------------------------
        self.txtReceipt =Text(self.Receipt_F, width = 46, height=8, bg="white", bd=4, font=('arial', 12, 'bold'))
        self.txtReceipt.grid(row=2, column=3)

        # ----------------------------------Button-------------------------------------
        self.btnTotal = Button(self.buttons_F, padx=16,pady=1, bd=7, fg= "black", command=CostofItem, font=('arial', 16, 'bold'), width=4, text = 'Total', bg='Powder Blue').grid(row=0, column=0)

        self.btnReceipt = Button(self.buttons_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = 'Receipt', bg='Powder Blue', command=Receipt).grid(row=0, column=1)

        self.btnReset = Button(self.buttons_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = 'Reset', bg='Powder Blue', command=Reset).grid(row=0, column=2)

        self.btnExit = Button(self.buttons_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = 'Exit', bg='Powder Blue', command=iExit).grid(row=0, column=3)


        # ----------------------------------Button-------------------------------------
        self.btn7 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '7', \
            bg='Powder Blue', command= lambda:btnClick(7)).grid(row=2, column=0)

        self.btn8 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '8', \
            bg='Powder Blue', command= lambda:btnClick(8)).grid(row=2, column=1)

        self.btn9 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '9', \
            bg='Powder Blue', command= lambda:btnClick(9)).grid(row=2, column=2)

        self.btnAdd = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '+', \
            bg='Powder Blue', command= lambda:btnClick("+")).grid(row=2, column=3)

        # ----------------------------------Button-------------------------------------
        self.btn4 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '4', \
            command= lambda:btnClick(4)).grid(row=3, column=0)

        self.btn5 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '5', \
            command= lambda:btnClick(5)).grid(row=3, column=1)

        self.btn6 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '6', \
            command= lambda:btnClick(6)).grid(row=3, column=2)

        self.btnSubstract = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '-', \
            bg='Powder Blue', command= lambda:btnClick("-")).grid(row=3, column=3)
            # ----------------------------------Button-------------------------------------
        self.btn1 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '1', \
            command= lambda:btnClick(1)).grid(row=4, column=0)

        self.btn2 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '2', \
            command= lambda:btnClick(2)).grid(row=4, column=1)

        self.btn3 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '3', \
            command= lambda:btnClick(3)).grid(row=4, column=2)

        self.btnMultiplication = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '*', \
            bg='Powder Blue', command= lambda:btnClick('*')).grid(row=4, column=3)

            # ----------------------------------Button-------------------------------------
        self.btn0 = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '0', \
            bg='Powder Blue', command= lambda:btnClick(0)).grid(row=5, column=0)

        self.btnClear = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = 'C', \
            bg='Powder Blue', command= btnClear).grid(row=5, column=1)

        self.btnEquals = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '=', \
            bg='Powder Blue', command= btnEquals).grid(row=5, column=2)

        self.btnDiv = Button(self.Cal_F, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '/', \
            bg='Powder Blue', command= lambda:btnClick("/")).grid(row=5, column=3)


class Item():
    def __init__(self, master):

        self.master = master
        self.master.title("Restaurant Management Systems")
        self.master.geometry('1350x750+0+0')
        self.master.configure(background= "Cadet Blue")
        self.frame = Frame(self.master)
        self.frame.pack()

        def home():
            # self.Window = Toplevel(self.master)
            # self.app = Item(self.Window)
            # self.master.withdraw()

            self.master.withdraw()


        self.btn1 = Button(self.frame, padx=16,pady=1, bd=7, fg= "black", font=('arial', 16, 'bold'), width=4, text = '1', \
            command=home).grid(row=4, column=0)

if __name__ == '__main__':
    main()
