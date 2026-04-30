import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
frame = tk.Frame(canvas)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0,0), window=frame, anchor="nw")

for i in range(30):
    tk.Checkbutton(frame, text=f"Item {i}").pack(anchor="w")

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()