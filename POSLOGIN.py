from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Portièr Systems")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='black')
        self.frame = Frame(self.master, bg='black')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Portière Systems', font=('Impact',80,'bold'), bg='black',
                              fg='White')
        self.lblTitle.grid(row =0, column = 0, columnspan=2, pady =40)


        

        #==========================Vatiables=========================================================
        iExit = StringVar()
        #=========================================================================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame,  width = 1350,height=600
                                ,font=('arial',50,'bold'), relief='ridge',bg='silver',bd=20)
        self.LoginFrame1.grid(row=1,column =0)

        self.LoginFrame2 = LabelFrame(self.frame,  width = 1000,height=600
                                ,font=('arial',50,'bold'), relief='ridge',bg='silver',bd=20)
        self.LoginFrame2.grid(row=2,column =0)

        #=====================================================================Labels and Entry =========================================================================================
        self.lblUsername=Label(self.LoginFrame1,text = 'Username', font=('arial',20,'bold'))
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable= self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.LoginFrame1,text = 'Password', font=('arial',20,'bold'))
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'), show='*', textvariable= self.Password)
        self.txtPassword.grid(row=1,column=1)

        #=======================================================================Buttons==================================================================================

        
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17, font='bold', command =self.Login_System)
        self.btnLogin.grid(row=3,column = 0)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 17,font='bold',command =self.Reset)
        self.btnReset.grid(row=3,column = 1)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 17,font='bold',command =self.iExit)
        self.btnExit.grid(row=3,column = 2)

        self.btnForgotPassword = Button(self.LoginFrame2, text = 'ForgotPassword', width = 17,font='bold')
        self.btnForgotPassword.grid(row=4,column = 0)

        self.btnHelp = Button(self.LoginFrame2, text = 'Help', width = 17,font='bold')
        self.btnHelp.grid(row=4,column = 1)


        self.btnRegister = Button(self.LoginFrame2, text = 'Register', width = 17,font='bold')
        self.btnRegister.grid(row=4,column = 2)
        #=====================================Buttons=================================================================================
    def Login_System(self):
        u =(self.Username.get())
        p =(self.Password.get())
        if (u ==str(123456789) and p ==str(987654321)):
             self.newWindow = Toplevel(self.master)
             self.app = Window2(self.newWindow)
             
        else:
            tkinter.messagebox.askyesno("Login Systems", "Invalid Credentials, Please enter correct credentials")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.Focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.Focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Point Of Sale", "Are you sure that you want to exit")
        if iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
       
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:

    def __init__(self,master):
        self.master = master
        self.master.title("Mainpage")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg ='black')
        self.frame = Frame(self.master, bg = 'black')
        self.frame.pack()
#=============================================================================================================================================
        MainFrame = Frame(self.root, bg='black')
        MainFrame.pack(padx=10, pady=10)
        
        DataFrame = Frame(MainFrame, bg='black', bd=5, width=800, height =300, padx=4, pady=4, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFTCOVER = LabelFrame(DataFrame, bg='black', bd=5, width=800, height =300, padx=4, pady=4)
        DataFrameLEFTCOVER .pack(side=BOTTOM)

        ChangeButtonFrame = Frame(DataFrameLEFTCOVER, bd=5, width=800, height =860, pady=4, relief=RIDGE)
        ChangeButtonFrame.pack(side=BOTTOM,padx=10)
        
        

        


if __name__=='__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()

