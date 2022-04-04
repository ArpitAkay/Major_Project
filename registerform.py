from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

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

        newpass_label=Label(frame,text="Password",font=("Book Antiqua",15,"bold"),bg="white")
        newpass_label.place(x=60,y=290)

        newpass_entry=ttk.Entry(frame,textvariable=self.v_newpass,width=25,font=("Book Antiqua",15,"bold"))
        newpass_entry.place(x=60,y=320)

        confpass_label=Label(frame,text="Confirm Password",font=("Book Antiqua",15,"bold"),bg="white")
        confpass_label.place(x=500,y=290)

        confpass_entry=ttk.Entry(frame,textvariable=self.v_confpass,width=25,font=("Book Antiqua",15,"bold"))
        confpass_entry.place(x=500,y=320)

        
        registernow_btn=Button(frame,command=self.register_data,text="Register",font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        registernow_btn.place(x=220,y=400,width=150,height=35)

        log_now_btn=Button(frame,text="Login",font=("Book Antiqua",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="white",activeforeground="white",activebackground="blue")
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
                


if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()