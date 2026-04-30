import tkinter as tk

def select_all():
    state = master_var.get()
    for var in checkbox_vars:
        var.set(state)

root = tk.Tk()
master_var = tk.IntVar()
tk.Checkbutton(root, text="Select All", variable=master_var, command=select_all, font=('Arial', 10, 'bold')).pack()

checkbox_vars = []
for i in range(3):
    v = tk.IntVar()
    checkbox_vars.append(v)
    tk.Checkbutton(root, text=f"Option {i+1}", variable=v).pack()

root.mainloop()