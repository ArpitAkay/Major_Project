from re import T
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()




class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login System")

        #TextVariablesForDataStorage
        self.v_username=StringVar()
        self.v_password=StringVar()

        self.v_forget_SecurityQ=StringVar()
        self.v_forget_securityA=StringVar()
        self.v_forgetnewpass=StringVar()





        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FRS\Major_Project\images\image1.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FRS\Major_Project\images\image8.png") 
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        image=Label(self.root,image=self.photoimg1)
        image.place(x=740,y=175,width=80,height=80)

        get_str=Label(frame,text="Get Started",font=("Book Antiqua",15,"bold"),bg="black",fg="white")
        get_str.place(x=115,y=90)

        username_label=Label(frame,text="Username",font=("Book Antiqua",15,"bold"),bg="black",fg="white")
        username_label.place(x=20,y=125)

        username_entry=ttk.Entry(frame,textvariable=self.v_username,width=30,font=("Book Antiqua",15,"bold"))
        username_entry.place(x=20,y=160)

        password_label=Label(frame,text="Password",font=("Book Antiqua",15,"bold"),bg="black",fg="white")
        password_label.place(x=20,y=195)

        password_entry=ttk.Entry(frame,textvariable=self.v_password,width=30,font=("Book Antiqua",15,"bold"))
        password_entry.place(x=20,y=230)

        login_btn=Button(frame,command=self.login_data,text="Login",width=5,font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        login_btn.place(x=110,y=275,width=120,height=35)

        register_btn=Button(frame,command=self.register_window,text="New User Register",width=5,font=("Book Antiqua",15,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        register_btn.place(x=20,y=320,width=200,height=35)

        forget_btn=Button(frame,command=self.forget_password,text="Forget Password",width=5,font=("Book Antiqua",15,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        forget_btn.place(x=10,y=350,width=200,height=35)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)





    #FunctionLoginButton
    def login_data(self):
        if self.v_username.get()=="" or self.v_password.get()=="":
            messagebox.showerror("Error","Please Enter Username and Password")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
           #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
            my_cursor=connection.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.v_username.get(),
                                                                                       self.v_password.get()
                                                                                       ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("Admin Access","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            connection.commit()
            connection.close()

    #ResetPasswordFunction
    def reset_password(self):
        if self.v_forget_SecurityQ.get()=="Select Security Question" or self.v_forget_securityA.get()=="" or self.v_forgetnewpass.get()=="":
            messagebox.showerror("Error","Please enter required fields",parent=self.root2)
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
           #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
            my_cursor=connection.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.v_username.get(),self.v_forget_SecurityQ.get(),self.v_forget_securityA.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct information",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.v_forgetnewpass.get(),self.v_username.get(),)
                my_cursor.execute(query,value)
                connection.commit()
                connection.close()
                messagebox.showinfo("Success","Your Password has been reset",parent=self.root2)
                self.root2.destroy()




    #ForgetFunction
    def forget_password(self):
        if self.v_username.get()=="":
            messagebox.showerror("Error","Please enter the Username to reset password")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
           #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
            my_cursor=connection.cursor()
            query=("select * from register where email=%s")
            value=(self.v_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid Username")
            else:
                connection.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                frame=Frame(self.root2,bg="white")
                frame.place(x=0,y=0,width=340,height=450)

                forget_label=Label(frame,text="Forget Password",font=("Book Antiqua",20,"bold"),bg="white",fg="blue")
                forget_label.place(x=0,y=0,width=340,height=40)

                security_label=Label(frame,text="Select Security Question",font=("Book Antiqua",15,"bold"),bg="white")
                security_label.place(x=30,y=60)

                security_combo=ttk.Combobox(frame,textvariable=self.v_forget_SecurityQ,font=("Book Antiqua",15,"bold"),width=23,state="read only")
                security_combo["values"]=("Select Security Question","What is the name of your first school?","In what city were you born?","What is the name of your favorite pet?")
                security_combo.current(0)
                security_combo.place(x=30,y=90)

                sans_label=Label(frame,text="Security Answer",font=("Book Antiqua",15,"bold"),bg="white")
                sans_label.place(x=30,y=130)

                sans_entry=ttk.Entry(frame,textvariable=self.v_forget_securityA,width=25,font=("Book Antiqua",15,"bold"))
                sans_entry.place(x=30,y=160)

                forgetnewpass_label=Label(frame,text="New Password",font=("Book Antiqua",15,"bold"),bg="white")
                forgetnewpass_label.place(x=30,y=200)

                forgetnewpass_entry=ttk.Entry(frame,textvariable=self.v_forgetnewpass,width=25,font=("Book Antiqua",15,"bold"))
                forgetnewpass_entry.place(x=30,y=230)

                reset_btn=Button(frame,command=self.reset_password,text="Reset",font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
                reset_btn.place(x=80,y=290,width=150,height=35)






class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Registeration Form")

        #TextVariablesForDataStorage
        self.v_fname=StringVar()
        self.v_lname=StringVar()
        self.v_contact=StringVar()
        self.v_email=StringVar()
        self.v_securityQ=StringVar()
        self.v_securityA=StringVar()
        self.v_newpass=StringVar()
        self.v_confpass=StringVar()


        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FRS\Major_Project\images\image1.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        frame=Frame(self.root,bg="white")
        frame.place(x=300,y=130,width=900,height=550)

        register_label=Label(frame,text="Register Here...",font=("Book Antiqua",18,"bold"),bg="white",fg="blue")
        register_label.place(x=60,y=10)

        fname_label=Label(frame,text="First Name",font=("Book Antiqua",15,"bold"),bg="white")
        fname_label.place(x=60,y=50)

        fname_entry=ttk.Entry(frame,textvariable=self.v_fname,width=25,font=("Book Antiqua",15,"bold"))
        fname_entry.place(x=60,y=80)

        lname_label=Label(frame,text="Last Name",font=("Book Antiqua",15,"bold"),bg="white")
        lname_label.place(x=500,y=50)

        lname_entry=ttk.Entry(frame,textvariable=self.v_lname,width=25,font=("Book Antiqua",15,"bold"))
        lname_entry.place(x=500,y=80)

        contact_label=Label(frame,text="Contact Number",font=("Book Antiqua",15,"bold"),bg="white")
        contact_label.place(x=60,y=130)

        contact_entry=ttk.Entry(frame,textvariable=self.v_contact,width=25,font=("Book Antiqua",15,"bold"))
        contact_entry.place(x=60,y=160)

        email_label=Label(frame,text="Email",font=("Book Antiqua",15,"bold"),bg="white")
        email_label.place(x=500,y=130)

        email_entry=ttk.Entry(frame,textvariable=self.v_email,width=25,font=("Book Antiqua",15,"bold"))
        email_entry.place(x=500,y=160)

        security_label=Label(frame,text="Select Security Question",font=("Book Antiqua",15,"bold"),bg="white")
        security_label.place(x=60,y=210)

        security_combo=ttk.Combobox(frame,textvariable=self.v_securityQ,font=("Book Antiqua",15,"bold"),width=23,state="read only")
        security_combo["values"]=("Select Security Question","What is the name of your first school?","In what city were you born?","What is the name of your favorite pet?")
        security_combo.current(0)
        security_combo.place(x=60,y=240)

        sans_label=Label(frame,text="Security Answer",font=("Book Antiqua",15,"bold"),bg="white")
        sans_label.place(x=500,y=210)

        sans_entry=ttk.Entry(frame,textvariable=self.v_securityA,width=25,font=("Book Antiqua",15,"bold"))
        sans_entry.place(x=500,y=240)

        newpass_label=Label(frame,text="New Password",font=("Book Antiqua",15,"bold"),bg="white")
        newpass_label.place(x=60,y=290)

        newpass_entry=ttk.Entry(frame,textvariable=self.v_newpass,width=25,font=("Book Antiqua",15,"bold"))
        newpass_entry.place(x=60,y=320)

        confpass_label=Label(frame,text="Confirm Password",font=("Book Antiqua",15,"bold"),bg="white")
        confpass_label.place(x=500,y=290)

        confpass_entry=ttk.Entry(frame,textvariable=self.v_confpass,width=25,font=("Book Antiqua",15,"bold"))
        confpass_entry.place(x=500,y=320)

        
        registernow_btn=Button(frame,command=self.register_data,text="Register",font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        registernow_btn.place(x=220,y=400,width=150,height=35)

        log_now_btn=Button(frame,command=self.return_login,text="Login",font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        log_now_btn.place(x=440,y=400,width=150,height=35)

    #FunctionForRegistration
    def register_data(self):
        if self.v_fname.get()=="" or self.v_lname.get()=="" or self.v_contact.get()=="" or self.v_email.get()=="" or self.v_securityQ.get()=="Select Security Question" or self.v_securityA.get()=="" or self.v_newpass.get()=="" or self.v_confpass.get()=="":
            messagebox.showerror("Error","Please enter all the required fields")
        elif self.v_newpass.get()!=self.v_confpass.get():
            messagebox.showerror("Error","New Password and Confirm Password should be same")
        else:
            connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
           #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
            my_cursor=connection.cursor()
            query=("select * from register where email=%s")
            value=(self.v_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Enter other Email")
            else:
                connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
               #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
                my_cursor=connection.cursor()
                my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.v_fname.get(),
                                                                                        self.v_lname.get(),
                                                                                        self.v_contact.get(),
                                                                                        self.v_email.get(),
                                                                                        self.v_securityQ.get(),
                                                                                        self.v_securityA.get(),
                                                                                        self.v_newpass.get()
                                                                                        ))


                connection.commit()
                connection.close()
                messagebox.showinfo("Success","Registration Successful")
                


    def return_login(self):
        self.root.destroy()




if __name__=="__main__":
    main()