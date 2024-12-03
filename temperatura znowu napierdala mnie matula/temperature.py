import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")
        master.geometry("400x300")
        master.resizable(False, False)
        
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
        
        self.ctoftab = ttk.Frame(self.notebook)
        self.ftoctab = ttk.Frame(self.notebook)
        self.ctoktab = ttk.Frame(self.notebook)
        self.ktoctab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.ctoftab, text="Celsius to Fahrenheit")
        self.notebook.add(self.ftoctab, text="Fahrenheit to Celsius")
        self.notebook.add(self.ctoktab, text="Celsius to Kelvin")
        self.notebook.add(self.ktoctab, text="Kelvin to Celsius")
        
        self.create_ctof_tab()
        self.create_ftoc_tab()
        self.create_ctok_tab()
        self.create_ktoc_tab()

    def create_ctof_tab(self):
        self.celsius_label = ttk.Label(self.ctoftab, text="Celsius:")
        self.celsius_label.pack(pady=10)
        self.celsius_entry = ttk.Entry(self.ctoftab, width=20)
        self.celsius_entry.pack(pady=5)
        self.ctof_button = ttk.Button(self.ctoftab, text="Convert", command=self.convert_ctof)
        self.ctof_button.pack(pady=10)
        self.ctof_result = ttk.Label(self.ctoftab, text="Wynik:")
        self.ctof_result.pack(pady=10)

    def create_ftoc_tab(self):
        self.fahrenheit_label = ttk.Label(self.ftoctab, text="Fahrenheit:")
        self.fahrenheit_label.pack(pady=10)
        self.fahrenheit_entry = ttk.Entry(self.ftoctab, width=20)
        self.fahrenheit_entry.pack(pady=5)
        self.ftoc_button = ttk.Button(self.ftoctab, text="Convert", command=self.convert_ftoc)
        self.ftoc_button.pack(pady=10)
        self.ftoc_result = ttk.Label(self.ftoctab, text="Wynik:")
        self.ftoc_result.pack(pady=10)

    def create_ctok_tab(self):
        self.kelvin_label = ttk.Label(self.ctoktab, text="Kelvin:")
        self.kelvin_label.pack(pady=10)
        self.kelvin_entry = ttk.Entry(self.ctoktab, width=20)
        self.kelvin_entry.pack(pady=5)
        self.ctok_button = ttk.Button(self.ctoktab, text="Convert", command=self.convert_ctok)
        self.ctok_button.pack(pady=10)
        self.ctok_result = ttk.Label(self.ctoktab, text="Wynik:")
        self.ctok_result.pack(pady=10)

    def create_ktoc_tab(self):
        self.celsius_label = ttk.Label(self.ktoctab, text="Celsius:")
        self.celsius_label.pack(pady=10)
        self.celsius_entry = ttk.Entry(self.ktoctab, width=20)
        self.celsius_entry.pack(pady=5)
        self.ktoc_button = ttk.Button(self.ktoctab, text="Convert", command=self.convert_ktoc)
        self.ktoc_button.pack(pady=10)
        self.ktoc_result = ttk.Label(self.ktoctab, text="Wynik:")
        self.ktoc_result.pack(pady=10)

    def convert_ktoc(self):
        try:
            kelvin = float(self.kelvin_entry.get())
            celsius = kelvin - 273.15
            celsius = round(celsius, 2)
            self.ktoc_result.config(text=f"Wynik: {celsius}°C")
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną wartość")

    def convert_ctok(self):
        try:
            celsius = float(self.celsius_entry.get())
            kelvin = celsius + 273.15
            kelvin = round(kelvin, 2)
            self.ctok_result.config(text=f"Wynik: {kelvin}K")
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną wartość")

    def convert_ctof(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit = round(fahrenheit, 2)
            self.ctof_result.config(text=f"Wynik: {fahrenheit}°F")
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną wartość")

    def convert_ftoc(self):
        try:
            fahrenheit = float(self.fahrenheit_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            celsius = round(celsius, 2)
            self.ftoc_result.config(text=f"Wynik: {celsius}°C")
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną wartość")

def main():
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()