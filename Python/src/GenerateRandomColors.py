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

        for i in range(7064):
            Canvas(window, width=12, height=12, bg=random_color()).grid(row=i // 100, column=i % 100)

        window.mainloop()


randomColorGrid()

