import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ====== Functions ======
def add_task():
    task = entry_task.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected)
    else:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def edit_task():
    selected = tasks_listbox.curselection()
    if selected:
        current_task = tasks_listbox.get(selected)
        new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=current_task)
        if new_task:
            tasks_listbox.delete(selected)
            tasks_listbox.insert(selected, new_task)
    else:
        messagebox.showwarning("Select Task", "Please select a task to edit.")

def mark_completed():
    selected = tasks_listbox.curselection()
    if selected:
        task = tasks_listbox.get(selected)
        if not task.startswith("✔ "):
            tasks_listbox.delete(selected)
            tasks_listbox.insert(selected, f"✔ {task}")
    else:
        messagebox.showwarning("Select Task", "Please select a task to mark as completed.")

# ====== Main Window ======
root = tk.Tk()
root.title("Professional To-Do List")
root.geometry("450x500")
root.configure(bg="#f0f4f7")


# ====== Title ======
title = tk.Label(root, text="My To-Do List", font=("Segoe UI", 18, "bold"), bg="#f0f4f7", fg="#0F4C75")
title.pack(pady=20)

# ====== Task Entry Frame ======
entry_frame = tk.Frame(root, bg="#f0f4f7")
entry_frame.pack(pady=10)

entry_task = tk.Entry(entry_frame, font=("Segoe UI", 12), width=28, bd=2, relief="groove")
entry_task.grid(row=0, column=0, padx=(0,10))

add_btn = tk.Button(entry_frame, text="Add Task", font=("Segoe UI", 11, "bold"),
                    bg="#3282B8", fg="white", width=12, command=add_task)
add_btn.grid(row=0, column=1)

# ====== Tasks Listbox with Scrollbar ======
tasks_frame = tk.Frame(root)
tasks_frame.pack(pady=10)

scrollbar = tk.Scrollbar(tasks_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox = tk.Listbox(tasks_frame, font=("Segoe UI", 12), width=40, height=15,
                           yscrollcommand=scrollbar.set, selectbackground="#0F4C75",
                           activestyle="none")
tasks_listbox.pack()
scrollbar.config(command=tasks_listbox.yview)

# ====== Action Buttons ======
action_frame = tk.Frame(root, bg="#f0f4f7")
action_frame.pack(pady=15)

edit_btn = tk.Button(action_frame, text="Edit Task", font=("Segoe UI", 11, "bold"),
                     bg="#FFB000", fg="white", width=12, command=edit_task)
edit_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(action_frame, text="Delete Task", font=("Segoe UI", 11, "bold"),
                       bg="#D00000", fg="white", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

complete_btn = tk.Button(action_frame, text="Mark Completed", font=("Segoe UI", 11, "bold"),
                         bg="#0F4C75", fg="white", width=15, command=mark_completed)
complete_btn.grid(row=0, column=2, padx=5)

# ====== Footer ======
footer = tk.Label(root, text="Professional To-Do List by Aman", font=("Segoe UI", 9),
                  bg="#f0f4f7", fg="#333")
footer.pack(side="bottom", pady=10)

# ====== Run App ======
root.mainloop()
