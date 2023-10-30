import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the input and result
entry = tk.Entry(window, width=40)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]
row_num, col_num = 1, 0
for button_text in buttons:
    tk.Button(window, text=button_text, padx=20, pady=20, command=lambda text=button_text: button_click(text) if text != '=' else calculate()).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Add a clear button
clear_button = tk.Button(window, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=row_num, column=col_num, columnspan=4)

# Start the main loop
window.mainloop()

