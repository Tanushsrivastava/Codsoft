import tkinter as tk
from tkinter import messagebox

# Global contact list
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contacts.append((name, phone))
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Name and Phone cannot be empty!")

# Function to view contact list
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        name, phone = contact
        contact_list.insert(tk.END, f"{name}: {phone}")

# Function to search for a contact
def search_contact():
    search_text = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        name, phone = contact
        if search_text in name or search_text in phone:
            contact_list.insert(tk.END, f"{name}: {phone}")

# Function to update a contact
def update_contact():
    selected_index = contact_list.curselection()
    
    if selected_index:
        selected_index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        
        if name and phone:
            contacts[selected_index] = (name, phone)
            view_contacts()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        contact_list.delete(selected_index)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create and configure widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

root.mainloop()
