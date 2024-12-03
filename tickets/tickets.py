import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class TicketReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticket Reservation System")
        self.root.geometry("800x600")
        self.dataFile = 'reservation.json'
        self.tree = ttk.Treeview(root, columns=(
            "Imię", "Nazwisko", "numer Telefonu", "liczba biletów"), show='headings')
        self.tree.heading("Imię", text="Imię")
        self.tree.heading("Nazwisko", text="Nazwisko")
        self.tree.heading("numer Telefonu", text="numer Telefonu")
        self.tree.heading("liczba biletów", text="liczba biletów")
        self.tree.pack(pady=20, fill="both", expand=True)
        self.load_data()
        self.addbutton = tk.Button(root, text="Dodaj rezerwacje")
        self.addbutton.pack(side="left", padx=10, pady=10)
        self.delete_button = tk.Button(root, text="Usunć rezerwacje")
        self.delete_button.pack(side="left", padx=10, pady=10)

    def load_data(self):
        if os.path.exists(self.dataFile):
            with open(self.dataFile, 'r') as file:
                data = json.load(file)
                for reservation in data:
                    self.tree.insert("", "end", values=(
                        reservation["Imię"], reservation["Nazwisko"], reservation["numer Telefonu"], reservation["liczba biletów"]))

    def save_data(self):
        with open(self.dataFile, 'w') as file:
            json.dump(self.tree.get_children(), file)
    def add_reservation(self):
        def save_new_reservation():
            first_name=first_name_entry.get()
            last_name=last_name_entry.get()
            phone_number=phone_number_entry.get()
            tickets=ticket_number_entry.get()
            if not first_name or not last_name or not phone_number or not tickets:
                messagebox.showerror("Błąd", "Wszystkie pola są wymagane")
                return
            new_reservation = {
                "Imię": first_name,
                "Nazwisko": last_name,
                "numer Telefonu": phone_number,
                "liczba biletów": tickets
            }
            self.tree.insert('', tk.END, values=(first_name, last_name, phone_number, tickets))
            reservations = []
            if os.path.exists(self.dataFile):
                with open(self.dataFile, 'r') as file:
                    reservations = json.load(file)
            reservations.append(new_reservation)
            self.save_data(reservations)
            add_window.destroy()
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj rezerwacje")
        add_window.geometry("300x250")
        tk.Label(add_window, text="Imię").pack()
        first_name_entry = tk.Entry(add_window)
        first_name_entry.pack()
        tk.Label(add_window, text="Nazwisko").pack()
        last_name_entry = tk.Entry(add_window)
        last_name_entry.pack()
        tk.Label(add_window, text="Numer telefonu").pack()
        phone_number_entry = tk.Entry(add_window)
        phone_number_entry.pack()
        tk.Label(add_window, text="Liczba biletów").pack()
        ticket_number_entry = tk.Entry(add_window)
        ticket_number_entry.pack()
        save_button = tk.Button(add_window, text="Zapisz", command=save_new_reservation)
    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Błąd", "Nie wybrano rezerwacji do usunięcia")
            return
        for item in selected:
            self.tree.delete(item)
        self.save_data()
        if os.path.exists(self.dataFile):
            with open(self.dataFile, 'r') as file:
                data = json.load(file)
                for reservation in data:
                    self.tree.insert("", "end", values=(
                        reservation["Imię"], reservation["Nazwisko"], reservation["numer Telefonu"], reservation["liczba biletów"]))
def main():
    root = tk.Tk()
    app = TicketReservationSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
