from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox
import os

# Keep all image/data paths portable so the project works after unzipping.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
from student import Student
from train import Train
from face_recognition_page import Face_Recognition_Page
from attendance import Attendance
from developer import Developer
from help import HELP
from time import strftime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

      
        #first image
        img = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\face recognition left.png")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
           
           #second image
        img1 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\face recognition middle.webp")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


           #third image
        img2 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\face recognition.jpg")
        img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # BACKGROUND 
        img3 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\background.jpg")
        img3 = img3.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1920, height=1080)

        title_lbl = Label(bg_img,
                          text="AI BASED SMART ATTENDANCE USING FACE RECOGNITION",
                          font=("times new roman", 30, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=-20, y=0, width=1550, height=45)


         #================= TIME ===============

     # TIME LABEL
        self.lbl = Label(bg_img, font=("times new roman", 20, "bold"),
                         background="white", foreground="blue")
        self.lbl.place(x=1350, y=5, width=180, height=35)

        self.time()
   


        #  STUDENT BUTTON 
        img4 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\student deatils.avif")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,
               command=self.student_details,
               cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1=Button(bg_img, text="Student Details",
               command=self.student_details,
               cursor="hand2",
               font=("times new roman", 15, "bold"),
               bg="red", fg="white")
        b1.place(x=200, y=300, width=220, height=40)

        #DETECT fACE BUTTON
        img5=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\face detect.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        
        b1=Button(bg_img,text="Face Detect",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=500,y=300,width=220,height=40)

           #ATTENDANCE BUTTON
        img6=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\Face-Attendance.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=800,y=300,width=220,height=40)

           #HELP DESK
        img7=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\help desk.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        
        b1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)

             #TRAIN DATA
        img8=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\train data.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=200,y=600,width=220,height=40)

        
             #PHOTO
        img9=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\photo.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=500,y=400,width=220,height=220)

        
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=500,y=600,width=220,height=40)
        

        
             #DEVELOPER
        img10=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\developer.webp")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        
        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1.place(x=800,y=600,width=220,height=40)





        #EXIT BUTTON 
        img11=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\exit.webp")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)


        b1=Button(bg_img, text="Exit",
               command=self.iExit,
               cursor="hand2",
               font=("times new roman", 15, "bold"),
               bg="red", fg="white")
        b1.place(x=1100, y=600, width=220, height=40)

       # ================= OPEN STUDENT WINDOW =================
    def show_dashboard(self):
        """Return focus to the dashboard after a feature screen is closed."""
        try:
            if hasattr(self, "new_window") and self.new_window.winfo_exists():
                self.new_window.destroy()
        except Exception:
            pass
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = Student(self.new_window, self.show_dashboard)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = Train(self.new_window, self.show_dashboard)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = Face_Recognition_Page(self.new_window, self.show_dashboard)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = Attendance(self.new_window, self.show_dashboard) 


    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = Developer(self.new_window, self.show_dashboard)


    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.transient(self.root)
        self.app = HELP(self.new_window, self.show_dashboard)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)



  
 
 

# ================= OPEN IMAGE FOLDER =================
    def open_image(self):
        os.startfile(os.path.join(BASE_DIR, "data"))

    def iExit(self):
        iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if iExit:
            self.root.destroy()

    


# ================= APPLICATION ENTRY POINT =================
# Start the complete application from ONE file:
# main.py -> Login -> Register/Forgot Password -> Dashboard -> Features
if __name__ == "__main__":
    from login import Login_Window

    root = Tk()
    app = Login_Window(root)
    root.mainloop()