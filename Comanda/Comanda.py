from tkinter import *
import tkinter.messagebox as tkMessageBox
import random
import time;
import datetime

root = Tk()
root.title("Novo Cadastro")
root.geometry("1200x700+0+0")
root.configure(bg='red')

LeftmainFrame = Frame(root, width=1200, height=700, bg='green', bd=8, relief="raise")
LeftmainFrame.pack(side=LEFT)

RightmainFrame = Frame(root, width=400, height=700, bd=8, relief="raise", bg='red')
RightmainFrame.pack(side=RIGHT)



LeftmainFrame0 = Frame(LeftmainFrame, width=400, height=75, bd=8, relief="raise", bg='black')
LeftmainFrame0.pack(side=TOP)

lblTitle = Label(LeftmainFrame0, font=('arial', 74, 'bold'), text='Comanda', bd=8, bg='lightsalmon')
lblTitle.grid(row=0, column=0, sticky=W)



LeftmainFrame1 = Frame(LeftmainFrame, width=1000, height=225, bd=8, relief="raise", bg='sandybrown')
LeftmainFrame1.pack(side=TOP)
LeftmainFrame2 = Frame(LeftmainFrame, width=1000, height=225, bd=8, bg='moccasin', relief="raise")
LeftmainFrame2.pack(side=TOP)
LeftmainFrame3 = Frame(LeftmainFrame, width=1000, height=100, bd=8, relief="raise", bg='lightskyblue')
LeftmainFrame3.pack(side=TOP)
LeftmainFrame4 = Frame(LeftmainFrame, width=1000, height=100, bd=8, relief="raise")
LeftmainFrame4.pack(side=TOP)

RightmainFrame1 = Frame(RightmainFrame, width=350, height=325, bd=8, relief="raise", bg='lightskyblue')
RightmainFrame1.pack(side=TOP)

RightmainFrame2 = Frame(RightmainFrame, width=380, height=325, bd=9, relief="raise")
RightmainFrame2.pack(side=BOTTOM)



def FoodRentalCost():
    NoofDays = float(NumberFood.get())
    FoodDiscountFood = float(DiscountFood.get())
    DailyRate = float(FoodDays.get())

    RentalCost = ((NoofDays * DailyRate) * FoodDiscountFood) / 25
    CostofRental = "£", str('%.2f' % ((NoofDays * DailyRate) - RentalCost))
    Total.set(CostofRental)

    ID = random.randint(32, 65)
    randomID = str(ID)
    CustomerFoodID.set("Food" + randomID)

    Inv = random.randint(24, 300)
    InvID = str(Inv)
    InvoiceFood.set("INV" + InvID)
    
    
    
    Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
Var5 = IntVar()
Var6 = IntVar()
Var7 = IntVar()
Var8 = IntVar()
CustomerFoodID = StringVar()
FoodDays = StringVar()
DiscountFood = StringVar()
NumberFood = StringVar()
InvoiceFood = StringVar()
RegistrationFood = StringVar()
IssueFood = StringVar()
FoodDate = StringVar()
Title = StringVar()
CustomerFood = StringVar()
FoodCode = StringVar()
Total = StringVar()
Receipt_Ref_Foof = StringVar()
DateofFood = StringVar()
LicenceFood = StringVar()
SurFood = StringVar()
StreetFood = StringVar()
ComandName = StringVar()
EngineFood = StringVar()
StyleFood = StringVar()
RegisteredFoodYear = StringVar()
ClassFood = StringVar()
FoodDescription = StringVar()
FoodBefore = StringVar()
FoodAfter = StringVar()
MilkShake = StringVar()
FoodModel = StringVar()
FoodColor = StringVar()
EngineMilkShake = StringVar()
FoodInsurance = StringVar()
Infantil = StringVar()
DailyFood = StringVar()



def Exit():
    result = tkMessageBox.askquestion("Novo Cadastro:")
    if result == 'yes':
        root.destroy()
        return
    
    
    
