import time
import datetime
from tkinter import*
import tkinter.messagebox
import tempfile
import os


root = Tk()
root.title("AllSTAR PAYROLL")
root.geometry('1350x650+0+0')

Tops = Frame(root, width=1350, height=50,bg="black", bd = 8, relief="raise")
Tops.pack(side = TOP)

f1 = Frame(root, width=300, height= 600, bg="black", bd = 8, relief="raise")
f1.pack(side = LEFT)
f2 = Frame(root, width=300, height= 700, bd = 8, relief="raise")
f2.pack(side = RIGHT)

f1a = Frame(f1, width=600, height= 200,  bd = 20, relief="raise")
f1a.pack(side = TOP)
f1b = Frame(f1, width=600, height= 600,  bg="blue", bd = 20, relief="raise")
f1b.pack(side = TOP)

lblinfo=Label(Tops, font=('Times New Roman', 50, 'bold'), text=" All-STAR PAYROLL", bd=10)
lblinfo.grid(row=0,column=0)



#==================================================================================================
def iPrint():
    q = txtPaySlip.get("1.0","end-1c")
    filename = tempfile.mktemp(".txt")
    open (filename, "w").write(q)
    os.startfile(filename, "print")




def iExit():
    iExit =tkinter.messagebox.askyesno("ALL STAR PAYROLL SYSTEM", "Are you sure that you want to Exit?")
    if iExit > 0:
        root.destroy()
        return

def Reset():
    Name.set("")
    Address.set("")
    Employer .set("")
    HoursWorked .set("")
    wageshour .set("")
    Payable .set("")
    Taxable .set("")
    NetPayable .set("")
    GrossPayable .set("")
    OvertimeHours .set("")
    Employer .set("")
    NINumber .set("")
    txtPaySlip.delete("1.0",END)

def EnterInfo():
    txtPaySlip.insert(END, "\t\tPay Slip\n\n")
    txtPaySlip.insert(END, 'Name: \t\t' + Name.get() + "\n\n")
    txtPaySlip.insert(END, 'Address: \t\t' + Address.get() + "\n\n")
    txtPaySlip.insert(END, 'Employer: \t\t' + Employer.get() + "\n\n")
    txtPaySlip.insert(END, 'NINumber: \t\t' + NINumber.get() + "\n\n")
    txtPaySlip.insert(END, 'Hours Worked: \t\t' + HoursWorked.get() + "\n\n")
    txtPaySlip.insert(END, 'Net Payable: \t\t' + NetPayable.get() + "\n\n")
    txtPaySlip.insert(END, 'Wages Per hour: \t\t' + wageshour.get() + "\n\n")
    txtPaySlip.insert(END, 'Tax Paid: \t\t' + Taxable.get() + "\n\n")
    txtPaySlip.insert(END, 'Payable: \t\t' + Payable.get() + "\n\n")


def WeeklyWages():
    HoursWorkedPerWeek=float(HoursWorked.get())
    WagesPerHours=float(wageshour.get())

    paydue = WagesPerHours * HoursWorkedPerWeek
    PaymentDue = "$", str('%.2f' %(paydue))
    Payable.set(PaymentDue)

    tax = paydue*0.2
    Taxables ="$" ,str ('%.2f' %(tax))
    Taxable.set(Taxables)

    netpay = paydue-tax
    NetPays="$", str('%.2f' %(netpay))
    NetPayable.set(NetPays)

    if HoursWorkedPerWeek > 40:
       OvertimeHours = (HoursWorkedPerWeek - 40) + WagesPerHours * 1.5
       OvertimeHours = "$", str ('%.2f' %(OvertimeHours))
       OvertimeHours.set(OvertimeHours)

    elif HoursWorkedPerWeek <= 40:
       OvertimeHours=(HoursWorkedPerWeek - 40)+ WagesPerHours * 1.5
       OvertimeHours = "$", str ('%.2f' %(OvertimeHours))
       OvertimeHours.set(OvertimeHours)
    return
#====================================Variables==================================================
Name=StringVar()
Address=StringVar()
Employer =StringVar()
HoursWorked =StringVar()
wageshour =StringVar()
Payable =StringVar()
Taxable =StringVar()
NetPayable =StringVar()
GrossPayable =StringVar()
OvertimeHours =StringVar()
Employer=StringVar()
NINumber =StringVar()
TimeofOrder=StringVar()
DateofOrder=StringVar()

