import tkinter as tk

window = tk.Tk()

def buttonClicked():
    print("Clicked")
    quit()

button = tk.Button(
    window,
    text="QUIT",
    bd=10,
    fg="red",
    activeforeground="black",
    activebackground="silver",
    font="Times 18 bold",
    height=3,
    width=20,
    padx=10,
    pady=10,
    relief="groove",
    command=buttonClicked
)
button.pack()
window.mainloop()