def Reset():
    Var1.set(0)
    Var2.set(0)
    Var3.set(0)
    Var4.set(0)
    Var5.set(0)
    Var6.set(0)
    Var7.set(0)
    Var8.set(0)
    CustomerFoodID.set("")
    FoodDays.set("")
    NumberFood.set("")
    InvoiceFood.set("")
    Total.set("")
    Receipt_Ref_Foof.set("")
    DiscountFood.set("")
    DateofFood.set("")
    EngineFood.set("")
    StyleFood.set("")
    RegisteredFoodYear.set("")
    ClassFood.set("")
    FoodDescription.set("")
    FoodBefore.set("")
    FoodAfter.set("")
    MilkShake.set("")
    FoodModel.set("")
    FoodColor.set("")
    EngineMilkShake.set("")
    FoodInsurance.set("")
    Infantil.set("")
    DailyFood.set("")
    RegistrationFood.set("")
    IssueFood.set("")
    FoodDate.set("")
    LicenceFood.set("")
    SurFood.set("")
    StreetFood.set("")
    ComandName.set("")
    Title.set("")
    CustomerFood.set("")
    FoodCode.set("")
    txtReceipt.delete("1.0", END)
    
    
    
    def retrive_imput():
        imputValue = txtReceipt.get("1.0", "end-1c")
    print(imputValue)
    
    
    
    def Receipt():
        txtReceipt.delete("1.0", END)
    x = random.randint(108, 506)
    randomRef = str(x)
    Receipt_Ref_Foof.set("BILL" + randomRef)

    txtReceipt.insert(END, 'RCIBO Ref:\t' + Receipt_Ref_Foof.get() + '\n\nData:\t' + DateofFood.get() + "\n\n")
    txtReceipt.insert(END, "Servicos: \n\n")

    txtReceipt.insert(END, 'ClienteID: \t' + CustomerFoodID.get() + "\n\n")

    txtReceipt.insert(END, 'Valor Infantil: \t\t' + FoodDays.get() + "\n\n")

    txtReceipt.insert(END, 'Qtos Dias: \t\t' + NumberFood.get() + "\n\n")

    txtReceipt.insert(END, 'ReciboID: \t\t' + InvoiceFood.get() + "\n\n")

    txtReceipt.insert(END, 'Tipo: \t\t' + DiscountFood.get() + "\n\n")

    txtReceipt.insert(END, 'Total: \t' + Total.get() + "\n\n")
    
    
    
    
txtReceipt = Text(RightmainFrame2, height=17, width=30, bd=8, bg='lemonchiffon', font=('arial', 12, 'bold'))
txtReceipt.grid(row=0, column=0)

DateofFood.set(time.strftime("%d/%m/%y"))



lblCustomerFood = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Cliente   :', bd=8, bg='sandybrown')
lblCustomerFood.grid(row=0, column=0, sticky=W)
txtCustomerFood = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=CustomerFood, width=31, justify='left')
txtCustomerFood.grid(row=0, column=1)

lblTitle = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Comanda   :', bd=8, bg='sandybrown')
lblTitle.grid(row=0, column=2, sticky=W)
txtTitle = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=Title, width=31, justify='left')
txtTitle.grid(row=0, column=3)

lblComandName = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Mesa   :', bd=8, bg='sandybrown')
lblComandName.grid(row=0, column=4, sticky=W)
txtComandName = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=ComandName, width=31, justify='left')
txtComandName.grid(row=0, column=5)

lblSurFood = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Cadeira   :', bd=8, bg='sandybrown')
lblSurFood.grid(row=1, column=0, sticky=W)
txtSurFood = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=SurFood, width=31, justify='left')
txtSurFood.grid(row=1, column=1)

lblStreetFood = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Adulto   :', bd=8, bg='sandybrown')
lblStreetFood.grid(row=1, column=2, sticky=W)
txtStreetFood = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=StreetFood, width=31, justify='left')
txtStreetFood.grid(row=1, column=3)

lblInfantil = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Infantil   :', bd=8, bg='sandybrown')
lblInfantil.grid(row=1, column=4, sticky=W)
txtInfantil = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=Infantil, width=31, justify='left')
txtInfantil.grid(row=1, column=5)

lblFoodCode = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Reserva  :', bd=8, bg='sandybrown')
lblFoodCode.grid(row=2, column=0, sticky=W)
txtFoodCode = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=FoodCode, width=31, justify='left')
txtFoodCode.grid(row=2, column=1)

lblLicenceFoodo = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Hora   :', bd=8, bg='sandybrown')
lblLicenceFoodo.grid(row=2, column=2, sticky=W)
txtLicenceFoodo = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=LicenceFood, width=31, justify='left')
txtLicenceFoodo.grid(row=2, column=3)

