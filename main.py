from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image2.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(self.root,text="AUTOMATIC ATTENDANCE MONITORING SYSTEM USING FACE DETECTION AND FACE RECOGNITION",font=("Book Antiqua",20,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student Details Button
        img4=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image3.jpg") 
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(self.root,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=200,width=220,height=220)

        b1_1=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=400,width=220,height=40)



        #Detection Face Button
        img5=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image4.jpeg") 
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(self.root,image=self.photoimg5,cursor="hand2")
        b1.place(x=1100,y=200,width=220,height=220)

        b1_1=Button(self.root,text="Face Detector",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=400,width=220,height=40)



         #Attendance Button
        img6=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image5.jpg") 
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(self.root,image=self.photoimg6,cursor="hand2")
        b1.place(x=1100,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Attendance",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=690,width=220,height=40)


         #Train Data Button
        img8=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image7.png") 
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(self.root,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=690,width=220,height=40)


         #Exit Button
        img11=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image10.jpg") 
        img11=img11.resize((110,110),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(self.root,image=self.photoimg11,cursor="hand2")
        b1.place(x=1400,y=590,width=110,height=110)

        b1_1=Button(self.root,text="Exit",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1400,y=690,width=110,height=30)

        
    #FunctionForImportingStudentFile
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)










if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()                                    