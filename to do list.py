import tkinter as tk

def create_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def update_task():
    selected_task = task_list.get(tk.ACTIVE)
    updated_task = entry.get()
    if updated_task and selected_task:
        task_list.delete(tk.ACTIVE)
        task_list.insert(tk.ACTIVE, updated_task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.get(tk.ACTIVE)
    if selected_task:
        task_list.delete(tk.ACTIVE)
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create task entry
entry = tk.Entry(root)
entry.pack()

# Create task list
task_list = tk.Listbox(root)
task_list.pack()

# Create buttons
create_button = tk.Button(root, text="Create", command=create_task)
update_button = tk.Button(root, text="Update", command=update_task)
delete_button = tk.Button(root, text="Delete", command=delete_task)

create_button.pack()
update_button.pack()
delete_button.pack()

root.mainloop()
