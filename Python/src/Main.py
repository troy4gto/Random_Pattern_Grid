from tkinter import*
import tkinter as tk
import Text_Box as tb

root = tk.Tk()

defined_size = tb.size_var.get()


root.geometry(defined_size)

c = tk.Canvas(root, height=1000, width=1000, bg='white')


def create_grid(event=None):

    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines
    for i in range(0, w, 12):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines
    for i in range(0, h, 12):
        c.create_line([(0, i), (w, i)], tag='grid_line')


c.bind('<Configure>', create_grid)
c.pack(fill=tk.BOTH, expand=True)

root.mainloop()

