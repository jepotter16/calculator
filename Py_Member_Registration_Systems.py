from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox


class Registration:

    def __init__(self, root):
        self.root = root
        self.root.title("Club Member Registration Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Lastname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()
        

        Membership =StringVar()
        Membership.set("0")

        #==============================================Funtion Declared=====================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Club Member Registrations Systems", "Confirmation if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def Reset():
            Firstname.set("")
            Lastname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set(0)
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProof_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Club Member Registrations Systems", "Confirm if you want to add a new\
record")
            if iResetRecord> 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return
        def Ref_No():
            
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t" + Ref.get()+ "\t\t" + Firstname.get() + "\t\t" + Lastname.get()
                                   + "\t\t" + Address.get() + "\t\t" +DateofOrder.get() + "\t\t" + Telephone.get()
                                   +"\t\t"+ Membership.get()+ "\n")

        def Membership_Fees():
       
            if (var4.get() == 1):
                self.txtMembership.configure(state = NORMAL)
                Item1 = float(50)
                Membership.set("$" + str(Item1))
                
            elif (var4.get() == 0):
                self.txtMembership.configure(state = DISABLED)
                Membership.set("0")
                
            
        #==============================================Frame================================================================

        Mainframe=Frame(self.root)
        Mainframe.grid()

        TitleFrame=Frame(Mainframe, bd=20,width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',59,'bold'),text="Member Registrations Systems",padx=2)
        self.lblTitle.grid()
        #=============================================Lower Frames=============================================================================
        MemberDetailsFrame = LabelFrame(Mainframe,width=1350,height=500, bd=20,
                                            pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10,width=350,height=400,
                        font=('arial',12,'bold'),text = 'Customer Name' ,relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame= LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,
                    relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
        #===========================================================================================================================================
        self.lblReferenceNo=Label(MembersName_F ,font=('arial',14,'bold'),text="Reference No",bd=7)
        self.lblReferenceNo.grid(row=0 ,column=0, sticky=W)
        self.txtReferenceNo=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7, textvariable=Ref,
                                  state =DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0 ,column=1)

        self.lblFirstname=Label(MembersName_F ,font=('arial',14,'bold'),text="Firstname",bd=7)
        self.lblFirstname.grid(row=1 ,column=0, sticky=W)
        self.txtFirstname=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7, insertwidth=2, textvariable=Firstname)
        self.txtFirstname.grid(row=1 ,column=1)

        self.lblLastname=Label(MembersName_F ,font=('arial',14,'bold'),text="Lastname",bd=7)
        self.lblLastname.grid(row=2 ,column=0, sticky=W)
        self.txtLastname=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7, textvariable=Lastname,
                               insertwidth= 2)
        self.txtLastname.grid(row=2 ,column=1)

        self.lblAddress=Label(MembersName_F ,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=3 ,column=0, sticky=W)
        self.txtAddress=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7, textvariable=Address,
                              insertwidth=2)
        self.txtAddress.grid(row=3 ,column=1)

        self.lblPostcode=Label(MembersName_F ,font=('arial',14,'bold'),text="Postcode",bd=7)
        self.lblPostcode.grid(row=4 ,column=0, sticky=W)
        self.txtPostcode=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7,textvariable=Postcode,
                               insertwidth=2)
        self.txtPostcode.grid(row=4 ,column=1)

        self.lblTelephone=Label(MembersName_F ,font=('arial',14,'bold'),text="Telephone",bd=7)
        self.lblTelephone.grid(row=5 ,column=0, sticky=W)
        self.txtTelephone=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7, textvariable=Telephone,
                                insertwidth=2)
        self.txtTelephone.grid(row=5 ,column=1)

        self.lblDate=Label(MembersName_F ,font=('arial',14,'bold'),text="Date",bd=7)
        self.lblDate.grid(row=6 ,column=0, sticky=W)
        self.txtDate=Entry(MembersName_F ,font=('arial',14,'bold'),bd=7,textvariable= DateofOrder,
                           insertwidth=2)
        self.txtDate.grid(row=6 ,column=1)
        #====================================================Member Information=======================================================================================
        self.lblProof_of_ID = Label(MembersName_F,font=('arial',14,'bold'),text="Proof_of_ID",bd=7)
        self.lblProof_of_ID.grid(row=7 ,column=0, sticky=W)

        self.cboProof_of_ID =ttk.Combobox(MembersName_F, textvariable = var1, state='readonly',
                                         font=('arial',14,'bold'),width=19)
        self.cboProof_of_ID['value']=('','Pilot License','Driving Licence','Passport','Student ID')
        self.cboProof_of_ID.current(0)
        self.cboProof_of_ID.grid(row=7,column=1)

        self.lblType_of_Member = Label(MembersName_F,font=('arial',14,'bold'),text="Type of Member",bd=7)
        self.lblType_of_Member.grid(row=8 ,column=0, sticky=W)

        self.cboType_of_Member=ttk.Combobox(MembersName_F, textvariable= var2, state='readonly',
                                         font=('arial',14,'bold'),width=19)
        self.cboType_of_Member['value']=('','Full Member','Annual membership','Pay as You Go','Honoary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)

        self.lblMethod_of_Payment = Label(MembersName_F ,font=('arial',14,'bold'),text="Method of Payment",bd=7)
        self.lblMethod_of_Payment.grid(row=9 ,column=0, sticky=W)

        self.cboMethod_of_Payment=ttk.Combobox(MembersName_F, textvariable= var3, state='readonly',
                                         font=('arial',14,'bold'),width=19)
        self.cboMethod_of_Payment['value']=('','Visa Card ','Master Card ','Debit Card ','Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1)

        #===============================================Check Button======================================================
        self.chkMembership = Checkbutton(MembersName_F, text="Membership Fees", variable=var4, onvalue =1,
        offvalue = 0,font=('arial',16, 'bold'),command = Membership_Fees).grid(row=10,column=0,sticky=W)
        
        self.txtMembership = Entry(MembersName_F,font=('arial',14, 'bold'), textvariable=Membership, bd=7,
                                  insertwidth=2,state= DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)
        #===============================================Receipt====================================================================
        self.lblLabel = Label(Receipt_ButtonFrame ,font=('arial',10,'bold'),pady=10,
        text="Member Ref\t Firstname\t Lastname\t Address\t\t Date Reg.\t Telephone\t Member Paid ",bd=7)
        self.lblLabel.grid(row=0 ,column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame,width=112, height =22, font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1 ,column=0, columnspan=4)

        #===============================================Buttons====================================================================
        self.btnReceipt=Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial',16,'bold'),width=13,
                               text="Receipt", command= Receipt).grid(row=2,column=0)
        self.btnReset=Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial',16,'bold'),width=13,
                               text="Reset", command= iResetRecord).grid(row=2,column=1)
        self.btnExit=Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial',16,'bold'),width=13,
                               text="Exit" , command =iExit).grid(row=2,column=2)
        
         #===================================================================================================================


if __name__=='__main__':
    root = Tk()
    application = Registration (root)
    root.mainloop()
    
