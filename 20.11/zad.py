import tkinter as tk
from tkinter import filedialog,messagebox
import os
def open_file():
    file_path=filedialog.askopenfilename(
    defaultextension=".txt",
    filetypes=[("All Files","*.*"),("Text Documents","*.txt")],
    title="Otwórz plik"
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content=file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
            root.title(f"Notatnik -{os.path.basename(file_path)}")
    else:
        messagebox.showerror("Błąd", f"Nie można otworzyć pliku: {e}")
        return

root=tk.Tk()
root.title("Notatnik")
root.geometry("800x600")
text_area=tk.Text(root, wrap=tk.WORD, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)
scrollbar=tk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)
menu_bar=tk.Menu(root)
file_menu=tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Otwórz", command=open_file)
file_menu.add_command(label="Zapisz")
file_menu.add_command(label="Zapisz jako")
file_menu.add_separator()
file_menu.add_command(label="Zakończ")
file_menu.add_separator()
file_menu.add_command(label="Wyjdz", command=root.quit)
menu_bar.add_cascade(label="Plik", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()