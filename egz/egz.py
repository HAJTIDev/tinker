import tkinter as tk
from tkinter import ttk, messagebox

class mainn:
    def __init__(self, root):
        self.root = root
        self.root.title("Dodaj pracownika")
        self.root.geometry("643x400")
        self.root.configure(bg="#B0C4DE")

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
        tk.Checkbutton(frame_right,text="Małe i wielkie litery",bg="#B0C4DE").grid(row=1,column=0,sticky="w",pady=5)
        tk.Checkbutton(frame_right,text="cyfry",bg="#B0C4DE").grid(row=2,column=0,sticky="w",pady=5)
        tk.Checkbutton(frame_right,text="znaki specjalne",bg="#B0C4DE").grid(row=3,column=0,sticky="w",pady=5)
        tk.Button(frame_right,text="Generuj",bg="#4682B4").grid(row=4,column=0,columnspan=2,pady=5)
        
        tk.Button(root,text="Zatwierdz",width=20,bg="#4682B4").place(x=233,y=240)
        

def main():
    root = tk.Tk()
    app = mainn(root)
    root.mainloop()

if __name__ == "__main__":
    main()
