import tkinter as tk
window = tk.Tk()
value=tk.DoubleVar()
scale=tk.Scale(window,from_=0, to= 60,
orient=tk.VERTICAL, variable=value)
scale.pack(anchor=tk.CENTER)
def selected():
    selection="Value = "+str(value.get())
    label.config(text=selection)
    window.after(200,selected)
label=tk.Label(window)
label.pack()
selected()
window.mainloop()