import tkinter as tk 
from tkinter import ttk, messagebox
import sqlite3
class TaskManager:
    def __init__(self,root):
        self.root=root
        self.root.title("Task Manager")
        self.root.geometry("800x600")
        self.conn=sqlite3.connect("tasks.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, status TEXT NOT NULL)")
        self.conn.commit()
        self.create_widgets()
    def create_widgets(self):
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill=tk.X)

        tk.Label(input_frame, text="Tytuł Zadania:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.title_entry.grid(row=0, column=1, pady=5)

        tk.Label(input_frame, text="Opis Zadania:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.description_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.description_entry.grid(row=1, column=1, pady=5)

        tk.Label(input_frame, text="Status:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(
            input_frame,
            textvariable=self.status_var,
            values=["Do Zrobienia", "W Trakcie", "Zakończone"],
            state="readonly",
            font=("Arial", 12)
        )
        self.status_combobox.grid(row=2, column=1, pady=5, padx=10)
        self.status_combobox.current(0)
        button_frame = tk.Frame(input_frame)
        button_frame.grid(row=3, column=1, pady=10, sticky=tk.E)
        self.add_button=tk.Button(button_frame,text="Dodaj Zadanie",command=self.add_task,width=15,bg="lightgreen",font=("Arial",12))
        self.add_button.pack(side=tk.LEFT,padx=5)
        self.update_button = tk.Button(
            button_frame, text="Aktualizuj Zadanie", 
            width=15, bg="lightblue", font=("Arial", 12), 
            state=tk.DISABLED
        )
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(
            button_frame, text="Wyczyść Pola", 
            width=15, bg="lightcoral", font=("Arial", 12)
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        list_frame = tk.Frame(self.root, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree=ttk.Treeview(list_frame,columns=("ID","Title","Description","Status"),show="headings",yscrollcommand=scrollbar.set)
        self.tree.heading("ID",text="ID")
        self.tree.heading("Title",text="Title")
        self.tree.heading("Description",text="Description")
        self.tree.heading("Status",text="Status")
        self.tree.column("ID",width=50,anchor=tk.CENTER)
        self.tree.column("Title",width=200)
        self.tree.column("Description",width=300)
        self.tree.column("Status",width=100,anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH,expand=True)
        scrollbar.config(command=self.tree.yview)
        actions_frame = tk.Frame(self.root, padx=10, pady=10)
        actions_frame.pack(fill=tk.X)
        self.delete_button = tk.Button(
            actions_frame, text="Usuń Zadanie", 
            width=15, bg="tomato", font=("Arial", 12), 
            state=tk.DISABLED
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.refresh_button = tk.Button(
            actions_frame, text="Odśwież", 
            width=15, bg="lightyellow", font=("Arial", 12)
        )
        self.refresh_button.pack(side=tk.LEFT, padx=5)
    def add_task(self):
        title=self.title_entry.get().strip()
        description=self.description_entry.get().strip()
        status=self.status_var.get()
        if not title:
            messagebox.showwarning("Błąd","Tytuł nie może być pusty")
            return
        self.cursor.execute("INSERT INTO tasks (title,description,status) VALUES (?,?,?)",(title,description,status))
        self.conn.commit()
def main():
    root=tk.Tk()
    app=TaskManager(root)
    root.mainloop()
if __name__ == "__main__":
    main()