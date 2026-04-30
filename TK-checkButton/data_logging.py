import tkinter as tk
import datetime

log = []

def log_change():
    state = "Checked" if var.get() == 1 else "Unchecked"
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    log.append(f"{timestamp}: {state}")
    print(log[-1])

root = tk.Tk()
var = tk.IntVar()
tk.Checkbutton(root, text="Track My Clicks", variable=var, command=log_change).pack(pady=20)

root.mainloop()