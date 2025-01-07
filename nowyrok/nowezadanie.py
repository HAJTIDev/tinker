import tkinter as tk
from tkinter import ttk, messagebox
import string
from PIL import ImageTk, Image

class mainn:
    def __init__(self, root):
        self.root = root
        self.root.title("wprowadzanie danych do paszportu")
        self.root.geometry("680x400")
        self.root.configure(bg="#B0C4DE")

        tk.Label(root, text="numer", bg="#b0c4de").place(x=20, y=20)
        tk.Entry(root, width=25).place(x=100, y=20)
        tk.Label(root, text="imie", bg="#b0c4de").place(x=20, y=60)
        tk.Entry(root, width=25).place(x=100, y=60)
        tk.Label(root, text="nazwisko", bg="#b0c4de").place(x=20, y=100)
        tk.Entry(root, width=25).place(x=100, y=100)

        colorframe = tk.LabelFrame(self.root, text="Kolor oczu", bg="#b0c4de")
        colorframe.place(x=20, y=140, width=180, height=100)

        color_var = tk.StringVar(value="niebieskie")
        tk.Radiobutton(colorframe, text="niebieskie", variable=color_var, value="niebieskie", bg="#b0c4de").pack(anchor="w")
        tk.Radiobutton(colorframe, text="zielone", variable=color_var, value="zielone", bg="#b0c4de").pack(anchor="w")
        tk.Radiobutton(colorframe, text="piwne", variable=color_var, value="piwne", bg="#b0c4de").pack(anchor="w")

        self.imageFrame = tk.Frame(
            self.root, width=600, height=300, bg="#B0C4DE", padx=10, pady=50)
        self.imageFrame.place(x=220, y=20)
        self.image = ImageTk.PhotoImage(Image.open("000-zdjecie.jpg"))
        self.label = tk.Label(self.imageFrame, image=self.image, height=240, padx=40, pady=10)
        self.label.grid(row=0, column=0, sticky="w")
        self.image2 = ImageTk.PhotoImage(Image.open("000-odcisk.jpg"))
        self.label2 = tk.Label(self.imageFrame, image=self.image2, height=240, padx=10)
        self.label2.grid(row=0, column=1, rowspan=2, sticky="e")

        tk.Button(root, text="zatwierdz").place(x=330, y=360)

def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()

if __name__ == "__main__":
    main()
