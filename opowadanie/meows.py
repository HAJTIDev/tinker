import tkinter as tk
from tkinter import ttk
def generate_story():
    person = entry_person.get()
    noun_plural = entry_noun_plural.get()
    verb = entry_verb.get()
    adjective = adjective_var.get()
    body_part = body_part_var.get()
    
    story = f"Sławny badacz i odkrywca {person} o mało co nie zrezygnował z ryzykownej wyprawy "\
            f"w poszukiwaniu zagubionego miasta, które zamieszkiwały mityczne {noun_plural}. "\
            f"Silny, {adjective} wiatr uderzał we wszystko na swojej drodze, "\
            f"ale {person} nie przestawał {verb}. Nagle, pojawiła się {body_part}, która stanęła "\
            f"na jego drodze. Wtedy {noun_plural} szybko porwały {person}. "\
            f"Jaki morał płynie z tego opowiadania? "\
            f"Zawsze miej przy sobie trochę zapasowego jedzenia i zapasowy pomysł, zanim zaczniesz coś szukać."
    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, story)

root = tk.Tk()
root.title("Mad Lib")
root.geometry("600x400")

label_person = ttk.Label(root, text="Osoba:")
label_person.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_person = ttk.Entry(root, width=30)
entry_person.grid(row=0, column=1, padx=10, pady=5)

label_noun_plural = ttk.Label(root, text="Rzeczownik w liczbie mnogiej:")
label_noun_plural.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_noun_plural = ttk.Entry(root, width=30)
entry_noun_plural.grid(row=1, column=1, padx=10, pady=5)

label_verb = ttk.Label(root, text="Czasownik:")
label_verb.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
entry_verb = ttk.Entry(root, width=30)
entry_verb.grid(row=2, column=1, padx=10, pady=5)

adjective_var = tk.StringVar()
adjective_var.set("nagłe")

label_adjective = ttk.Label(root, text="Przymiotnik:")
label_adjective.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
check_sudden = ttk.Checkbutton(root, text="nagłe", variable=adjective_var, onvalue="nagłe", offvalue="")
check_sudden.grid(row=3, column=1, sticky=tk.W)
check_happy = ttk.Checkbutton(root, text="radosne", variable=adjective_var, onvalue="radosne", offvalue="")
check_happy.grid(row=3, column=2, sticky=tk.W)
check_exciting = ttk.Checkbutton(root, text="ekscytujące", variable=adjective_var, onvalue="ekscytujące", offvalue="")
check_exciting.grid(row=3, column=3, sticky=tk.W)

body_part_var = tk.StringVar()
body_part_var.set("pępek")

label_body_part = ttk.Label(root, text="Część ciała:")
label_body_part.grid(row=4, column=0, sticky=tk.W, padx=10)
body_part_menu = ttk.Radiobutton(root, text="pępek", variable=body_part_var, value="pępek")
body_part_menu.grid(row=4, column=1, padx=10,sticky=tk.W)
body_part_menu = ttk.Radiobutton(root, text="duży palec u nogi", variable=body_part_var, value="duży palec u nogi")
body_part_menu.grid(row=4, column=2, padx=10,sticky=tk.W)
body_part_menu = ttk.Radiobutton(root, text="rzeźń przedutony", variable=body_part_var, value="rzeźń przedutony")
body_part_menu.grid(row=4, column=3, padx=10, sticky=tk.W)
generate_button = ttk.Button(root, text="Kliknij, aby wyświetlić opowiadanie", command=generate_story)
generate_button.grid(row=5, column=0, columnspan=5)
output_text = tk.Text(root, width=70, height=10, wrap=tk.WORD)
output_text.grid(row=6, column=0, columnspan=5, padx=10, sticky=tk.W)
root.mainloop()
