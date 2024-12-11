import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class TaskMenager:
    def __init__(self, root):
        self.root = root
        self.root.title("Menedżer Zadań")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
        """)
        self.conn.commit()
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, padx=10, pady=10)
        input_frame.pack(fill=tk.X)
        tk.Label(input_frame, text="Tytył Zadania:", font=(
            "Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.title_enter = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.title_enter.grid(row=0, column=1, pady=5, padx=10)
        tk.Label(input_frame, text="Opis Zadania:", font=("Arial", 12)).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        self.description_entry = tk.Entry(
            input_frame, width=50, font=("Arial", 12))
        self.description_entry.grid(row=1, column=1, pady=5)

        tk.Label(input_frame, text="Status:", font=("Arial", 12)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
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
        button_frame.grid(row=3, column=1, pady=5, padx=10)
        self.add_button = tk.Button(button_frame, text="Dodaj Zadanie",
                                    command=self.add_task, width=15, bg="lightgreen", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.update_button = tk.Button(button_frame, text="Aktualizuj Zadanie",
                                       width=15, bg="lightblue", font=("Arial", 12), state=tk.DISABLED, command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5,)
        self.clear_button = tk.Button(
            button_frame, text="Wyczyść Pola", width=15, bg="lightcoral", font=("Arial", 12))
        self.clear_button.pack(side=tk.LEFT, padx=5)
        list_frame = tk.Frame(self.root, padx=10, pady=10)
        list_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(list_frame, columns=(
            "ID", "Title", "Description", "Status"), show="headings", yscrollcommand=scrollbar.set)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Tytuł Zadania")
        self.tree.heading("Description", text="Opis Zadania")
        self.tree.heading("Status", text="Status")
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Title", width=200)
        self.tree.column("Description", width=300)
        self.tree.column("Status", width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)
        action_frame = tk.Frame(self.root, padx=10, pady=10)
        action_frame.pack(fill=tk.X)
        self.delete_button = tk.Button( 
            action_frame, text="Usuń zadanie", width=15, bg="tomato", font=("Arial", 12),command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.refresh_button = tk.Button(
            action_frame, text="Odśwież Listę", width=15, bg="lightyellow", font=("Arial", 12), command=self.view_task)
        self.refresh_button.pack(side=tk.LEFT, padx=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.view_task()
    def delete_task(self):
        selected_item=self.free.focus()
        if not selected_item:
            messagebox.showerror("Błąd","Proszę wybrać zadanie")
            return
        values=self.tree.item(selected_item,"values")
        task_id=values[0]
        confirm=messagebox.askyesno("Potwierdzenie","Czy na pewno chcesz usunąć zadanie?")
        if confirm:
            self.cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
            self.conn.commit()
            self.view_task()
    def clear_fields(self):
        self.title_enter.delete(0,tk.END)
        self.description_entry.delete(0,tk.END)
        self.status_combobox.current(0)
        self.update_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)
    def __del__(self):
        self.conn.close()       
    def update_task(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Błąd", "Proszę wybrać zadanie")
            return
            values=self.tree.item(selected_item,"values")
            task_id=values[0]
            title=self.title_enter.get().strip()
            description=self.description_entry.get().strip()
            status=self.status_var.get()
            if not title:
                messagebox.showerror("Brak tytułu","Proszę wprowadzić tytuł zadania")
                return
            self.cursor.execute("UPDATE tasks SET title=?,description=?,status=? WHERE id=?",(title,description,status,task_id))
            self.conn.commit()
            self.view_task()
    def add_task(self):
        title = self.title_enter.get().strip()
        description = self.description_entry.get().strip()
        status = self.status_var.get()
        if not title:
            messagebox.showerror(
                "Brak tytułu", "Proszę wprowadzic tytuł zadania")
            return
        self.tree.insert("", "end")
        self.cursor.execute(
            "INSERT INTO tasks (title,description,status) VALUES(?,?,?)", (title, description, status))
        self.conn.commit()
        self.view_task()

    def view_task(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.cursor.execute("SELECT * from tasks")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)
        self.update_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)

    def on_tree_select(self, event):
        self.update_button.config(state=tk.NORMAL)
        self.delete_button.config(state=tk.NORMAL)
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")
        self.selected_id = values[0]
        self.title_enter.delete(0, tk.END)
        self.title_enter.insert(0, values[1])
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, values[2])
        self.status_var.set(values[3])
def main():
    root = tk.Tk()
    app = TaskMenager(root)

    root.mainloop()


if __name__ == "__main__":
    main()
