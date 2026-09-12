from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:

    def __init__(self, root, back_command=None):
        self.root = root
        self.back_command = back_command
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # ================= MOBILE-STYLE NAVIGATION =================
        # The dashboard stays open underneath this screen. Use Back instead of
        # repeatedly clicking the window X button.
        self.back_btn = Button(
            self.root,
            text="← Back",
            command=self.go_back,
            cursor="hand2",
            font=("Arial", 12, "bold"),
            bg="darkgreen",
            fg="white",
            activebackground="green",
            activeforeground="white",
            bd=0,
            relief=FLAT
        )
        self.back_btn.place(x=20, y=5, width=120, height=35)
        self.root.bind("<Escape>", lambda event: self.go_back())


        title_lbl = Label(self.root, text="DEVELOPER       ",
                          font=("times new roman", 35, "bold"),
                          fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1550,height=45)


       
        img_top=Image.open(r"College_Images\developer1.webp")
        img_top=img_top.resize((1920, 1000),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1920, height=1000)

        #FRAME
        main_frame = Frame( f_lbl,bg="white", bd=2)
        main_frame.place(x=1000, y=50, width=500, height=660)

        img_top1=Image.open(r"College_Images\maneesh.jpg")
        img_top1=img_top1.resize((250, 250),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=250, height=250)

        #DEVELOPER INFO
        Label( main_frame, text="Hello MY Name Is Maneesh.",
              font=("times new roman", 15, "bold"),fg="darkblue",
              bg="white").place(x=0,y=5)
        
        Label( main_frame, text="I Am A Full Stack Developer.",
              font=("times new roman", 15, "bold"),fg="darkblue",
              bg="white").place(x=0,y=40)
        
        img2=Image.open(r"College_Images\developer2.webp")
        img2=img2.resize((610,410),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=-2,y=250,width=610,height=410)



    # ================= BACK TO DASHBOARD =================
        # Keep Back button above all existing images/labels.
        self.back_btn.lift()

    def go_back(self):
        """Return to the dashboard without requiring the window X button."""
        try:
            self.root.grab_release()
        except Exception:
            pass
        if self.back_command:
            self.back_command()
        else:
            self.root.destroy()


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
