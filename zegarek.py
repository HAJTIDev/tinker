import tkinter as tk
import time

window = tk.Tk()
window.configure(bg="black")

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)

clock = tk.Label(window, font="times 50", fg="white", bg="black")
clock.pack(expand=True)

tick()
window.mainloop()