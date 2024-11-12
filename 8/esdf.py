import tkinter as tk
window = tk.Tk()
def spinvalue():
    label.config(text=str(spin.get()))
spin=tk.Spinbox(window,from_=0, to= 50, width=5, command=spinvalue)
spin.pack()
label=tk.Label(window)
label.pack()
window.mainloop()