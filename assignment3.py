from tkinter import *
from random import randint

# solution version 1: without extensions

def show_duo_names():
    print()
    print('┌─────────────────────┬───────────────────────┐')
    print('│ 0HV120 assignment 3 │ Memory Test           │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 1       │ Ammy Prohkrathok      │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 2       │ Rosalie Bentvelsen    │')
    print('└─────────────────────┴───────────────────────┘')


class MemoryTestWindow:
    def __init__(self):
        start_label = Label(text = "click 'Start' to begin the memory test")
        start_label.pack()

        self.__canvas = Canvas()
        self.__canvas.config(width = 1200)
        self.__canvas.config(height = 700)
        #self.__canvas.config(background = "grey")
        self.__canvas.pack()






        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    root.title('Memory Test')
    root.minsize(600, 400)
    window = MemoryTestWindow()
    root.mainloop()

main()