lblFoodDate = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Data  :', bd=8, bg='sandybrown')
lblFoodDate.grid(row=2, column=4, sticky=W)
txtFoodDate = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=FoodDate, width=31, justify='left')
txtFoodDate.grid(row=2, column=5)

lblIssueFood = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Rodizio   :', bd=8, bg='sandybrown')
lblIssueFood.grid(row=3, column=0, sticky=W)
txtIssueFood = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=IssueFood, width=31, justify='left')
txtIssueFood.grid(row=3, column=1)

lblRegistrationFood = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Buffet   :', bd=8, bg='sandybrown')
lblRegistrationFood.grid(row=3, column=2, sticky=W)
txtRegistrationFood = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=RegistrationFood, width=31, justify='left')
txtRegistrationFood.grid(row=3, column=3)

lblRentalRate = Label(LeftmainFrame1, font=('arial', 11, 'bold'), text='Observações   :', bd=8, bg='sandybrown')
lblRentalRate.grid(row=3, column=4, sticky=W)
txtRentalRate = Entry(LeftmainFrame1, font=('arial', 10, 'bold'), bd=2, textvariable=DailyFood, width=31, justify='left')
txtRentalRate.grid(row=3, column=5)




lblEngineFood = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Café da Manhã:', bd=8, bg='moccasin')
lblEngineFood.grid(row=0, column=0, sticky=W)
txtEngineFood = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=EngineFood, width=31, justify='left')
txtEngineFood.grid(row=0, column=1)

lblStyleFood = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Almoço:', bd=8, bg='moccasin')
lblStyleFood.grid(row=0, column=2, sticky=W)
txtStyleFood = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=StyleFood, width=31, justify='left')
txtStyleFood.grid(row=0, column=3)

lblRegisteredFoodYear = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Jantar:', bd=8, bg='moccasin')
lblRegisteredFoodYear.grid(row=0, column=4, sticky=W)
txtRegisteredFoodYear = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=RegisteredFoodYear, width=31, justify='left')
txtRegisteredFoodYear.grid(row=0, column=5)

lblClassFood = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Regional:', bd=8, bg='moccasin')
lblClassFood.grid(row=1, column=0, sticky=W)
txtClassFood = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=ClassFood, width=31, justify='left')
txtClassFood.grid(row=1, column=1)

lblFoodDescription = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Oriental:', bd=8, bg='moccasin')
lblFoodDescription.grid(row=1, column=2, sticky=W)
txtFoodDescription = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodDescription, width=31, justify='left')
txtFoodDescription.grid(row=1, column=3)

lblFoodBefore = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Vegetariana:', bd=8, bg='moccasin')
lblFoodBefore.grid(row=1, column=4, sticky=W)
txtFoodBefore = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodBefore, width=31, justify='left')
txtFoodBefore.grid(row=1, column=5)

lblFoodAfter = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Lanche:', bd=8, bg='moccasin')
lblFoodAfter.grid(row=2, column=0, sticky=W)
txtFoodAfter = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodAfter, width=31, justify='left')
txtFoodAfter.grid(row=2, column=1)

lblMilkShake = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Petisco:', bd=8, bg='moccasin')
lblMilkShake.grid(row=2, column=2, sticky=W)
txtMilkShake = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=MilkShake, width=31, justify='left')
txtMilkShake.grid(row=2, column=3)

lblFoodModel = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Doceria:', bd=8, bg='moccasin')
lblFoodModel.grid(row=2, column=4, sticky=W)
txtFoodModel = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodModel, width=31, justify='left')
txtFoodModel.grid(row=2, column=5)

lblEngineMilkShake = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Salgados:', bd=8, bg='moccasin')
lblEngineMilkShake.grid(row=3, column=0, sticky=W)
txtEngineMilkShake = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=EngineMilkShake, width=31, justify='left')
txtEngineMilkShake.grid(row=3, column=1)

lblFoodColor = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Parcerias:', bd=8, bg='moccasin')
lblFoodColor.grid(row=3, column=2, sticky=W)
txtFoodColor = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodColor, width=31, justify='left')
txtFoodColor.grid(row=3, column=3)

lblFoodInsurance = Label(LeftmainFrame2, font=('arial', 11, 'bold'), text='Alcoolicas:', bd=8, bg='moccasin')
lblFoodInsurance.grid(row=3, column=4, sticky=W)
txtFoodInsurance = Entry(LeftmainFrame2, font=('arial', 10, 'bold'), bd=2, textvariable=FoodInsurance, width=31, justify='left')
txtFoodInsurance.grid(row=3, column=5)




