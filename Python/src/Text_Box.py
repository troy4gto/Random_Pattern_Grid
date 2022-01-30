import tkinter as tk
from tkinter import *
root = tk.Tk()
ws = Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing size and password
size_var = tk.StringVar()


# defining a function that will
# get the size and password and
# print them on the screen
def submit():

    size = size_var.get()

    print("The size is : " + size)


# creating a label for
# size using widget Label
size_label = tk.Label(root, text='User Size', font=('calibre', 10, 'bold'))

# creating a entry for input
# size using widget Entry
size_entry = tk.Entry(root, textvariable=size_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
size_label.grid(row=0, column=0)
size_entry.grid(row=0, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
