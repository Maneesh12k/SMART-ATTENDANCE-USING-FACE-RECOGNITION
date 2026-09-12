from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from database_setup import get_connection
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Register:
    def __init__(self, root, back_command=None):
        self.root = root
        self.back_command = back_command
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")

        # ================= MOBILE-STYLE NAVIGATION =================
        self.back_btn = Button(
            self.root, text="← Back", command=self.go_back, cursor="hand2",
            font=("Arial", 12, "bold"), bg="darkgreen", fg="white",
            activebackground="green", activeforeground="white", bd=0, relief=FLAT
        )
        self.back_btn.place(x=20, y=5, width=120, height=35)
        self.root.bind("<Escape>", lambda event: self.go_back())



        # ================= VARIABLES ==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
        
        

        

        # ================= Background =================
        img = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\bg.jpg")
        img = img.resize((1550, 838))
        self.bg = ImageTk.PhotoImage(img)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1550, height=838)

        # ============ Left Image =================
        img1 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\leftregister.webp")
        img1 = img1.resize((470, 550))
        self.left_img = ImageTk.PhotoImage(img1)

        left_lbl = Label(self.root, image=self.left_img)
        left_lbl.place(x=50, y=100, width=470, height=550)


         #MAIN FRAME
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE", font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # =========== LABEL AND ENTRY =======================

        #-------------------------ROWS 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #------------------------ ROWS 2


        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


    


         # ================= Row 3 =================
        Label(frame, text="Security Question",font=("times new roman",15,"bold"), bg="white").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(
            frame,font=("times new roman",15,"bold"), textvariable=self.var_securityQ, state="readonly",
            values=("Select", "Your Birth Place", "Your Pet Name","Your Father Name","Your Mother Name"))
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        Label(frame, text="Answer",font=("times new roman",15,"bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_securityA).place(x=370, y=270,width=250)



        #--------------------ROWS 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ================= Check Button =================
        Checkbutton(frame,
                    text="I Agree The Terms & Conditions",
                    variable=self.var_check,
                    onvalue=1, offvalue=0).place(x=50, y=380)

        # ================ BUTTONS =======================

        img=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\registernow.png")
        img=img.resize((200,45),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white").place(x=50,y=450,width=200)

    


        # ================= FUNCTION =================
    def register_data(self):
        if (self.var_fname.get() == "" or
            self.var_email.get() == "" or
            self.var_securityQ.get() == "Select"):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match")

        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to terms & conditions")

        else:
            try:
                conn = get_connection()
                my_cursor = conn.cursor()
                
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists")
                else:
                    my_cursor.execute(
                        "INSERT INTO register (fname,lname,contact,email,securityQ,securityA,password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                            )
                            
                            )
                    
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully")
                    
                conn.close()
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}")



    
            


        




    def go_back(self):
        if self.back_command:
            self.back_command()
        else:
            self.root.destroy()


# ================= MAIN =================
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()