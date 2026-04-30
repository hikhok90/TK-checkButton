import tkinter as tk

root = tk.Tk()
var = tk.IntVar(value=1) # Setting value=1 makes it checked immediately

tk.Checkbutton(root, text="Email Notifications (Default On)", variable=var).pack(pady=10)

root.mainloop()