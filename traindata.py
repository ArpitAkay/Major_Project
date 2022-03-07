from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Dataset")

        
        #BackgroundImage
        bg_img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\FaceRecognitionSystem\images\image2.jpg") 
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgimage=Label(self.root,image=self.bg_photoimg)
        bgimage.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(self.root,text="TRAIN DATASET",font=("Book Antiqua",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #TrainDataButton
        b=Button(self.root,text="Train Data",cursor="hand2",font=("Book Antiqua",15,"bold"),bg="darkblue",fg="white")
        b.place(x=200,y=400,width=220,height=40)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]

        #ConvertedIntoGrayScale
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.'[1]))
        







if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop() 