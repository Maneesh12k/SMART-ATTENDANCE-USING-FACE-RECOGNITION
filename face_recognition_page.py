from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from datetime import datetime
import pickle


class Face_Recognition_Page:

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




        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 30, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # Images
        img_top = Image.open(r"College_Images\face recognition1.webp")
        img_top = img_top.resize((750, 790), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=45, width=750, height=790)

        img_bottom = Image.open(r"College_Images\face recognition3.webp")
        img_bottom = img_bottom.resize((950, 790), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=750, y=45, width=950, height=790)

        Button(self.root, text="Start Recognition",
               command=self.face_recog,
               font=("Arial", 20, "bold"),
               bg="green", fg="white").place(x=1100, y=750, width=250, height=40)

    # ================= ATTENDANCE =================
        # Keep Back button above all existing images/labels.
        self.back_btn.lift()

    def mark_attendance(self, i, n, r, d):
        """Record the recognized student using the current PC date/time.

        One row is kept per student per day. If the student is recognized again
        on the same day, the existing row is refreshed with the latest time.
        On a new day, a new attendance row is created automatically.
        """
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attendance.csv")
        header = ["ID", "Name", "Roll", "Department", "Time", "Date", "Status"]

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d/%m/%Y")

        rows = []
        if os.path.exists(csv_path):
            try:
                with open(csv_path, "r", newline="", encoding="utf-8-sig") as f:
                    rows = list(csv.reader(f))
            except Exception:
                rows = []

        # Always keep a clean header.
        if not rows or rows[0] != header:
            data_rows = [row for row in rows if row and row[0] != "ID"]
            rows = [header] + data_rows

        updated = False
        for row in rows[1:]:
            if len(row) >= 7 and str(row[0]) == str(i) and row[5] == current_date:
                row[1] = str(n)
                row[2] = str(r)
                row[3] = str(d)
                row[4] = current_time
                row[6] = "Present"
                updated = True
                break

        if not updated:
            rows.append([str(i), str(n), str(r), str(d), current_time, current_date, "Present"])

        try:
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(rows)
        except Exception as e:
            print("Attendance CSV Error:", e)

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        if not os.path.exists("classifier.xml"):
            print("Train data first")
            return

        if not os.path.exists("labels.pkl"):
            print("labels.pkl not found")
            return

    # Load mapping
        with open("labels.pkl", "rb") as f:
            label_map = pickle.load(f)

        self.reverse_map = {v: k for k, v in label_map.items()}
        self.faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("classifier.xml")
        
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = cap.read()
            if not ret:
                break

            img = self.draw_boundary(img)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        cap.release()
        cv2.destroyAllWindows()

    def draw_boundary(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

        # 🔥 Always define first
            i = n = r = d = "Unknown"
            real_id = None

        # Predict
            label, confidence = self.clf.predict(gray[y:y+h, x:x+w])

        # Map ID
            real_id = self.reverse_map.get(label, None)

        # 🔥 Recognition condition
            if real_id is not None and confidence < 90:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Maneesh@2006",
                        database="face_detection"
                    )

                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT id,name,roll,dep FROM student WHERE id=%s",
                        (real_id,)
                    )

                    result = cursor.fetchone()

                    if result:
                         i, n, r, d = result

                    conn.close()

                except Exception as e:
                    print("DB Error:", e)

        # 🔥 Display
            if i != "Unknown":
                cv2.putText(img, f"ID: {i}", (x, y-75),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                cv2.putText(img, f"Name: {n}", (x, y-50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                cv2.putText(img, f"Roll: {r}", (x, y-25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                cv2.putText(img, f"Dept: {d}", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

                self.mark_attendance(i, n, r, d)

            else:
                cv2.putText(img, "Unknown", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)

        return img
    
        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            if not ret:
                break

            img = draw_boundary(img)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        cap.release()
        cv2.destroyAllWindows()


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


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Page(root)
    root.mainloop()
