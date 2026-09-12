from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from database_setup import get_connection


class Forgot_Password:
    def __init__(self, root, back_command=None):
        self.root = root
        self.back_command = back_command
        self.root.title("Forgot Password")
        self.root.geometry("400x400+500+150")

        # ================= MOBILE-STYLE NAVIGATION =================
        self.back_btn = Button(
            self.root, text="← Back", command=self.go_back, cursor="hand2",
            font=("Arial", 11, "bold"), bg="darkgreen", fg="white", bd=0
        )
        self.back_btn.place(x=20, y=5, width=100, height=32)
        self.root.bind("<Escape>", lambda event: self.go_back())


        # ===== Variables =====
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_new_password = StringVar()

        # ===== Title =====
        title = Label(self.root, text="Forgot Password", font=("times new roman", 18, "bold"))
        title.pack(pady=10)

        # ===== Email =====
        lbl_email = Label(self.root, text="Email", font=("times new roman", 12))
        lbl_email.pack()
        txt_email = ttk.Entry(self.root, textvariable=self.var_email, width=30)
        txt_email.pack(pady=5)

        # ===== Security Question =====
        lbl_q = Label(self.root, text="Select Security Question", font=("times new roman", 12))
        lbl_q.pack()

        combo_q = ttk.Combobox(self.root, textvariable=self.var_securityQ, state="readonly")
        combo_q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Favorite Teacher")
        combo_q.current(0)
        combo_q.pack(pady=5)

        # ===== Answer =====
        lbl_ans = Label(self.root, text="Answer", font=("times new roman", 12))
        lbl_ans.pack()
        txt_ans = ttk.Entry(self.root, textvariable=self.var_securityA, width=30)
        txt_ans.pack(pady=5)

        # ===== New Password =====
        lbl_pass = Label(self.root, text="New Password", font=("times new roman", 12))
        lbl_pass.pack()
        txt_pass = ttk.Entry(self.root, textvariable=self.var_new_password, width=30, show="*")
        txt_pass.pack(pady=5)

        # ===== Button =====
        btn_reset = Button(self.root, text="Reset Password", command=self.reset_password,
                           bg="red", fg="white")
        btn_reset.pack(pady=20)

        # Keep Back visible above the form widgets.
        self.back_btn.lift()

    # ===== Reset Password Function =====
    def reset_password(self):
        if (self.var_email.get() == "" or self.var_securityQ.get() == "Select" or
                self.var_securityA.get() == "" or self.var_new_password.get() == ""):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = get_connection()
            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            value = (self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get())

            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Details")
            else:
                update_query = "UPDATE register SET password=%s WHERE email=%s"
                val = (self.var_new_password.get(), self.var_email.get())

                my_cursor.execute(update_query, val)
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Password Reset Successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}")


    def go_back(self):
        if self.back_command:
            self.back_command()
        else:
            self.root.destroy()


# ===== Run File Directly =====
if __name__ == "__main__":
    root = Tk()
    obj = Forgot_Password(root)
    root.mainloop()