import tkinter as tk

root = tk.Tk()
tk.Checkbutton(
    root, 
    text="Custom Colors", 
    selectcolor="yellow",   # Color of the check mark box
    fg="red",               # Text color
    activebackground="gray" # Background when clicking
).pack(pady=20)

root.mainloop()