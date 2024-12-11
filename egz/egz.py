import tkinter as tk
from tkinter import ttk, messagebox

class mainn:
    def __init__(self, root):
        self.root = root
        self.root.title("Dodaj pracownika")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        left_frame = ttk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        right_frame = ttk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        label1 = ttk.Label(left_frame, text="Left Box")
        label1.pack()

        label2 = ttk.Label(right_frame, text="Right Box")
        label2.pack()

def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()

if __name__ == "__main__":
    main()