import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os

class mainn:
    def __init__(self, root):
        self.root = root
        self.root.title("wprowadzanie danych do paszportu")
        self.root.geometry("680x400")
        self.root.configure(bg="#5f9ea0")

        tk.Label(root, text="numer", bg="#5f9ea0").place(x=20, y=20)
        self.numer_entry = tk.Entry(root, width=25)
        self.numer_entry.place(x=100, y=20)
        self.numer_entry.bind("<FocusOut>", self.update_images)

        tk.Label(root, text="imie", bg="#5f9ea0").place(x=20, y=60)
        tk.Entry(root, width=25).place(x=100, y=60)
        tk.Label(root, text="nazwisko", bg="#5f9ea0").place(x=20, y=100)
        tk.Entry(root, width=25).place(x=100, y=100)

        colorframe = tk.LabelFrame(self.root, text="Kolor oczu", bg="#5f9ea0")
        colorframe.place(x=20, y=140, width=180, height=100)

        color_var = tk.StringVar(value="niebieskie")
        tk.Radiobutton(colorframe, text="niebieskie", variable=color_var, value="niebieskie", bg="#5f9ea0").pack(anchor="w")
        tk.Radiobutton(colorframe, text="zielone", variable=color_var, value="zielone", bg="#5f9ea0").pack(anchor="w")
        tk.Radiobutton(colorframe, text="piwne", variable=color_var, value="piwne", bg="#5f9ea0").pack(anchor="w")

        self.imageFrame = tk.Frame(self.root, width=600, height=300, bg="#5f9ea0", padx=30, pady=0)
        self.imageFrame.place(x=220, y=20)
        self.image_label = tk.Label(self.imageFrame, height=240, padx=40, pady=10)
        self.image_label.grid(row=0, column=0, sticky="w")
        self.image2_label = tk.Label(self.imageFrame, height=240, padx=10)
        self.image2_label.grid(row=0, column=1, rowspan=2, sticky="e")

        tk.Button(root, text="zatwierdz", width=50).place(x=270, y=270)

    def update_images(self, event):
        numer = self.numer_entry.get()
        self.checkNumber(numer)

    def checkNumber(self, numer):
        if numer == "1111":
            self.image = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/111-zdjecie.jpg"))
            self.image_label.config(image=self.image)
            self.image2 = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/111-odcisk.jpg"))
            self.image2_label.config(image=self.image2)
        elif numer == "3333":
            self.image = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/333-zdjecie.jpg"))
            self.image_label.config(image=self.image)
            self.image2 = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/333-odcisk.jpg"))
            self.image2_label.config(image=self.image2)
        else:
            self.image = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/000-zdjecie.jpg"))
            self.image_label.config(image=self.image)
            self.image2 = ImageTk.PhotoImage(Image.open("c:/Users/uczen54/Desktop/tinker/nowyrok/000-odcisk.jpg"))
            self.image2_label.config(image=self.image2)

def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()

if __name__ == "__main__":
    main()