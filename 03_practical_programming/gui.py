import tkinter as tk 

clicks: int = 0

def on_click() -> None:
    global clicks 
    clicks += 1
    name = entry.get().strip()
    label.config(text=f'{name} clicked {clicks} times.')

root = tk.Tk()
root.title('Counter')

label = tk.Label(root, text='Clicked 0 times.', font=('Arial', 18))
entry = tk.Entry(root, width=20)
button = tk.Button(root, text='Click me', command=on_click)

label.pack(padx=20, pady=5)
entry.pack(padx=20, pady=5)
button.pack(padx=20, pady=5)

root.mainloop()