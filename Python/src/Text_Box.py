import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title('Enter Canvas Size')

# store user input
canvas_size = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered size as: {canvas_size.get()} '
    showinfo(
        title='Information',
        message=msg
    )


# main window frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# size window
size_label = ttk.Label(signin, text="'Enter Canvas Size such as: 100x100 (whole numbers only, lowercase x only)")
size_label.pack(fill='x', expand=True)

size_entry = ttk.Entry(signin, textvariable=canvas_size)
size_entry.pack(fill='x', expand=True)
size_entry.focus()


# submit button
submit_button = ttk.Button(signin, text="Submit", command=login_clicked)
submit_button.pack(fill='x', expand=True, pady=10)


root.mainloop()

