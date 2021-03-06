from math import fabs
from mimetypes import init
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#from numpy import delete
import cv2
import os 
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        #TextVariablesForDataStorage
        self.v_aid=StringVar()
        self.v_aroll=StringVar()
        self.v_aname=StringVar()
        self.v_adep=StringVar()
        self.v_atime=StringVar()
        self.v_adate=StringVar()
        self.v_astatus=StringVar()








        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FRS\Major_Project\images\image1.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Book Antiqua",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bgimage,bd=2,bg="white")
        main_frame.place(x=15,y=60,width=1495,height=715)

        #LeftLabelFrame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Book Antiqua",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=685)

        #AttendanceID
        Aid_label=Label(Left_frame,text="Attendance ID",font=("Book Antiqua",12,"bold"),bg="white")
        Aid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Aid_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_aid,font=("Book Antiqua",12,"bold"))
        Aid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #RollNumber
        roll_label=Label(Left_frame,text="Roll Number",font=("Book Antiqua",12,"bold"),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_aroll,font=("Book Antiqua",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Name
        name_label=Label(Left_frame,text="Name",font=("Book Antiqua",12,"bold"),bg="white")
        name_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_aname,font=("Book Antiqua",12,"bold"))
        name_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        dep_label=Label(Left_frame,text="Department",font=("Book Antiqua",12,"bold"),bg="white")
        dep_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        #dep_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_adep,font=("Book Antiqua",12,"bold"))
        #dep_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(Left_frame,textvariable=self.v_adep,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        dep_combo["values"]=("Select Deparatment","Engineering","Management","Arts and Science","Business Studies","Fine Arts and Communication")
        dep_combo.current(0)
        dep_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)










        
        #Time
        time_label=Label(Left_frame,text="Time",font=("Book Antiqua",12,"bold"),bg="white")
        time_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_atime,font=("Book Antiqua",12,"bold"))
        time_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Date
        date_label=Label(Left_frame,text="Date",font=("Book Antiqua",12,"bold"),bg="white")
        date_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(Left_frame,width=20,textvariable=self.v_adate,font=("Book Antiqua",12,"bold"))
        date_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        
        #AttendanceStatus
        as_label=Label(Left_frame,text="Attendance Status",font=("Book Antiqua",12,"bold"),bg="white")
        as_label.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        as_combo=ttk.Combobox(Left_frame,textvariable=self.v_astatus,font=("Book Antiqua",12,"bold"),width=18,state="read only")
        as_combo["values"]=("Select Attendance Status","Present","Absent")
        as_combo.current(0)
        as_combo.grid(row=6,column=1,padx=10,pady=5,sticky=W)

        #ButtonFrameInLeft_Frame
        btn1_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=305,width=730,height=40)

        import_btn=Button(btn1_frame,text="Import csv",command=self.importCsv,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn1_frame,text="Export csv",command=self.exportCsv,width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn1_frame,text="Update",width=17,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn1_frame,text="Reset",command=self.reset_data,width=18,font=("Book Antiqua",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        #RightFrame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Book Antiqua",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=685)

        #TableFrame
        tableframe=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        tableframe.place(x=5,y=10,width=684,height=640)

        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(tableframe,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")
        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=200)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=120)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #FunctionForFetchingData
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #FunctionForImportingData
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    

    #FunctionForExportingData
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)

    def get_cursor(self,events=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.v_aid.set(rows[0]),
        self.v_aroll.set(rows[1]),
        self.v_aname.set(rows[2]),
        self.v_adep.set(rows[3]),
        self.v_atime.set(rows[4]),
        self.v_adate.set(rows[5]),
        self.v_astatus.set(rows[6]),


    #ResetButtonFunction
    def reset_data(self):
        self.v_aid.set("")
        self.v_aroll.set("")
        self.v_aname.set("")
        self.v_adep.set("Select Department")
        self.v_atime.set("")
        self.v_adate.set("")
        self.v_astatus.set("Select Attendance Status")
        











if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 