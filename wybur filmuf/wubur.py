import tkinter as tk
from tkinter import messagebox

# Function to display selected genres
def show_selections():
    selections = []
    if comedy_var.get():
        selections.append("Lubisz filmy komediowe.")
    if drama_var.get():
        selections.append("Lubisz filmy dramatyczne.")
    if romance_var.get():
        selections.append("Lubisz filmy romantyczne.")
    
    result_label.config(text="\n".join(selections))
root = tk.Tk()
root.title("Wybór filmów")
root.geometry("300x200")
label = tk.Label(root, text="Wybierz swoje ulubione gatunki filmów.\nZaznacz wszystkie, które chciałbyś wybrać:")
label.pack(pady=10)
comedy_var = tk.BooleanVar()
drama_var = tk.BooleanVar()
romance_var = tk.BooleanVar()
comedy_check = tk.Checkbutton(root, text="komedia", variable=comedy_var, command=show_selections)
comedy_check.pack(anchor="w")

drama_check = tk.Checkbutton(root, text="dramat", variable=drama_var, command=show_selections)
drama_check.pack(anchor="w")

romance_check = tk.Checkbutton(root, text="romans", variable=romance_var, command=show_selections)
romance_check.pack(anchor="w")
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()
