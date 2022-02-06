from tkinter import *
import Text_Box as tb
from random import randint

defined_size = tb.canvas_size.get()


def random_color():
    colors = ['blue', 'white']

    return colors[randint(0, len(colors)-1)]


class randomColorGrid:
    def __init__(self):
        window = Tk()
        window.geometry(defined_size)
        window.title("Display Random Colors")

        for i in range(3064):
            if i % 2 == (i // 8) % 2:
                color = random_color()
            else:
                color = random_color()
            Canvas(window, width=25, height=25, bg=color).grid(row=i // 60, column=i % 60)

        window.mainloop()


randomColorGrid()

