from ast import Try
from multiprocessing import connection
from sqlite3 import connect
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from numpy import delete
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #VariablesForDataStorage
        self.v_dep=StringVar()
        self.v_course=StringVar()
        self.v_year=StringVar()
        self.v_sem=StringVar()
        self.v_id=StringVar()
        self.v_name=StringVar()
        self.v_roll=StringVar()
        self.v_gender=StringVar()
        self.v_sec=StringVar()
        self.v_dob=StringVar()
        self.v_email=StringVar()
        self.v_phone=StringVar()
        self.v_address=StringVar()
        self.v_cc=StringVar()
        

        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image2.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("Book Antiqua",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bgimage,bd=2,bg="white")
        main_frame.place(x=15,y=60,width=1495,height=715)

        #LeftLabelFrame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Book Antiqua",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=685)

        #CurrentCourse
        currentcourseframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Book Antiqua",12,"bold"))
        currentcourseframe.place(x=15,y=35,width=745,height=220)

        #DepartmentLabel
        dept_label=Label(currentcourseframe,text="Department",font=("Book Antiqua",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(currentcourseframe,textvariable=self.v_dep,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        dept_combo["values"]=("Select Deparatment","Engineering","Management","Arts and Science","Business Studies","Fine Arts and Communication")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #CourseLabel
        course_label=Label(currentcourseframe,text="Course",font=("Book Antiqua",12,"bold"),bg="white")
        course_label.grid(row=1,column=0,padx=10,sticky=W)

        course_combo=ttk.Combobox(currentcourseframe,textvariable=self.v_course,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        course_combo["values"]=("Select Course","Computer Science","Information Technology","Electronics and Communication","Petroleum","Humanities and Social Sciences","Hotel Management and Hospitality","Biotechnology","Electrical","Management","Commerce","Nursing","Civil","Mechanical","Life Science","Paramedical Science","Computer Application")
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #YearLabel
        year_label=Label(currentcourseframe,text="Year",font=("Book Antiqua",12,"bold"),bg="white")
        year_label.grid(row=2,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(currentcourseframe,textvariable=self.v_year,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        year_combo["values"]=("Select Year","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #SemesterLabel
        sem_label=Label(currentcourseframe,text="Semester",font=("Book Antiqua",12,"bold"),bg="white")
        sem_label.grid(row=3,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(currentcourseframe,textvariable=self.v_sem,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        
        #StudentInformation
        studentinfoframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("Book Antiqua",12,"bold"))
        studentinfoframe.place(x=15,y=260,width=745,height=420)

        #StudentID
        sID_label=Label(studentinfoframe,text="Student ID",font=("Book Antiqua",12,"bold"),bg="white")
        sID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        sID_entry=ttk.Entry(studentinfoframe,textvariable=self.v_id,width=20,font=("Book Antiqua",12,"bold"))
        sID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #StudentName
        sname_label=Label(studentinfoframe,text="Student Name",font=("Book Antiqua",12,"bold"),bg="white")
        sname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        sname_entry=ttk.Entry(studentinfoframe,textvariable=self.v_name,width=20,font=("Book Antiqua",12,"bold"))
        sname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

        #Section
        section_label=Label(studentinfoframe,text="Section",font=("Book Antiqua",12,"bold"),bg="white")
        section_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #section_entry=ttk.Entry(studentinfoframe,textvariable=self.v_sec,width=20,font=("Book Antiqua",12,"bold"))
        #section_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(studentinfoframe,textvariable=self.v_sec,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        section_combo["values"]=("Select Section","A","B","C","D","E","F","G","H","I")
        section_combo.current(0)
        section_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #RollNumber
        rno_label=Label(studentinfoframe,text="Roll Number",font=("Book Antiqua",12,"bold"),bg="white")
        rno_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        rno_entry=ttk.Entry(studentinfoframe,textvariable=self.v_roll,width=20,font=("Book Antiqua",12,"bold"))
        rno_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Gender
        gender_label=Label(studentinfoframe,text="Gender",font=("Book Antiqua",12,"bold"),bg="white")
        gender_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(studentinfoframe,textvariable=self.v_gender,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","I prefer not to say")
        gender_combo.current(0)
        gender_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #DateOfBirth
        dob_label=Label(studentinfoframe,text="Date Of Birth",font=("Book Antiqua",12,"bold"),bg="white")
        dob_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        #from tkcalendar import Calendar
        #self.root.geometry("250x250")
        
        #cal=Calendar(self.root,electmode='day',year=2001,month = 1,day=24)
        
        #cal.pack(pady = 20)
        
        #def grad_date():
         #   date.config(text="Selected Date is: " + cal.get_date())
        
       
        #Button(self.root,text = "Get Date",command=grad_date).pack(pady=20)
        #date=Label(self.root,text="")
        #date.pack(pady=20)
        
        
        
        
        
        
        dob_entry=ttk.Entry(studentinfoframe,textvariable=self.v_dob,width=20,font=("Book Antiqua",12,"bold"))
        dob_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)       
        
        #Email
        email_label=Label(studentinfoframe,text="Email",font=("Book Antiqua",12,"bold"),bg="white")
        email_label.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(studentinfoframe,textvariable=self.v_email,width=20,font=("Book Antiqua",12,"bold"))
        email_entry.grid(row=6,column=1,padx=10,pady=5,sticky=W)


        #PhoneNumber
        pno_label=Label(studentinfoframe,text="Phone Number",font=("Book Antiqua",12,"bold"),bg="white")
        pno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        pno_entry=ttk.Entry(studentinfoframe,textvariable=self.v_phone,width=20,font=("Book Antiqua",12,"bold"))
        pno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(studentinfoframe,text="Address",font=("Book Antiqua",12,"bold"),bg="white")
        address_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(studentinfoframe,textvariable=self.v_address,width=20,font=("Book Antiqua",12,"bold"))
        address_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Class Coordinator
        cc_label=Label(studentinfoframe,text="Class Coordinator",font=("Book Antiqua",12,"bold"),bg="white")
        cc_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        cc_entry=ttk.Entry(studentinfoframe,textvariable=self.v_cc,width=20,font=("Book Antiqua",12,"bold"))
        cc_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #RadioButtons
        self.v_radio=StringVar()
        rbtn1=ttk.Radiobutton(studentinfoframe,variable=self.v_radio,text="Take Photo Sample",value="Yes")
        rbtn1.grid(row=7,column=1)

        rbtn2=ttk.Radiobutton(studentinfoframe,variable=self.v_radio,text="No Photo Sample",value="No")
        rbtn2.grid(row=7,column=2)

        #FirstButtonFrameInStudentInfoFrame
        btn1_frame=Frame(studentinfoframe,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=305,width=730,height=40)

        save_btn=Button(btn1_frame,text="Save",command=self.add_data,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn1_frame,text="Update",command=self.update_data,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn1_frame,text="Delete",command=self.delete_data,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn1_frame,text="Reset",command=self.reset_data,width=18,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #SecondButtonFrameInStudentInfoFrame
        btn2_frame=Frame(studentinfoframe,bd=2,relief=RIDGE,bg="white")
        btn2_frame.place(x=5,y=345,width=730,height=40)

        takephoto_btn=Button(btn2_frame,text="Take Photo",command=self.generate_dataset,width=36,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=4)

        updatephotosample_btn=Button(btn2_frame,text="Update Photo",width=36,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        updatephotosample_btn.grid(row=0,column=5)

        #RightLabelFrame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Book Antiqua",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)


        #SearchSystem
        searchframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Book Antiqua",12,"bold"))
        searchframe.place(x=786,y=35,width=685,height=70)

        search_label=Label(searchframe,text="Search By :",font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(searchframe,font=("Book Antiqua",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(searchframe,width=20,font=("Book Antiqua",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(searchframe,text="Search",width=12,font=("Book Antiqua",8,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(searchframe,text="Show All",width=12,font=("Book Antiqua",8,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)


        #TableFrame
        tableframe=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        tableframe.place(x=5,y=85,width=684,height=350)

        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(tableframe,column=("dep","course","year","sem","id","name","roll","gender","sec","dob","email","phone","address","cc","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
       
       
       
       
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("cc",text="Class Coordinator")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("cc",width=120)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.data_fetch()
    
    
    
    
    def add_data(self):
        if self.v_dep.get()=="Select Department" or self.v_course.get()=="Select Course" or self.v_year.get()=="Select Year" or self.v_sem.get()=="Select Semester" or self.v_id.get()=="" or self.v_name.get()=="" or self.v_sec.get()=="Select Section" or self.v_roll.get()=="" or self.v_gender.get()=="Select Gender" or self.v_dob.get()=="" or self.v_email.get()=="" or self.v_phone.get()=="" or self.v_address.get()=="" or self.v_cc.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
               #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
                my_cursor=connection.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.v_dep.get(),
                                                                                                              self.v_course.get(),
                                                                                                              self.v_year.get(),
                                                                                                              self.v_sem.get(),
                                                                                                              self.v_id.get(),
                                                                                                              self.v_name.get(),
                                                                                                              self.v_sec.get(),
                                                                                                              self.v_roll.get(),
                                                                                                              self.v_gender.get(),
                                                                                                              self.v_dob.get(),
                                                                                                              self.v_email.get(),
                                                                                                              self.v_phone.get(),
                                                                                                              self.v_address.get(),
                                                                                                              self.v_cc.get(),
                                                                                                              self.v_radio.get()))


                connection.commit()
                self.data_fetch()
                connection.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)


    #FuntionForFetchingData
    def data_fetch(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
       #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
        my_cursor=connection.cursor()   
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            connection.commit()
        connection.close()     

    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.v_dep.set(data[0]),
        self.v_course.set(data[1]),
        self.v_year.set(data[2]),
        self.v_sem.set(data[3]),
        self.v_id.set(data[4]),
        self.v_name.set(data[5]),
        self.v_sec.set(data[6]),
        self.v_roll.set(data[7]),
        self.v_gender.set(data[8]),
        self.v_dob.set(data[9]),
        self.v_email.set(data[10]),
        self.v_phone.set(data[11]),
        self.v_address.set(data[12]),
        self.v_cc.set(data[13]),
        self.v_radio.set(data[14]),

    #UpdateButtonFunction
    def update_data(self):
        if self.v_dep.get()=="Select Department" or self.v_course.get()=="Select Course" or self.v_year.get()=="Select Year" or self.v_sem.get()=="Select Semester" or self.v_id.get()=="" or self.v_name.get()=="" or self.v_sec.get()=="Select Section" or self.v_roll.get()=="" or self.v_gender.get()=="Select Gender" or self.v_dob.get()=="" or self.v_email.get()=="" or self.v_phone.get()=="" or self.v_address.get()=="" or self.v_cc.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                updat=messagebox.askyesno("updat","Do you want to update the details",parent=self.root)
                if updat>0:
                    connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
                   #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
                    my_cursor=connection.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,CC=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                            self.v_dep.get(),
                                                                                                                                                                                            self.v_course.get(),
                                                                                                                                                                                            self.v_year.get(),
                                                                                                                                                                                            self.v_sem.get(),
                                                                                                                                                                                            self.v_name.get(),
                                                                                                                                                                                            self.v_sec.get(),
                                                                                                                                                                                            self.v_roll.get(),
                                                                                                                                                                                            self.v_gender.get(),
                                                                                                                                                                                            self.v_dob.get(),
                                                                                                                                                                                            self.v_email.get(),
                                                                                                                                                                                            self.v_phone.get(),
                                                                                                                                                                                            self.v_address.get(),
                                                                                                                                                                                            self.v_cc.get(),
                                                                                                                                                                                            self.v_radio.get(),
                                                                                                                                                                                            self.v_id.get()                                
                                                                                                                                                                                                            ))
                else:
                    if not updat:
                        return
                messagebox.showinfo("Success","Details have been successfully updated")
                connection.commit()
                self.data_fetch()
                connection.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)    


    #DeleteButtonFunction
    def delete_data(self):
        if self.v_id.get()=="":
            messagebox.showerror("Error","Please enter Student ID",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete","Do you want to delete the Details",parent=self.root)
                if delete>0:
                    connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
                   #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
                    my_cursor=connection.cursor()
                    sql="DELETE FROM student WHERE Student_id=%s"
                    val=(self.v_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                connection.commit()
                self.data_fetch()
                connection.close()
                messagebox.showinfo("Delete","Successfully deleted details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    
    #ResetButtonFunction
    def reset_data(self):
        self.v_dep.set("Select Department")
        self.v_course.set("Select Course")
        self.v_year.set("Select Year")
        self.v_sem.set("Select Semester")
        self.v_id.set("")
        self.v_name.set("")
        self.v_sec.set("Select Section")
        self.v_roll.set("")
        self.v_gender.set("Select Gender")
        self.v_dob.set("")
        self.v_email.set("")
        self.v_phone.set("")
        self.v_address.set("")
        self.v_cc.set("")
        self.v_radio.set("")


    #TakePhotoSamples
    def generate_dataset(self):
        if self.v_dep.get()=="Select Department" or self.v_course.get()=="Select Course" or self.v_year.get()=="Select Year" or self.v_sem.get()=="Select Semester" or self.v_id.get()=="" or self.v_name.get()=="" or self.v_sec.get()=="Select Section" or self.v_roll.get()=="" or self.v_gender.get()=="Select Gender" or self.v_dob.get()=="" or self.v_email.get()=="" or self.v_phone.get()=="" or self.v_address.get()=="" or self.v_cc.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="Kumar@arpit@24",database="face_recognition")
               #conn=mysql.connector.connect(host="sql6.freesqldatabase.com",username="sql6475557",password="",database="sql6475557")           
                my_cursor=connection.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,CC=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                            self.v_dep.get(),
                                                                                                                                                                                            self.v_course.get(),
                                                                                                                                                                                            self.v_year.get(),
                                                                                                                                                                                            self.v_sem.get(),
                                                                                                                                                                                            self.v_name.get(),
                                                                                                                                                                                            self.v_sec.get(),
                                                                                                                                                                                            self.v_roll.get(),
                                                                                                                                                                                            self.v_gender.get(),
                                                                                                                                                                                            self.v_dob.get(),
                                                                                                                                                                                            self.v_email.get(),
                                                                                                                                                                                            self.v_phone.get(),
                                                                                                                                                                                            self.v_address.get(),
                                                                                                                                                                                            self.v_cc.get(),
                                                                                                                                                                                            self.v_radio.get(),
                                                                                                                                                                                            self.v_id.get()==id+1                                
                                                                                                                                                                                            ))

                connection.commit()
                self.data_fetch()
                self.reset_data()
                connection.close()

                #LoadPredefinedDataOnFaceFrontalsFromOpencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #FunctionForCroppingImage
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

                        


                    



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 