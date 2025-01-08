import tkinter as tk
from tkinter import ttk,messagebox
import random
import string
class mainn:
    def __init__(self,root):
        self.root=root
        self.root.title("Muzyka")
        self.root.geometry("700x400")
        self.root.configure(bg="#2E8B57")
       
        image_frame = tk.Frame(self.root, bg="#2E8B57")
        image_frame.pack(side=tk.TOP, pady=10)

        image1 = tk.PhotoImage(file="obraz3.png")
        image2 = tk.PhotoImage(file="obraz2.png")

        label1 = tk.Label(image_frame, image=image1)
        label1.pack(side=tk.LEFT, padx=10)
        label2 = tk.Label(image_frame, image=image2)
        label2.pack(side=tk.RIGHT, padx=10)
def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()
if __name__ == "__main__":
    main()