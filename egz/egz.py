import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class mainn:
    def __init__(self, root):
        self.root = root
        self.root.title("Dodaj pracownika")
        self.root.geometry("643x400")
        self.root.configure(bg="#B0C4DE")
        self.include_letters= tk.BooleanVar(value=True)
        self.include_digits= tk.BooleanVar(value=True)
        self.include_special= tk.BooleanVar(value=True)

        frame_left=tk.LabelFrame(self.root,text="Dodaj Pracownika", bg="#B0C4DE")
        frame_left.place(x=10,y=10,width=260,height=200)
        
        tk.Label(frame_left,text="imie",bg="#B0C4DE").grid(row=0,column=0,sticky="w",pady=5)
        tk.Entry(frame_left).grid(row=0,column=1,pady=5)
        tk.Label(frame_left,text="nazwisko",bg="#B0C4DE").grid(row=1,column=0,sticky="w",pady=5)
        tk.Entry(frame_left).grid(row=1,column=1,pady=5)
        tk.Label(frame_left,text="Stanowisko",bg="#B0C4DE").grid(row=2,column=0,sticky="w",pady=5)
        ttk.Combobox(frame_left,values=["Kierownik","Starszy Programista","Młodszy Programista","Tester"]).grid(row=2,column=1,pady=5)
        
        frame_right=tk.LabelFrame(self.root,text="Generowanie hasła", bg="#B0C4DE")
        frame_right.place(x=350,y=10,width=280,height=200)
        
        tk.Label(frame_right,text="Ile znaków",bg="#B0C4DE").grid(row=0,column=0,sticky="w",pady=5)
        tk.Entry(frame_right).grid(row=0,column=1,pady=5)
        tk.Checkbutton(frame_right,text="Małe i wielkie litery",bg="#B0C4DE",variable=self.include_letters).grid(row=1,column=0,sticky="w",pady=5)
        tk.Checkbutton(frame_right,text="cyfry",bg="#B0C4DE",variable=self.include_digits).grid(row=2,column=0,sticky="w",pady=5)
        tk.Checkbutton(frame_right,text="znaki specjalne",bg="#B0C4DE",variable=self.include_special).grid(row=3,column=0,sticky="w",pady=5)
        tk.Button(frame_right,text="Generuj",bg="#4682B4").grid(row=4,column=0,columnspan=2,pady=5)
        
        tk.Button(root,text="Zatwierdz",width=20,bg="#4682B4").place(x=233,y=240)
        
    def generatepass(self):
        rangeOfNum = self.length_var.get()
        if self.include_letters.get() == False and self.include_digits.get() == False and self.include_special.get() == False:
            messagebox.showerror("ERROR","Nie można wygenerować bez niczego")
        elif self.length_var.get()<1:
            messagebox.showerror("ERROR","Nie można wygenerować hasła z jedną literą")
        else:
            self.password_entry.delete(0, tk.END)
            temp = ""
            allChars =""
            if self.include_letters.get():
                allChars+= string.ascii_letters
            if self.include_digits.get():
                allChars+=string.digits
            if self.include_special.get():
                allChars+=string.punctuation
            for _ in range(rangeOfNum):
                temp+=random.choice(allChars)
            self.password_var.set(temp)
           
        
def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()

if __name__ == "__main__":
    main()
