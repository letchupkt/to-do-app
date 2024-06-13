import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to remove '{task}'?")
        if confirmation:
            listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("No Task Selected", "Please select a task to remove.")

def clear_tasks():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirmation:
        listbox.delete(0, tk.END)

def on_hover(event):
    add_button.config(bg="#5DBCD2")

def on_leave(event):
    add_button.config(bg="#4FA8B8")

root = tk.Tk()
root.title("To-Do List by letchu_pkt")

canvas = tk.Canvas(root, width=400, height=400, bg="#4FA8B8", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Add a gradient background
for i in range(400):
    r = int(190 - (190 * i) / 400)
    g = int(220 - (220 * i) / 400)
    b = int(230 - (230 * i) / 400)
    color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    canvas.create_line(0, i, 400, i, fill=color)

entry = tk.Entry(root, font=('Helvetica', 18))
entry.place(relx=0.05, rely=0.05, relwidth=0.65, relheight=0.1)

add_button = tk.Button(root, text="Add", font=('Helvetica', 14), command=add_task)
add_button.place(relx=0.72, rely=0.05, relwidth=0.15, relheight=0.1)
add_button.bind("<Enter>", on_hover)
add_button.bind("<Leave>", on_leave)

remove_button = tk.Button(root, text="Remove", font=('Helvetica', 14), command=remove_task)
remove_button.place(relx=0.05, rely=0.18, relwidth=0.3, relheight=0.1)

clear_button = tk.Button(root, text="Clear All", font=('Helvetica', 14), command=clear_tasks)
clear_button.place(relx=0.35, rely=0.18, relwidth=0.3, relheight=0.1)

listbox = tk.Listbox(root, font=('Helvetica', 18), selectmode=tk.SINGLE, selectbackground="#a5a5a5")
listbox.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.5)

root.mainloop()
