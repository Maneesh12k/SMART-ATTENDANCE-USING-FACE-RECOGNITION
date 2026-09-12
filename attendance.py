from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import csv
from datetime import datetime


class Attendance:

    def __init__(self, root, back_command=None):
        self.root = root
        self.back_command = back_command
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance Management System")

        # ================= MOBILE-STYLE NAVIGATION =================
        self.back_btn = Button(
            self.root, text="← Back", command=self.go_back, cursor="hand2",
            font=("Arial", 12, "bold"), bg="darkgreen", fg="white",
            activebackground="green", activeforeground="white", bd=0, relief=FLAT
        )
        self.back_btn.place(x=20, y=5, width=120, height=35)
        self.root.bind("<Escape>", lambda event: self.go_back())


        self.mydata = []

        # ================= VARIABLES =================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ================= IMAGES =================
        img = Image.open(r"College_Images\student middle.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"College_Images\student right.jpg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"College_Images\background.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=0, y=200, width=1530, height=710)

        # ================= TITLE =================
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=205, width=1505, height=620)

        # ================= LEFT FRAME =================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white",
                                relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=10, width=720, height=600)

        img_left = Image.open(r"College_Images\attendance.webp")
        img_left = img_left.resize((710, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=710, height=130)

        Left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        Left_inside_frame.place(x=0, y=140, width=714, height=430)

        # ================= FORM =================
        Label(Left_inside_frame, text="Attendance ID :",font="comicsansns 11 bold",bg="white").grid(row=0, column=0, padx=10, pady=5,sticky=W)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_id).grid(row=0, column=1,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Roll :",font="comicsansns 11 bold", bg="white").grid(row=0, column=2)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_roll).grid(row=0, column=3,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Name :",font="comicsansns 11 bold", bg="white").grid(row=1, column=0)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_name).grid(row=1, column=1,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Department :",font="comicsansns 11 bold", bg="white").grid(row=1, column=2)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_dep).grid(row=1, column=3,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Time :",font="comicsansns 11 bold", bg="white").grid(row=2, column=0)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_time).grid(row=2, column=1,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Date :",font="comicsansns 11 bold", bg="white").grid(row=2, column=2)
        ttk.Entry(Left_inside_frame, textvariable=self.var_atten_date).grid(row=2, column=3,padx=10,pady=5,sticky=W)

        Label(Left_inside_frame, text="Attendance Status :",font="comicsansns 11 bold", bg="white").grid(row=3, column=0,padx=10,pady=5,sticky=W)

        self.atten_status = ttk.Combobox(
            Left_inside_frame,width=20,font="comicsansns 11 bold",
            textvariable=self.var_atten_attendance,
            state="readonly",
            values=("Present", "Absent")
        )
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)

        # ================= BUTTONS =================
        btn_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", command=self.updateData,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Delete", command=self.deleteData,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white").grid(row=0, column=3)
        Button(btn_frame, text="Reset", command=self.resetData,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white").grid(row=0, column=4)

        # ================= RIGHT FRAME =================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                 relief=RIDGE, text="Student Details")
        Right_frame.place(x=750, y=10, width=750, height=550)

        table_frame = Frame(Right_frame)
        table_frame.place(x=5, y=5, width=710, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table = ttk.Treeview(
            table_frame,
            columns=("id","name","roll","department","time","date","attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        for col in self.table["columns"]:
            self.table.heading(col, text=col.upper())
            self.table.column(col, width=100)

        self.table["show"] = "headings"
        self.table.pack(fill=BOTH, expand=1)

        self.table.bind("<ButtonRelease>", self.get_cursor)

        # Load the project's live attendance file automatically.
        # Face recognition writes the current date/time to this same file.
        self.load_live_attendance()

    # ================= FUNCTIONS =================

        # Keep Back button above all existing images/labels.
        self.back_btn.lift()

    def load_live_attendance(self):
        """Load the attendance.csv generated by face recognition."""
        live_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
        self.csv_file = live_file

        if not os.path.exists(live_file):
            self.mydata = [["ID", "Name", "Roll", "Department", "Time", "Date", "Status"]]
            with open(live_file, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(self.mydata[0])
        else:
            try:
                with open(live_file, "r", newline="", encoding="utf-8-sig") as f:
                    self.mydata = list(csv.reader(f))
            except Exception:
                self.mydata = []

        header = ["ID", "Name", "Roll", "Department", "Time", "Date", "Status"]
        if not self.mydata or self.mydata[0] != header:
            self.mydata = [header] + [row for row in self.mydata if row and row[0] != "ID"]
            with open(live_file, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(self.mydata)

        self.refresh_table()

    def importCsv(self):
        live_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
        file_path = filedialog.askopenfilename(
            initialdir=os.path.dirname(live_file),
            initialfile=os.path.basename(live_file),
            filetypes=[("CSV Files", "*.csv")]
        )
        if not file_path:
            return

        self.csv_file = file_path

        with open(file_path, "r", newline="", encoding="utf-8-sig") as f:
            self.mydata = list(csv.reader(f))

        self.refresh_table()

    def exportCsv(self):
        if not self.mydata:
            messagebox.showerror("Error", "No data")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv")
        if not file_path:
            return
        with open(file_path, "w", newline="") as f:
            csv.writer(f).writerows(self.mydata)
        messagebox.showinfo("Success", "Exported")

    def refresh_table(self):
        self.table.delete(*self.table.get_children())
        for row in self.mydata:
            self.table.insert("", END, values=row)

    def get_cursor(self, event=""):
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        if len(values) < 7:
            return
        
        self.var_atten_id.set(values[0])
        self.var_atten_name.set(values[1])
        self.var_atten_roll.set(values[2])
        self.var_atten_dep.set(values[3])
        self.var_atten_time.set(values[4])
        self.var_atten_date.set(values[5])
        self.var_atten_attendance.set(values[6])

    def updateData(self):
        selected = self.table.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a record")
            return
        
        import re

# ===== VALIDATION =====

# 1. Empty field check
        if (self.var_atten_id.get() == "" or
            self.var_atten_name.get() == "" or
            self.var_atten_roll.get() == "" or
            self.var_atten_dep.get() == "" or
            self.var_atten_time.get() == "" or
            self.var_atten_date.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return


# 2. ID must be numeric (13 digits if enrollment)
        if not re.fullmatch(r"\d{13}", self.var_atten_id.get()):
            messagebox.showerror("Error", "Attendance ID must be 13 digits", parent=self.root)
            return


# 3. Roll number must be numeric
        if not self.var_atten_roll.get().isdigit():
            messagebox.showerror("Error", "Roll number must be numeric", parent=self.root)
            return


# 4. Name should contain only letters
        if not re.fullmatch(r"[A-Za-z ]+", self.var_atten_name.get()):
            messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
            return


# 5. Time format HH:MM:SS
        if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", self.var_atten_time.get()):
            messagebox.showerror("Error", "Time must be in HH:MM:SS format", parent=self.root)
            return


# ===== DATE VALIDATION =====
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", self.var_atten_date.get()):
            messagebox.showerror("Error", "Date must be DD/MM/YYYY")
            return

        try:
            datetime.strptime(self.var_atten_date.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date")
            return

        new_data = (
            self.var_atten_id.get(),
            self.var_atten_name.get(),
            self.var_atten_roll.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        )

    # update table
        self.table.item(selected, values=new_data)

    # update list
        index = self.table.index(selected)
        self.mydata[index] = list(new_data)

    # ✅ SAVE BACK TO CSV
        try:
            with open(self.csv_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(self.mydata)

            messagebox.showinfo("Success", "Attendance updated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to update CSV: {str(e)}")


    def deleteData(self):
        """Delete the selected attendance record from the live attendance.csv."""
        selected = self.table.focus()
        values = self.table.item(selected, "values")
        if not selected or len(values) < 7 or str(values[0]).upper() == "ID":
            messagebox.showerror("Error", "Please select an attendance record to delete", parent=self.root)
            return

        if not messagebox.askyesno(
            "Delete Attendance",
            f"Delete attendance for {values[1]} on {values[5]}?",
            parent=self.root
        ):
            return

        try:
            live_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
            with open(live_file, "r", newline="", encoding="utf-8-sig") as f:
                rows = list(csv.reader(f))
            header = ["ID", "Name", "Roll", "Department", "Time", "Date", "Status"]
            data_rows = rows[1:] if rows and rows[0] == header else rows
            target = list(values)
            removed = False
            new_rows = []
            for row in data_rows:
                if not removed and row == target:
                    removed = True
                    continue
                new_rows.append(row)
            if not removed:
                messagebox.showerror("Error", "Selected attendance record was not found in the live CSV.", parent=self.root)
                return
            with open(live_file, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows([header] + new_rows)
            self.mydata = [header] + new_rows
            self.csv_file = live_file
            self.refresh_table()
            self.resetData()
            messagebox.showinfo("Delete", "Attendance record deleted successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete attendance: {e}", parent=self.root)

    def resetData(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Present")


    # ================= BACK TO DASHBOARD =================
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
    app = Attendance(root)
    root.mainloop()
