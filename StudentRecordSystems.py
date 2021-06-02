from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox
import tempfile
import os

class Student:

    def __init__(self, root):
        self.root=root
        self.root.title("Student Record System")
        self.root.geometry("1350x75+0+0")

        iDate = StringVar()
        iDate.set(time.strftime("%d/%m/%Y"))


        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()
        Date=StringVar()
        ULNumber=StringVar()
        RegNumber=StringVar()
        NextofNick=StringVar()
        StudentID=StringVar()
        StudentLoan=StringVar()
        Degree=StringVar()

        StudentLoan=StringVar()
        StudentLoan.set("0")
        InternationalFees=StringVar()
        InternationalFees.set("0")
        AccomodationFees=StringVar()
        AccomodationFees.set("0")
        #=============================================Functions==================================================================

        def iExit():
            iExit =tkinter.messagebox.askyesno("Student Record System", "Are you sure that you want to Exit?")
            if iExit > 0:
                root.destroy()
                return

        def iPrint():
            q =self.txtReceipt.get("1.0", "end-1c")
            filename = tempfile.mktemp(".txt")
            open (filename, "w"). write(q)
            os.startfile(filename, "print")

        def iReset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            StudentID.set("")
           

            ULNumber.set("")
            RegNumber.set("")
            NextofNick.set("")
            StudentLoan.set("")

            var1.set("")
            var2.set("")
            var3.set("0")
            var4.set(0)
            var5.set(0)
            var6.set(0)
            StudentLoan.set("0")
            InternationalFees.set("0")
            AccomodationFees.set("0")
            self.txtStudentLoan.configure(state= DISABLED)
            self.txtAccomodation.configure(state= DISABLED)
            self.txtInternational.configure(state= DISABLED)

            self.cboProof_of_ID.current(0)
            self.cboType_of_Degree.current(0)
            self.cboMethod_of_Payment.current(0)
            Ref_No()

        def Reset():
            jReset =tkinter.messagebox.askyesno("Student Record System", "Are you sure that you want to Reset?")
            if jReset > 0:
                iReset()
            elif jReset <= 0:
                iReset()
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,"Student ID\t\t Firstname\t\t Lastname\t\t Address\t\t Post Code\t\t Student Loan \t\t \
        \tTelephone\t\t Date\t\t Degree\t\t ULN Number\t\t Next of Nick\t\n")
               
        def Ref_No():
                Member_Ref=StringVar()
                x = random.randint(10908, 500876)
                randomRef = str(x)
                Member_Ref.set(randomRef)
                StudentID.set(randomRef)

        def Receipt():

            Ref_No()
            self.txtReceipt.insert(END,StudentID.get()+"\t\t" + Firstname.get()+ Surname.get()+"\t\t"+ Address.get()+"\t\t"+ PostCode.get()+"\t\t" + StudentLoan.get()+" \t\t\t"
        + Telephone.get()+"\t\t"+ iDate.get()+"\t\t"+ var2.get()+"\t\t"+ ULNumber.get()+"\t\t"+ NextofNick.get() + "\n")
           
           
        def Student_Loan():
            global paid1
            if (var4.get() == 1):
               self.txtStudentLoan.configure(state = NORMAL)
               Item1=float(9450)

               StudentLoan.set("$" + str(Item1))
               paid1 = StudentLoan.get()
               StudentLoan.set("$" + str(Item1))
            elif (var4.get() == 0):
                self.txtStudentLoan.configure(state = NORMAL)
                StudentLoan.set("0")

       
               
        #========================================================================================================================
       
        Mainframe=Frame(self.root)
        Mainframe.grid()

        Tops = Frame(Mainframe, bd=10, relief=RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle= Label(Tops, width=30, font=('arial' ,39,'bold'), text= "Student Record System", justify=CENTER)
        self.lblTitle.grid(padx=150)

        MembersName_F = LabelFrame(Mainframe, bd=10,width=1300,height=400,
                    font=('arial',12, 'bold'),text = 'Student Name',relief=RIDGE)
        MembersName_F.pack(padx=38,side=TOP)

        Receipt_ButtonFrame= LabelFrame(Mainframe, bd=10,width=1300,height=200,font=('arial',12,'bold'),text = 'Details',relief=RIDGE)
        Receipt_ButtonFrame.pack(padx=38,side=TOP)

        #================================================Widget=========================================================
        self.lblStudentID= Label(MembersName_F, font=('arial' ,16,'bold'), text= "Student ID", bd=7)
        self.lblStudentID.grid(row=0,column=0, sticky=W)
        self.txtStudentID= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable= StudentID, bd=7,
                                 insertwidth=2, state=DISABLED)
        self.txtStudentID.grid(row=0,column=1)

        self.lblFirstname= Label(MembersName_F, font=('arial' ,16,'bold'), text= "First Name", bd=7)
        self.lblFirstname.grid(row=1,column=0, sticky=W)
        self.txtFirstname= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=Firstname, bd=7,
                                 insertwidth=2)
        self.txtFirstname.grid(row=1,column=1)

        self.lblSurname= Label(MembersName_F, font=('arial' ,16,'bold'), text= "Last Name", bd=7)
        self.lblSurname.grid(row=2,column=0, sticky=W)
        self.txtSurname= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=Surname, bd=7,
                                 insertwidth=2)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress= Label(MembersName_F, font=('arial' ,16,'bold'), text= "Address", bd=7)
        self.lblAddress.grid(row=3,column=0, sticky=W)
        self.txtAddress= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=Address, bd=7,
                                 insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPostCode= Label(MembersName_F, font=('arial' ,16,'bold'), text= "Post Code", bd=7)
        self.lblPostCode.grid(row=4,column=0, sticky=W)
        self.txtPostCode= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=PostCode, bd=7,
                                 insertwidth=2)
        self.txtPostCode.grid(row=4,column=1)

        self.chkStudentLoan = Checkbutton(MembersName_F, text= "Student Loan", variable=var4, onvalue =1,
        offvalue = 0, font=('arial' ,16,'bold'), command=Student_Loan).grid(row =5, column=0,sticky=W)
        self.txtStudentLoan= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=StudentLoan, bd=7,
                                 insertwidth=2,state= DISABLED, justify=RIGHT)
        self.txtStudentLoan.grid(row=5,column=1)
        #================================================Widget=========================================================
        self.lblTelephone = Label(MembersName_F, font=('arial' ,16,'bold'), text= "Telephone", bd=7)
        self.lblTelephone.grid(row=0,column=2, sticky=W)
        self.txtTelephone= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=Telephone, bd=7,
                                 insertwidth=2)
        self.txtTelephone.grid(row=0,column=3)

        self.lblDate= Label(MembersName_F, font=('arial', 16,'bold'), text= "Date", bd=7)
        self.lblDate.grid(row=1,column=2, sticky=W)
        self.txtDate= Entry(MembersName_F, font=('arial', 13,'bold'), textvariable=iDate, bd=7,
                                 insertwidth=2)
        self.txtDate.grid(row=1,column=3)

        self.lblProof_of_ID = Label(MembersName_F, font=('arial' ,16,'bold'), text= "Proof of ID ", bd=7)
        self.lblProof_of_ID .grid(row=2,column=2, sticky=W)

        self.cboProof_of_ID =ttk.Combobox(MembersName_F,textvariable = var1, state='readonly',
                                          font=('arial',13,'bold'),width=19)
        self.cboProof_of_ID['value']=('','Pilot License' , 'Driving License','Passport','Student ID')
        self.cboProof_of_ID.current(0)
        self.cboProof_of_ID.grid(row=2,column=3)

        self.lblType_of_Degree = Label(MembersName_F,font=('arial' ,16,'bold'), text= "Type of Degree", bd=7)
        self.lblType_of_Degree.grid(row=3,column=2, sticky=W)

        self.cboType_of_Degree =ttk.Combobox(MembersName_F,textvariable = var2, state='readonly',
                                             font=('arial',13,'bold'),width=19)
        self.cboType_of_Degree['value']=('','Undergaduate' , 'Postgraduate','Doctoral Degree')
        self.cboType_of_Degree.current(0)
        self.cboType_of_Degree.grid(row=3,column=3)

        self.lblMethod_of_Payment = Label(MembersName_F, font=('arial' ,16,'bold'), text= "Method of Payment", bd=7)
        self.lblMethod_of_Payment.grid(row=4,column=2, sticky=W)

        self.cboMethod_of_Payment =ttk.Combobox(MembersName_F, textvariable = var3, state='readonly',
                                               font=('arial',13, 'bold'),width=19)
        self.cboMethod_of_Payment['value']=('','Visa Card','Master Card','Debit Card','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=4,column=3)

        self.chkAccomodation = Checkbutton(MembersName_F,text= "Accomodation", variable=var5, onvalue = 1,
        offvalue = 0,font=('arial' ,16,'bold')).grid(row=5,column=2,sticky=W)
        self.txtAccomodation= Entry(MembersName_F,font=('arial' ,13,'bold'), textvariable=AccomodationFees, bd=7,
                                 insertwidth=2,state= DISABLED, justify=RIGHT)
        self.txtAccomodation.grid(row=5,column=3)
        #=============================================Widget====================================================================
        self.lblRegNumber= Label(MembersName_F, font=('arial' ,16,'bold'), text= "Reg Number", bd=7)
        self.lblRegNumber.grid(row=0,column=4, sticky=W)
        self.lblRegNumber= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=RegNumber, bd=7,
                                 insertwidth=1)
        self.lblRegNumber.grid(row=0,column=5)

        self.lblULNUmber= Label(MembersName_F,font=('arial' ,16,'bold'), text= "ULN Number", bd=7)
        self.lblULNUmber.grid(row=1,column=4, sticky=W)
        self.txtULNUmber= Entry(MembersName_F, font=('arial' ,13,'bold'), textvariable=ULNumber, bd=7,
                                 insertwidth=1)
        self.txtULNUmber.grid(row=1,column=5)

        self.lblNextofNick = Label(MembersName_F,font=('arial' ,16,'bold'), text= "Next of Nick", bd=7)
        self.lblNextofNick.grid(row=2,column=4, sticky=W)
        self.txtNextofNick =Entry(MembersName_F, font=('arial',13,'bold'), textvariable=NextofNick, bd=7,
                                  insertwidth=1)
        self.txtNextofNick.grid(row=2,column=5)
       
       
        self.lblAddress = Label(MembersName_F,font=('arial' ,16,'bold'), text= "Address", bd=7)
        self.lblAddress.grid(row=3,column=4, sticky=W)
        self.txtAddress = Entry(MembersName_F,font=('arial',13,'bold'), textvariable=Address, bd=7,
                                          insertwidth=1)
        self.txtAddress.grid(row=3,column=5)

   
        self.lblPostCode = Label(MembersName_F,font=('arial' ,16,'bold'), text= "PostCode", bd=7)
        self.lblPostCode.grid(row=4,column=4, sticky=W)
        self.txtPostCode =Entry(MembersName_F, font=('arial',13,'bold'), textvariable=PostCode, bd=7,
                             insertwidth=1)
        self.txtPostCode .grid(row=4,column=5)
       
        self.chkMembership = Checkbutton(MembersName_F, text= "International Student Fees", variable=var6, onvalue = 1,
        offvalue = 0,font=('arial' ,16,'bold')).grid(row=5,column=4,sticky=W)
        self.txtInternational= Entry(MembersName_F,font=('arial' ,13,'bold'), textvariable=InternationalFees, bd=7,
                                 insertwidth=1,state= DISABLED, justify=RIGHT)
        self.txtInternational.grid(row=5,column=5)
        #=========================================================================================================================
        self.txtReceipt = Text(Receipt_ButtonFrame, width=181, height=10,font=('arial',10,'bold'))
        self.txtReceipt.grid(row =0, column=0, columnspan=4)

        self.txtReceipt.insert(END,"Student ID\t\t Firstname\t\t Lastname\t\t Address\t\t Post Code\t\t Student Loan \t\t \
        \tTelephone\t\t Date\t\t Degree\t\t ULN Number\t\t Next of Nick\t\n")
        #===============================================Button==========================================================================
        self.btnReceipt=Button(Receipt_ButtonFrame, bd=7, font=('arial' ,16,'bold'), width=13,
                               text="Receipt",command=Receipt).grid(row =1, column=0, pady=12)

        self.btnReset=Button(Receipt_ButtonFrame, bd=7, font=('arial' ,16,'bold'), width=13,
                               text="Reset", command=Reset).grid(row =1, column=1, pady=12)

        self.btnPrint=Button(Receipt_ButtonFrame, bd=7, font=('arial' ,16,'bold'), width=13,
                               text="Print", command=iPrint).grid(row =1, column=2, pady=12)

        self.btnExit=Button(Receipt_ButtonFrame, bd=7, font=('arial' ,16,'bold'), width=13,
                               text="Exit",command=iExit).grid(row =1, column=3, pady=12)
       
if __name__=='__main__':
    root = Tk()
    application = Student (root)
    root.mainloop()

       

        
