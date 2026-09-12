from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from datetime import datetime
from train import rebuild_face_model



class Student:

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


        #first image
        img=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\student left.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\student middle.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\student right.jpg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

         #background
        img3=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\background.jpg")
        img3=img3.resize((1920,1080),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1920,height=1080)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        main_frame = Frame(bg_img,bg="white", bd=2)
        main_frame.place(x=10, y=50, width=1505, height=665)

          

        # ============ Variables ============
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_course = StringVar()
        self.var_radio = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_parent = StringVar()
        




        # ================= LEFT FRAME =================
        Left_frame = LabelFrame(main_frame, bd=2,bg="white",
                                relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=10, width=750, height=650)

        img_left=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\Student-Management-System.webp")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # ================= Course Frame =================
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white",
                                          relief=RIDGE,
                                          text="Current Course Information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        Label(current_course_frame, text="Department",
              font=("times new roman", 12, "bold"),
              bg="white").grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,
                                 textvariable=self.var_dep,cursor="hand2",font=("times new roman",12,"bold"),
                                 state="readonly",
                                 width=20)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        Label(current_course_frame, text="Course",
              font=("times new roman", 12, "bold"),
              bg="white").grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,
                                    textvariable=self.var_course,cursor="hand2",font=("times new roman",12,"bold"),
                                    state="readonly")
        course_combo["values"] = ("Select Course", "CSE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        # Year
        Label(current_course_frame, text="Year",
              font=("times new roman", 12, "bold"),
              bg="white").grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,
                                  textvariable=self.var_year,cursor="hand2",font=("times new roman",12,"bold"),
                                  state="readonly",
                                  width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        # Semester
        Label(current_course_frame, text="Semester",
              font=("times new roman", 12, "bold"),
              bg="white").grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,
                                      textvariable=self.var_sem,cursor="hand2",font=("times new roman",12,"bold"),
                                      state="readonly",
                                      width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2",
                                    "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

        # ================= Student Info Frame =================
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white",
                                         relief=RIDGE,
                                         text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=5, y=300, width=720, height=320)

         #student id
        studentId_label=Label(Class_Student_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         #student name
        studentName_label=Label(Class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


          #class division
        class_div_label=Label(Class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


         #gender
        gender_label=Label(Class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        

        gender_combo = ttk.Combobox(Class_Student_frame,
                                      textvariable=self.var_gender,cursor="hand2",font=("times new roman",12,"bold"),
                                      state="readonly",
                                      width=20)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)



         #roll no
        roll_no_label=Label(Class_Student_frame,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(Class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #EMAIL
        email_label=Label(Class_Student_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


          #phone no
        phone_no_label=Label(Class_Student_frame,text="Phone No :",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


          #address
        address_label=Label(Class_Student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


         #parent phone no
        parent_phone_no_label=Label(Class_Student_frame,text="Parent Phone No :",font=("times new roman",12,"bold"),bg="white")
        parent_phone_no_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        parent_phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_parent,width=20,font=("times new roman",12,"bold"))
        parent_phone_no_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio button
        self.var_radio=StringVar()
        radionbtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        
        radionbtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)


        
        # ================= Buttons =================
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=715, height=85)

        Button(btn_frame, cursor="hand2", text="Save", command=self.add_data,
               width=23,font=("times new roman",14,"bold"),bg="blue",fg="white").grid(row=0, column=0)
        
        Button(btn_frame,cursor="hand2",text="Update",command=self.update_data,width=20,font=("times new roman",14,"bold"),bg="blue",fg="white").grid(row=0,column=1)

        Button(btn_frame,cursor="hand2",text="Delete",command=self.delete_data,width=22,font=("times new roman",14,"bold"),bg="blue",fg="white").grid(row=0,column=2)

        Button(btn_frame, cursor="hand2", text="Reset", command=self.reset_data,
               width=23,font=("times new roman",14,"bold"),bg="blue", fg="white").grid(row=1, column=0)
        
        Button(btn_frame,cursor="hand2",text="Take Photo Sample",command=self.generate_dataset,width=20,font=("times new roman",14,"bold"),bg="blue",fg="white").grid(row=1,column=1)

        Button(btn_frame,cursor="hand2",text="Update Photo Sample",
       command=self.update_photo_sample, width=22,font=("times new roman",14,"bold"),bg="blue",fg="white").grid(row=1,column=2)



        # ================= RIGHT FRAME =================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                 relief=RIDGE,
                                 text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=740, height=650)

        img_right=Image.open(r"C:\Users\manee\OneDrive\Desktop\Face Recognition System\College_Images\right frame.jpg")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        
                # ================= Search System in Right Frame =================
        search_frame = LabelFrame(Right_frame,cursor="hand2", bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=5, width=725, height=70)

        search_label = Label(search_frame,cursor="hand2", text="Search By :", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(search_frame,cursor="hand2", font=("times new roman", 12, "bold"),
                                         state="readonly", width=15)
        self.search_combo["values"] = ("Select", "Roll No", "Phone No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.search_entry = ttk.Entry(search_frame,cursor="hand2", width=20, font=("times new roman", 12, "bold"))
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10,
                            font=("times new roman", 12, "bold"),
                            bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5)

        showAll_btn = Button(search_frame, cursor="hand2",text="Show All", width=10,
                             font=("times new roman", 12, "bold"),
                             bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

            # ================= Table Frame =================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=75, width=725, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("dep","year","sem","course","id", "name", "division", "gender", "roll",
                     "dob", "email", "phone", "address", "parent"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("parent", text="Parent Phone")



        
       

        self.student_table["show"] = "headings"

        for col in ("dep","year","sem","course","id","name","division","gender","roll",
            "dob","email","phone","address","parent"):
          self.student_table.column(col, width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()
        
           

    # ================= ADD DATA FUNCTION =================
        # Keep Back button above all existing images/labels.
        self.back_btn.lift()

    def add_data(self):


    # ===== CHECK DUPLICATE ENTRY =====
        for row in self.student_table.get_children():
            values = self.student_table.item(row, "values")

    # Compare important fields (you can customize)
            if (
                values[0] == self.var_dep.get() and
                values[1] == self.var_course.get() and
                values[2] == self.var_year.get() and
                values[3] == self.var_sem.get() and
                values[4] == self.var_id.get() and
                values[5] == self.var_name.get() and
                values[6] == self.var_roll.get()):
                messagebox.showerror("Error", "Details already exist")
                return
        
            if values[4] == self.var_id.get():
                messagebox.showerror("Error", "Student ID already exists")
                return
        

    # ===== EMPTY FIELD CHECK =====
        if (
            self.var_dep.get() == "Select Department" or
            self.var_year.get() == "Select Year" or
            self.var_sem.get() == "Select Semester" or
            self.var_course.get() == "Select Course" or
            self.var_id.get() == "" or
            self.var_name.get() == "" or
            self.var_div.get() == "" or
            self.var_roll.get() == "" or
            self.var_dob.get() == "" or
            self.var_email.get() == "" or
            self.var_phone.get() == "" or
            self.var_address.get() == "" or
            self.var_parent.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            return

    # ===== PHONE VALIDATION =====
        import re
        if not re.fullmatch(r"\d{10}", self.var_phone.get()):
            messagebox.showerror("Error", "Phone number must be exactly 10 digits", parent=self.root)
            return
        
    # ===== CLASS DIVISION VALIDATION =====

        if not re.fullmatch(r"[A-Za-z0-9]+", self.var_div.get()):
            messagebox.showerror("Error", "Class Division must contain only letters and numbers", parent=self.root)
            return
        
        # ===== PARENT PHONE VALIDATION =====

        if not re.fullmatch(r"\d{10}", self.var_parent.get()):
            messagebox.showerror(
                "Error",
                "Parent phone number must be exactly 10 digits",
                parent=self.root
            )
            return
        
        # ===== ENROLLMENT (STUDENT ID) VALIDATION =====
        if not re.fullmatch(r"\d{13}", self.var_id.get()):
            messagebox.showerror("Error", "Enrollment number must be exactly 13 digits", parent=self.root)
            return

        if not re.fullmatch(r"\d{10}", self.var_parent.get()):
            messagebox.showerror("Error", "Parent phone number must be exactly 10 digits", parent=self.root)
            return

    # ===== EMAIL VALIDATION =====
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
            return
        
    # 3. Roll number must be numeric
        if not self.var_roll.get().isdigit():
            messagebox.showerror("Error", "Roll number must be numeric", parent=self.root)
            return
        

    # 4. Name should contain only letters
        if not re.fullmatch(r"[A-Za-z ]+", self.var_name.get()):
            messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
            return
        
        states_list = [
            "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
            "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
            "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
            "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
            "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
            "Uttar Pradesh","Uttarakhand","West Bengal","Delhi"
        ]

        address = self.var_address.get()

# check if any state name exists in address
        if not any(state.lower() in address.lower() for state in states_list):
            messagebox.showerror(
                "Error",
                "Address must contain a valid state name",
                parent=self.root)
            return

    # ===== DOB VALIDATION =====
        from datetime import datetime
        try:
            datetime.strptime(self.var_dob.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "DOB must be in DD/MM/YYYY format", parent=self.root)
            return

    # ===== DATABASE CODE =====
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Maneesh@2006",
                database="face_detection"
        )

            my_cursor = conn.cursor()

            my_cursor.execute("""
                    INSERT INTO student (dep,year,sem,course,id,name,division,gender,roll,dob,email,phone,address,parent,photosample)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                                (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_parent.get(),
                    self.var_radio.get()
                ))

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo(
                    "Success",
                    "Student details have been added successfully",
                    parent=self.root
                )

        except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To: {str(es)}",
                    parent=self.root
                )


    # ================= FETCH DATA =================
    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Maneesh@2006",
            database="face_detection"
        )

        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student;")

        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("", END, values=i)

            conn.commit()

        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

    # ✅ Prevent error
        if not data:
            return

    # Now safe to access
        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_sem.set(data[2])
        self.var_course.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_gender.set(data[7])
        self.var_roll.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_parent.set(data[13])
        self.var_radio.set(data[14])

    #================= UPDATE FUNCTION ===============
    def update_data(self):
     if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
     else:
        try:
            Update = messagebox.askyesno(
                "Update",
                "Do you want to update this student details",
                parent=self.root
            )

            if Update > 0:
                conn=mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Maneesh@2006",
                    database="face_detection"
                )

                my_cursor=conn.cursor()

                my_cursor.execute("""
                UPDATE student SET
                dep=%s,
                year=%s,
                sem=%s,
                course=%s,
                name=%s,
                division=%s,
                gender=%s,
                roll =%s,
                dob=%s,
                email=%s,
                phone=%s,
                address=%s,
                parent=%s,
                photosample=%s
                WHERE id=%s
                """,(
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_course.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_parent.get(),
                    self.var_radio.get(),
                    self.var_id.get()
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Student details successfully updated",
                    parent=self.root
                )

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Due to: {str(es)}",
                parent=self.root
            )

          # ================= DELETE FUNCTION =================
    def _remove_student_face_samples(self, student_id):
        """Remove every training image belonging to a student ID."""
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        removed = 0
        if os.path.isdir(data_dir):
            prefix = f"user.{student_id}."
            for filename in os.listdir(data_dir):
                if filename.startswith(prefix) and filename.lower().endswith(".jpg"):
                    try:
                        os.remove(os.path.join(data_dir, filename))
                        removed += 1
                    except OSError:
                        pass
        return removed

    def _remove_student_attendance(self, student_id):
        """Remove attendance history for a student who was deleted."""
        import csv
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
        if not os.path.exists(csv_path):
            return
        try:
            with open(csv_path, "r", newline="", encoding="utf-8-sig") as f:
                rows = list(csv.reader(f))
            header = ["ID", "Name", "Roll", "Department", "Time", "Date", "Status"]
            data_rows = rows[1:] if rows and rows[0] == header else [r for r in rows if r and r[0] != "ID"]
            data_rows = [r for r in data_rows if not r or str(r[0]) != str(student_id)]
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows([header] + data_rows)
        except Exception as e:
            print("Attendance cleanup warning:", e)

    def delete_data(self):
        student_id = self.var_id.get().strip()
        if student_id == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
            return

        try:
            if not messagebox.askyesno(
                "Student Delete Page",
                "Delete this student, their face samples, and their attendance records?",
                parent=self.root
            ):
                return

            conn = mysql.connector.connect(
                host="localhost", username="root", password="Maneesh@2006", database="face_detection"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM student WHERE id=%s", (student_id,))
            deleted_db = my_cursor.rowcount
            conn.commit()
            conn.close()

            removed_samples = self._remove_student_face_samples(student_id)
            self._remove_student_attendance(student_id)

            # Immediately rebuild the active recognizer so deleted faces cannot be recognized.
            success, train_message = rebuild_face_model()

            self.fetch_data()
            self.reset_data()

            if deleted_db:
                messagebox.showinfo(
                    "Delete",
                    f"Student deleted successfully.\n\nRemoved {removed_samples} old face sample(s).\n{train_message}",
                    parent=self.root
                )
            else:
                messagebox.showwarning("Delete", "Student ID was not found in the database.", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ================= RESET FUNCTION =================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_course.set("Select Course")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_gender.set("Male")
        self.var_roll.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_parent.set("")
        self.var_radio.set("")


       # ================= GENERATE DATA SET OR TAKE PHOTO SAMPLE =========
    def generate_dataset(self):
        if self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Student ID & Name required", parent=self.root)
            return

        student_id = self.var_id.get().strip()
        old_samples = self._remove_student_face_samples(student_id)
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                return None
            x, y, w, h = faces[0]
            return img[y:y+h, x:x+w]

        cap = cv2.VideoCapture(0)
        img_id = 0
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        os.makedirs(data_dir, exist_ok=True)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            face = face_cropped(frame)
            if face is not None:
                img_id += 1
                face = cv2.resize(face, (450, 450))
                gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name = os.path.join(data_dir, f"user.{student_id}.{img_id}.jpg")
                cv2.imwrite(file_name, gray_face)
                preview = gray_face.copy()
                cv2.putText(preview, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Capturing Faces", preview)
            if cv2.waitKey(1) == 13 or img_id == 100:
                break

        cap.release()
        cv2.destroyAllWindows()

        if img_id == 0:
            messagebox.showerror("Error", "No face sample was captured. Please try again.", parent=self.root)
            return

        try:
            success, train_message = rebuild_face_model()
            if success:
                messagebox.showinfo(
                    "Success",
                    f"Dataset Created Successfully.\n\n{img_id} new samples saved.\n{old_samples} old samples replaced.\n{train_message}",
                    parent=self.root
                )
            else:
                messagebox.showwarning("Training", f"Samples saved, but model training failed:\n{train_message}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Training Error", f"Samples were saved, but the model could not be rebuilt:\n{e}", parent=self.root)


    # ===================== UPDATE PHOTO SAMPLE ====================
    def update_photo_sample(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
            return

        try:
            student_id = self.var_id.get().strip()
            old_samples = self._remove_student_face_samples(student_id)
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                if len(faces) == 0:
                    return None
                x, y, w, h = faces[0]
                return img[y:y+h, x:x+w]

            cap = cv2.VideoCapture(0)
            img_id = 0
            data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
            os.makedirs(data_dir, exist_ok=True)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                face = face_cropped(frame)
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450, 450))
                    gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_path = os.path.join(data_dir, f"user.{student_id}.{img_id}.jpg")
                    cv2.imwrite(file_path, gray_face)
                    preview = gray_face.copy()
                    cv2.putText(preview, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Updating Face Data", preview)
                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            if img_id == 0:
                messagebox.showerror("Error", "No face sample was captured. Please try again.", parent=self.root)
                return

            success, train_message = rebuild_face_model()
            if success:
                messagebox.showinfo(
                    "Success",
                    f"Photo sample updated successfully.\n\n{img_id} new samples saved.\n{old_samples} old samples replaced.\n{train_message}",
                    parent=self.root
                )
            else:
                messagebox.showwarning("Training", f"Samples saved, but model training failed:\n{train_message}", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)


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
    obj = Student(root)
    root.mainloop()
