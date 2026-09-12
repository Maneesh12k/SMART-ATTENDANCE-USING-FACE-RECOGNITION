from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class HELP:

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


        title_lbl = Label(self.root, text="HELP DESK      ",
                          font=("times new roman", 35, "bold"),
                          fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1550,height=45)


       
        img_top=Image.open(r"College_Images\help.jpg")
        img_top=img_top.resize((1528, 780),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1528, height=780)

        Label(f_lbl, text="Email:maneeshkumar6309@gmail.com",
              font=("times new roman", 20, "bold"),fg="black",
              bg="red").place(x=550,y=420)



        # ================= MAIN =================

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

if __name__ == "__main__":
    root = Tk()
    obj = HELP(root)
    root.mainloop()
