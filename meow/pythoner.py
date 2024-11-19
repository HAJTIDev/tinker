import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        master.title("Password Generator")
        master.geometry("500x350")
        master.resizable(False, False)
        
        self.main_frame = ttk.Frame(master, padding="20 20 10 20")
        self.main_frame.pack(fill=tk.BOTH, expand=False)
        
        self.options_frame = ttk.LabelFrame(self.main_frame, text="Character Options", padding="10 10 10 10")
        self.options_frame.pack(fill="x", expand=True, pady=10)
        
        self.include_letters = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        
        self.letters_check = ttk.Checkbutton(
            self.options_frame,
            text="Letters (a-z), (A-Z)",
            variable=self.include_letters,
        )
        self.letters_check.grid(row=0, column=0, sticky="w", pady=5)
        
        self.digits_check = ttk.Checkbutton(
            self.options_frame,
            text="Numbers (0-9)",
            variable=self.include_numbers,
        )
        self.digits_check.grid(row=1, column=0, sticky="w", pady=5)
        
        self.special_check = ttk.Checkbutton(
            self.options_frame,
            text="Special Characters",
            variable=self.include_special,
        )
        self.special_check.grid(row=2, column=0, sticky="w", pady=5)
        
        self.length_frame = ttk.Frame(self.main_frame)
        self.length_frame.pack(fill="x", expand=True, pady=10)
        
        self.length_label = ttk.Label(self.length_frame, text="Password Length:")
        self.length_label.pack(side="left", padx=(0, 10))
        
        self.length_var = tk.IntVar(value=8)
        self.length_spinbox = ttk.Spinbox(
            self.length_frame,
            from_=4,
            to=64,
            textvariable=self.length_var,
            width=5,
        )
        self.length_spinbox.pack(side="left")
        
        self.generate_button = ttk.Button(
            self.main_frame,
            text="Generate Password",
            command=self.generate_password,
        )
        self.generate_button.pack(pady=10)
        
        self.password_frame = ttk.Frame(self.main_frame)
        self.password_frame.pack(fill="x", expand=True, pady=10)
        
        self.password_label = ttk.Label(self.password_frame, text="Password:")
        self.password_label.pack(side="left", padx=(0, 10))
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            self.password_frame,
            width=30,
            state="readonly"
        )
        self.password_entry.pack(side="left")
    
    def generate_password(self):
        characters = ""
        
        if self.include_letters.get():
            characters += string.ascii_letters
        
        if self.include_numbers.get():
            characters += string.digits
        
        if self.include_special.get():
            characters += string.punctuation
        
        length = self.length_var.get()
        
        password = "".join(random.choice(characters) for _ in range(length))
        
        self.password_var.set(password)
        self.password_entry.configure(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.configure(state="readonly")

root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()
