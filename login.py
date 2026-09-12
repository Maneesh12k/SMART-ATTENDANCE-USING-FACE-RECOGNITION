from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from database_setup import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from register import Register
from forgot_password import Forgot_Password


def main():
    root = Tk()
    app = Login_Window(root)
    root.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System - Login")
        self.root.geometry("1920x1080+0+0")

        # ================= Database Bootstrap =================
        # Create the original register_page database/table if it is missing.
        try:
            from database_setup import ensure_database
            ensure_database()
        except Exception as es:
            messagebox.showerror(
                "Database Error",
                "MySQL could not be prepared.\n\n"
                f"Error: {es}\n\n"
                "Make sure MySQL is running and the root password in "
                "database_setup.py matches your MySQL installation.",
                parent=self.root,
            )

        # ================= Background =================
        img = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\background.webp")
        img = img.resize((1550, 838), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1550, height=838)

        # ================= Frame =================
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=450, height=550)

        # ================= Login Image =================
        img1 = Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\login.webp")
        img1 = img1.resize((300, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=690, y=175, width=300, height=200)

        # ================= Title =================
        get_str = Label(frame, text="Login Here", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=150, y=200)

        # ================= Username =================
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=110, y=250)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=110, y=280, width=250)

        # ================= Password =================
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=110, y=310)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15),show="*")
        self.txtpass.place(x=110, y=340, width=250)

        # ================= Login Button =================
        loginbtn = Button(frame,command=self.login ,text="Login",
                          font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE,
                          fg="white", bg="red")
        loginbtn.place(x=160, y=390, width=120)

        # ================= Register Button =================
        registerbtn = Button(frame,command=self.register_window, text="New User Register",
                             font=("times new roman", 12, "bold"),
                             borderwidth=0,
                             fg="white", bg="black")
        registerbtn.place(x=140, y=440, width=180)

        # ================= Forget Password =================
        forgetbtn = Button(frame, command=self.forgot_password_window, text="Forget Password",
                           font=("times new roman", 12, "bold"),
                           borderwidth=0,
                           fg="white", bg="black")
        forgetbtn.place(x=140, y=480, width=180)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            try:
                conn = get_connection()
                
                my_cursor = conn.cursor()
                
                query = "SELECT * FROM register WHERE email=%s AND password=%s"
                value = (self.txtuser.get(), self.txtpass.get())
                
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Login Successful", parent=self.root)
                    conn.close()

                    # Open the dashboard in the SAME application window.
                    # The user starts the project once: Login -> Dashboard -> Features.
                    from main import Face_Recognition_System
                    for widget in self.root.winfo_children():
                        widget.destroy()
                    self.app = Face_Recognition_System(self.root)
                    self.root.title("Face Recognition System")
                    self.root.deiconify()
                    self.root.lift()
                    self.root.focus_force()

            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}")


    def show_login(self):
        """Return to the login screen from a child screen."""
        try:
            if hasattr(self, "new_window") and self.new_window.winfo_exists():
                self.new_window.destroy()
        except Exception:
            pass
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window, self.show_login)

    def forgot_password_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Forgot_Password(self.new_window, self.show_login)

# ========== MAIN FUNCTION ==========
def main():
    root = Tk()
    app = Login_Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()