import tkinter as tk
from tkinter import messagebox

def show_selection():
    selection = ""
    if genre_var.get() == 1:
        selection = "Lubisz filmy komediowe."
    elif genre_var.get() == 2:
        selection = "Lubisz filmy dramatyczne."
    elif genre_var.get() == 3:
        selection = "Lubisz filmy romantyczne."
    
    result_label.config(text=selection)

root = tk.Tk()
root.title("Wybór filmów")
root.geometry("300x200")

label = tk.Label(root, text="Wybierz swoje ulubione gatunki filmów:")
label.pack(pady=10)

genre_var = tk.IntVar()

comedy_radio = tk.Radiobutton(root, text="komedia", variable=genre_var, value=1, command=show_selection)
comedy_radio.pack(anchor="w")

drama_radio = tk.Radiobutton(root, text="dramat", variable=genre_var, value=2, command=show_selection)
drama_radio.pack(anchor="w")

romance_radio = tk.Radiobutton(root, text="romans", variable=genre_var, value=3, command=show_selection)
romance_radio.pack(anchor="w")

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()