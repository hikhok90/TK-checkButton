import tkinter as tk

root = tk.Tk()
var = tk.IntVar()

def update_status():
    status_label.config(text="Feature Enabled" if var.get() else "Feature Disabled")

cb = tk.Checkbutton(root, text="Extra Features", variable=var, command=update_status)
cb.pack()

status_label = tk.Label(root, text="Feature Disabled", fg="blue")
status_label.pack()

root.mainloop()