import tkinter as tk

root = tk.Tk()
root.title("My Desktop GUI")
root.geometry("400x300")
root.configure(bg="#282c34")

label = tk.Label(root, text="Hello from tkinter!", fg="#ffffff", bg="#282c34", font=("Segoe UI", 18))
label.pack(pady=40)

button = tk.Button(root, text="Click me", font=("Segoe UI", 14), command=lambda: label.config(text="You clicked the button!"))
button.pack(pady=20)

root.mainloop()
