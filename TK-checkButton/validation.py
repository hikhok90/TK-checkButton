import tkinter as tk

root = tk.Tk()
agree_var = tk.IntVar()

def toggle_btn():
    if agree_var.get() == 1:
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

tk.Checkbutton(root, text="I agree to the Terms", variable=agree_var, command=toggle_btn).pack()
submit_btn = tk.Button(root, text="Continue", state="disabled")
submit_btn.pack()

root.mainloop()