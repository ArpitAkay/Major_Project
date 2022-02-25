from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


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
        self.v_sec=StringVar()
        self.v_roll=StringVar()
        self.v_gender=StringVar()
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
        dept_label=Label(currentcourseframe,text="Deparatment",font=("Book Antiqua",12,"bold"),bg="white")
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
        year_combo["values"]=("Select Year","Computer Science","Information Technology","Electronics and Communication","Petroleum","Humanities and Social Sciences","Hotel Management and Hospitality","Biotechnology","Electrical","Management","Commerce","Nursing","Civil","Mechanical","Life Science","Paramedical Science","Computer Application")
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

        section_entry=ttk.Entry(studentinfoframe,textvariable=self.v_sec,width=20,font=("Book Antiqua",12,"bold"))
        section_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #RollNumber
        rno_label=Label(studentinfoframe,text="Roll Number",font=("Book Antiqua",12,"bold"),bg="white")
        rno_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        rno_entry=ttk.Entry(studentinfoframe,textvariable=self.v_roll,width=20,font=("Book Antiqua",12,"bold"))
        rno_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Gender
        gender_label=Label(studentinfoframe,text="Gender",font=("Book Antiqua",12,"bold"),bg="white")
        gender_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(studentinfoframe,textvariable=self.v_gender,width=20,font=("Book Antiqua",12,"bold"))
        gender_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #DateOfBirth
        dob_label=Label(studentinfoframe,text="Date Of Birth",font=("Book Antiqua",12,"bold"),bg="white")
        dob_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

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
        self.v_radio1=StringVar()
        rbtn1=ttk.Radiobutton(studentinfoframe,textvariable=self.v_radio1,text="Take Photo Sample",value="Yes")
        rbtn1.grid(row=7,column=1)

        self.v_radio2=StringVar()
        rbtn2=ttk.Radiobutton(studentinfoframe,textvariable=self.v_radio2,text="No Photo Sample",value="No")
        rbtn2.grid(row=7,column=2)

        #FirstButtonFrameInStudentInfoFrame
        btn1_frame=Frame(studentinfoframe,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=305,width=730,height=40)

        save_btn=Button(btn1_frame,text="Save",command=self.add_data,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn1_frame,text="Update",width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn1_frame,text="Delete",width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn1_frame,text="Reset",width=18,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #SecondButtonFrameInStudentInfoFrame
        btn2_frame=Frame(studentinfoframe,bd=2,relief=RIDGE,bg="white")
        btn2_frame.place(x=5,y=345,width=730,height=40)

        takephoto_btn=Button(btn2_frame,text="Take Photo",width=36,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
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
        self.student_table.column("cc",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)


    def add_data(self):
        if self.v_dep.get()=="Select Department" or self.v_course.get()=="Select Course" or self.v_year.get()=="Select Year" or self.v_sem.get()=="Select Semester" or self.v_id.get()=="" or self.v_name.get()=="" or self.v_sec.get()=="" or self.v_roll.get()=="" or self.v_gender.get()=="" or self.v_dob.get()=="" or self.v_email.get()=="" or self.v_phone.get()=="" or self.v_address.get()=="" or self.v_cc.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            pass                     







if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 