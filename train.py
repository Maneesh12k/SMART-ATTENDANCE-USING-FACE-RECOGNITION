from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLASSIFIER_PATH = os.path.join(BASE_DIR, "classifier.xml")
LABELS_PATH = os.path.join(BASE_DIR, "labels.pkl")


def rebuild_face_model(data_dir=DATA_DIR, classifier_path=CLASSIFIER_PATH, labels_path=LABELS_PATH):
    """Rebuild the LBPH face model from the current photo samples.

    This is intentionally shared by Student add/delete/photo-update and the
    Train Data screen so the recognizer never keeps deleted/stale samples.
    Returns (success, message).
    """
    faces = []
    ids = []
    label_map = {}

    if not os.path.isdir(data_dir):
        for path in (classifier_path, labels_path):
            try:
                os.remove(path)
            except FileNotFoundError:
                pass
        return False, "No face samples found. Add a photo sample first."

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Sort files so rebuilding the model is deterministic.
    files = sorted(f for f in os.listdir(data_dir) if f.lower().endswith(".jpg"))
    for file in files:
        parts = file.split('.')
        if len(parts) < 3 or parts[0] != 'user':
            continue
        real_id = parts[1]
        path = os.path.join(data_dir, file)
        try:
            img = Image.open(path).convert('L')
            img_np = np.array(img, 'uint8')
        except Exception:
            continue

        detected = face_cascade.detectMultiScale(img_np, 1.3, 5)
        if len(detected) == 0:
            continue

        if real_id not in label_map:
            label_map[real_id] = len(label_map)
        numeric_id = label_map[real_id]

        for (x, y, w, h) in detected:
            faces.append(img_np[y:y+h, x:x+w])
            ids.append(numeric_id)

    if not faces:
        for path in (classifier_path, labels_path):
            try:
                os.remove(path)
            except FileNotFoundError:
                pass
        return False, "No valid face samples found to train the model."

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, np.array(ids))
    clf.write(classifier_path)

    with open(labels_path, "wb") as f:
        pickle.dump(label_map, f)

    return True, f"Training completed for {len(label_map)} student(s)."


class Train:

    def __init__(self, root, back_command=None):
        self.root = root
        self.back_command = back_command
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

        self.root.geometry("1920x1080+0+0")


        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"),
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # ===== TOP IMAGES =====
        img_top = Image.open(r"College_Images\train 1.png")
        img_top = img_top.resize((500, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=500, height=325)

        img_top1 = Image.open(r"College_Images\train2.jpg")
        img_top1 = img_top1.resize((500, 325), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        Label(self.root, image=self.photoimg_top1).place(x=500, y=55, width=500, height=325)

        img_top2 = Image.open(r"College_Images\train3.jpg")
        img_top2 = img_top2.resize((550, 325), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        Label(self.root, image=self.photoimg_top2).place(x=1000, y=55, width=550, height=325)


        #===========button============
        Button(self.root, text="TRAIN DATA",
               command=self.train_classifier,
               font=("Arial", 20, "bold"),
               bg="red", fg="white").place(x=0, y=380, width=1530, height=120)
        

         # ===== BOTTOM IMAGE =====
        img_bottom = Image.open(r"College_Images\photo.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=500, width=1530, height=325)

        # Keep Back button above all existing images/labels.
        self.back_btn.lift()

    def train_classifier(self):
        try:
            success, message = rebuild_face_model()
            if success:
                messagebox.showinfo("Success", message + "\nThe latest photo samples are now active.")
            else:
                messagebox.showerror("Training", message)
        except Exception as e:
            messagebox.showerror("Training Error", f"Unable to train the model: {e}")


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
    obj = Train(root)
    root.mainloop()
