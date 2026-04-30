import tkinter as tk

root = tk.Tk()
var = tk.IntVar()
# If the value is 2, it will show the 'tristate' look (usually a dash or square)
var.set(2) 

tk.Checkbutton(root, text="Partial Selection", variable=var, tristatevalue=2).pack()

root.mainloop()