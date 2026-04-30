import tkinter as tk

root = tk.Tk()
for r in range(3):
    for c in range(3):
        tk.Checkbutton(root, text=f"R{r} C{c}").grid(row=r, column=c, padx=5, pady=5)

root.mainloop()