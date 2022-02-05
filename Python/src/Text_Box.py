import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Enter width and height')

# store email address and password
width = tk.StringVar()
height = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered width: {width.get()} and height: {height.get()}'
    showinfo(
        title='Information',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
width_label = ttk.Label(signin, text="width:")
width_label.pack(fill='x', expand=True)

width_entry = ttk.Entry(signin, textvariable=width)
width_entry.pack(fill='x', expand=True)
width_entry.focus()

# password
height_label = ttk.Label(signin, text="height:")
height_label.pack(fill='x', expand=True)

height_entry = ttk.Entry(signin, textvariable=height)
height_entry.pack(fill='x', expand=True)

# login button
submit_button = ttk.Button(signin, text="Submit", command=login_clicked)
submit_button.pack(fill='x', expand=True, pady=10)


root.mainloop()

