import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, bg="red", text="button 1")
b1.grid(row=0, column=0, ipadx=5, ipady=5)

b2 = tk.Button(window, bg="yellow", text="button 2")
b2.grid(row=0, column=1, ipadx=5, ipady=5)

b3 = tk.Button(window, bg="green", text="button 3")
b3.grid(row=0, column=2, ipadx=5, ipady=5)

b4 = tk.Button(window, bg="blue", text="button 4")
b4.grid(row=1, column=0, ipadx=5, ipady=5)

b5 = tk.Button(window, bg="green", text="button 5")
b5.grid(row=1, column=1, ipadx=5, ipady=5)

b6 = tk.Button(window, bg="magenta", text="button 6")
b6.grid(row=1, column=2, ipadx=5, ipady=5)

b7 = tk.Button(window, bg="silver", text="button 7")
b7.grid(row=2, column=1, ipadx=5, ipady=5)

window.mainloop()