lblCustomerFoodID = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Telefone :', bd=8, bg='lightskyblue')
lblCustomerFoodID.grid(row=0, column=0, sticky=W)
txtCustomerFoodID = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=CustomerFoodID, width=31, justify='left')
txtCustomerFoodID.grid(row=0, column=1)

lblFoodDays = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Email :', bd=8, bg='lightskyblue')
lblFoodDays.grid(row=0, column=2, sticky=W)
txtFoodDays = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=FoodDays, width=31, justify='left')
txtFoodDays.grid(row=0, column=3)

lblDiscountFood = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Tipo :', bd=8, bg='lightskyblue')
lblDiscountFood.grid(row=0, column=4, sticky=W)
txtDiscountFood = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=DiscountFood, width=31, justify='left')
txtDiscountFood.grid(row=0, column=5)

lblNumberFood = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Contrato :', bd=8, bg='lightskyblue')
lblNumberFood.grid(row=1, column=0, sticky=W)
txtNumberFood = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=NumberFood, width=31, justify='left')
txtNumberFood.grid(row=1, column=1)

lblInvoiceFood = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Desconto :', bd=8, bg='lightskyblue')
lblInvoiceFood.grid(row=1, column=2, sticky=W)
txtInvoiceFood = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=InvoiceFood, width=31, justify='left')
txtInvoiceFood.grid(row=1, column=3)

lblTotal = Label(LeftmainFrame3, font=('arial', 11, 'bold'), text='Total  :', bd=8, bg='lightskyblue') 
lblTotal.grid(row=1, column=4, sticky=W)
txtTotal = Entry(LeftmainFrame3, font=('arial', 10, 'bold'), bd=2, textvariable=Total, width=31, justify='left')
txtTotal.grid(row=1, column=5)





style = Checkbutton(RightmainFrame1, text='Alergico\t\t\t', onvalue=1, offvalue=0, variable=Var1, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=0, sticky=W)
style = Checkbutton(RightmainFrame1, text='Vegano\t\t\t', onvalue=1, offvalue=0, variable=Var2, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=1, sticky=W)
style = Checkbutton(RightmainFrame1, text='Religioso\t\t\t', onvalue=1, offvalue=0, variable=Var3, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=2, sticky=W)
style = Checkbutton(RightmainFrame1, text='Infantil\t\t\t', onvalue=1, offvalue=0, variable=Var4, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=3, sticky=W)
style = Checkbutton(RightmainFrame1, text='Livre Demanda\t\t', onvalue=1, offvalue=0, variable=Var5, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=4, sticky=W)
style = Checkbutton(RightmainFrame1, text='Sem Lactose \t', onvalue=1, offvalue=0, variable=Var6, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=5, sticky=W)
style = Checkbutton(RightmainFrame1, text='Pets\t\t', onvalue=1, offvalue=0, variable=Var7, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=6, sticky=W)
style = Checkbutton(RightmainFrame1, text='Ver Observações\t\t', onvalue=1, offvalue=0, variable=Var8, bg='lightskyblue', font=('arial', 12, 'bold')).grid(row=7, sticky=W)


btnTotal = Button(LeftmainFrame4, text='TOTAL', padx=6, bd=3, fg='yellow', bg='black', font=('arial', 10, 'bold'), width=22, height=2, command=FoodRentalCost).grid(row=0, column=0)

btnReceipt = Button(LeftmainFrame4, text='Recibo', padx=6, bd=3, fg='yellow', bg='black', font=('arial', 10, 'bold'), width=22, height=2, command=Receipt).grid(row=0, column=2)

btnReset = Button(LeftmainFrame4, text='Limpar', padx=6, bd=3, fg='yellow', bg='black', font=('arial', 10, 'bold'), width=22, height=2, command=Reset).grid(row=0, column=3)

btnExit = Button(LeftmainFrame4, text='Sair', padx=6, bd=3, fg='yellow', bg='black', font=('arial', 10, 'bold'), width=22, height=2, command=Exit).grid(row=0, column=4)

btnImprimir = Button(LeftmainFrame4, text='Imprimir', padx=6, bd=3, fg='yellow', bg='black', font=('arial', 10, 'bold'), width=22, height=2, command=lambda: retrive_imput()).grid(row=0,column=5)

root.mainloop()