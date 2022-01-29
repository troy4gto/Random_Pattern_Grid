from tkinter import*
import tkinter as tk


root = tk.Tk()

myLabel = Label(root, text="Random Pattern")

myLabel.pack()

c = tk.Canvas(root, height=0.00125, width=0.00125, bg='white')


def create_grid(event=None):

    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 100):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 100):
        c.create_line([(0, i), (w, i)], tag='grid_line')


c.bind('<Configure>', create_grid)
c.pack(fill=tk.BOTH, expand=True)

root.mainloop()

