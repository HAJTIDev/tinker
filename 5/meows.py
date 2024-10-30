import tkinter as tk
window=tk.Tk()
label1=tk.Label(window,text="Label 1",bg="silver")
label1.place(x=0,y=20,width=50,height=35)
label2=tk.Label(window,text="Label 2",bg="red")
label2.place(x=700,y=700,width=90,height=35)
window.mainloop()