DateofOrder.set(time.strftime("%m/%d/%Y"))
#=========================================Label Widget========================================================================
lblName=Label(f1a, text="Name", font=('Times New Roman',16,'bold'), bd=20).grid(row=0,column=0)
lblAddress=Label(f1a, text="Address", font=('Times New Roman',16,'bold'),bd=20).grid(row=0,column=2)
lblEmployer=Label(f1a, text="Employer", font=('Times New Roman',16,'bold'),bd=20).grid(row=1,column=0)
lblNInumer=Label(f1a, text="NINumber", font=('Times New Roman',16,'bold'),bd=20).grid(row=1,column=2)
lblHoursWorked=Label(f1a, text="HOURS WORKED:", font=('Times New Roman',16,'bold'),bd=20).grid(row=2,column=0)
lblHourlyRate=Label(f1a, text="HourlyRate", font=('Times New Roman',16,'bold'),fg="blue",bd=20).grid(row=2,column=2)
lblTax=Label(f1a, text="Tax", font=('Times New Roman',16,'bold'),fg="red",bd=20, anchor='w').grid(row=3,column=0)
lblOvertime=Label(f1a, text="Overtime", font=('Times New Roman',16,'bold'),fg="blue",bd=20).grid(row=3,column=2)
lblGrossPay=Label(f1a, text="Gross Pay", font=('Times New Roman',16,'bold'),fg="red",bd=20).grid(row=4,column=0)
lblNetPay=Label(f1a, text="Net Pay", font=('Times New Roman',16,'bold'),fg="red",bd=20).grid(row=4,column=2)
#=======================================Etry Widget  =======================================================================
etxtName= Entry(f1a, textvariable=Name, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtName.grid(row=0,column=1)
etxtAddress= Entry(f1a, textvariable=Address, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmployer= Entry(f1a, textvariable=Employer, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtEmployer.grid(row=1,column=1)
etxtHoursWorked= Entry(f1a, textvariable=HoursWorked, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtwageshour= Entry(f1a, textvariable=wageshour, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtwageshour.grid(row=2,column=3)
etxtninoW= Entry(f1a, textvariable=NINumber, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtninoW.grid(row=1,column=3)
etxtGrossPay= Entry(f1a, textvariable=GrossPayable, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtGrossPay.grid(row=4,column=1)
etxtNetPay= Entry(f1a, textvariable=NetPayable, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtNetPay.grid(row=4,column=3)
etxtTax= Entry(f1a, textvariable=Taxable, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtTax.grid(row=3,column=1)
etxtOvertimeHours= Entry(f1a, textvariable=OvertimeHours, font=('arial',16,'bold'),bd=16, width=22, justify='left')
etxtOvertimeHours.grid(row=3,column=3)
#====================================Text Widget===============================================================
lblPaySlip=Label(f2, font=('arial',20,'bold'),textvariable=DateofOrder).grid(row=0,column=0)
txtPaySlip= Text(f2, height = 22, width =35, bd=16, font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)
#======================================Buttons================================================================================
btnSalary=Button(f1b, text='Weekly Salary', padx=16, pady=16, bd=8, fg="black",
                 font=('arial',16,'bold'),width=10,height=1, command=WeeklyWages).grid(row=0,column=0)

btnReset=Button(f1b, text='Reset',padx=16, pady=16, bd=8, fg="black",
                 font=('arial',16,'bold'),width=10,height=1, command=Reset).grid(row=0,column=1)

btnPaySlip=Button(f1b, text='View Payslip', padx=16, pady=16, bd=8, fg="black",
                 font=('arial',16,'bold'),width=10,height=1,command=EnterInfo).grid(row=0,column=2)

btnExit=Button(f1b, text='Exit', padx=16, pady=16, bd=8, fg="black",
                 font=('arial',16,'bold'),width=10,height=1, command=iExit) .grid(row=0,column=3)

btnPrint=Button(f1b, text='Print',padx=16, pady=16, bd=8, fg="black",
                 font=('arial',16,'bold'),width=10,height=1,command=iPrint).grid(row=0,column=4)

btnPrint=Button(Tops, text='Update',padx=10, pady=10, bd=8, fg="black",bg="white",
                 font=('arial',12,'bold'),width=8,height=1,).grid(row=0,column=1)
btnPrint=Button(Tops, text='Add New',padx=10, pady=10, bd=8, fg="black",bg="white",
                 font=('arial',12,'bold'),width=8,height=1,).grid(row=0,column=2)
btnPrint=Button(Tops, text='Search',padx=10, pady=10, bd=8, fg="black",bg="white",
                 font=('arial',12,'bold'),width=8,height=1,).grid(row=0,column=3)





root.mainloop()
