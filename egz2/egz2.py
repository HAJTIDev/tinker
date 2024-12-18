import tkinter as tk
from tkinter import ttk

def oblicz_cene():

    if rodzaj.get() == "Pocztówka":
        cena.set("Cena: 1,0 zł")
    elif rodzaj.get() == "List":
        cena.set("Cena: 1,5 zł")
    elif rodzaj.get() == "Paczka":
        cena.set("Cena: 10,0 zł")
root = tk.Tk()
root.title("Nadaj Przesyłkę")
root.geometry("500x300")
root.resizable(False, False)
rodzaj = tk.StringVar(value="List")
cena = tk.StringVar(value="Cena: 1,5 zł")

frame1 = tk.LabelFrame(root, text="Rodzaj przesyłki", padx=10, pady=10)
frame1.place(x=20, y=20, width=150, height=130)

tk.Radiobutton(frame1, text="Pocztówka", variable=rodzaj, value="Pocztówka", command=oblicz_cene).pack(anchor="w")
tk.Radiobutton(frame1, text="List", variable=rodzaj, value="List", command=oblicz_cene).pack(anchor="w")
tk.Radiobutton(frame1, text="Paczka", variable=rodzaj, value="Paczka", command=oblicz_cene).pack(anchor="w")
btn_cena = tk.Button(root, text="Sprawdź Cenę", command=oblicz_cene)
btn_cena.place(x=30, y=160, width=120, height=25)
canvas = tk.Canvas(root, width=80, height=50)
canvas.create_rectangle(5, 5, 75, 45, fill="grey", outline="black")
canvas.place(x=20, y=200)
label_cena = tk.Label(root, textvariable=cena, font=("Arial", 10, "bold"))
label_cena.place(x=120, y=220)
frame2 = tk.LabelFrame(root, text="Dane adresowe", padx=10, pady=10)
frame2.place(x=200, y=20, width=270, height=180)

tk.Label(frame2, text="Ulica z numerem").grid(row=0, column=0, sticky="w")
entry_ulica = tk.Entry(frame2, width=25)
entry_ulica.insert(0, "")
entry_ulica.grid(row=0, column=1)

tk.Label(frame2, text="Kod pocztowy").grid(row=1, column=0, sticky="w")
entry_kod = tk.Entry(frame2, width=25)
entry_kod.insert(0, "")
entry_kod.grid(row=1, column=1)

tk.Label(frame2, text="Miasto").grid(row=2, column=0, sticky="w")
entry_miasto = tk.Entry(frame2, width=25)
entry_miasto.grid(row=2, column=1)

btn_zatwierdz = tk.Button(root, text="Zatwierdź", font=("Arial", 10))
btn_zatwierdz.place(x=200, y=220, width=270, height=30)
root.mainloop()