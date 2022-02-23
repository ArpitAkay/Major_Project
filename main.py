from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #Image1
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\GEU2008.jpg") 
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Image2
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image1.jpg") 
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Image3
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\GEU2008.jpg") 
        img3=img3.resize((550,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image2.jpg") 
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bgimage,text="AUTOMATIC ATTENDANCE MONITORING SYSTEM USING FACE DETECTION AND FACE RECOGNITION",font=("Book Antiqua",20,"bold"),bg="white",fg="blue")
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
        b1.place(x=500,y=200,width=220,height=220)

        b1_1=Button(self.root,text="Face Detector",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=400,width=220,height=40)



         #Attendance Button
        img6=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image5.jpg") 
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(self.root,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=200,width=220,height=220)

        b1_1=Button(self.root,text="Attendance",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=400,width=220,height=40)




         #Help Desk Button
        img7=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image6.jfif") 
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(self.root,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=200,width=220,height=220)

        b1_1=Button(self.root,text="Help Desk",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=400,width=220,height=40)




         #Train Data Button
        img8=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image7.png") 
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(self.root,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=690,width=220,height=40)



         #Database Button
        img9=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image8.jfif") 
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(self.root,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Database",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=690,width=220,height=40)



         #Developer Button
        img10=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image9.jpg") 
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(self.root,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Developer",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=690,width=220,height=40)



         #Exit Button
        img11=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image10.jpg") 
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(self.root,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=490,width=220,height=220)

        b1_1=Button(self.root,text="Exit",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=690,width=220,height=40)

        #FunctionForImportingStudentFile
        
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)










if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()                                    