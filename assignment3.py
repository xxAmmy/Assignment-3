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
    def __init__(self, root):
        window = root
        window.title('Memory Test')
        window.minsize(600, 400)

        #top label
        start_label = Label(text = "click 'Start' to begin the memory test")
        start_label.pack()

        #make canvas
        self.__canvas = Canvas(root)
        self.__canvas.config(width = 1200)
        self.__canvas.config(height = 700)
        self.__canvas.config(background = "white")
        self.__canvas.pack()

        #bottom text
        toolbar = Frame(window)
        startbutton = Button(toolbar, text = 'start')
        startbutton.pack(side = 'left')
        label1 = Label(toolbar, text = 'ms invisible:')
        label1.pack(side = 'left')
        entry1 = Entry(toolbar)
        entry1.pack(side = 'left')
        label2 = Label(toolbar, text = 'ms between:')
        label2.pack(side = 'left')
        entry2 = Entry(toolbar)
        entry2.pack(side = 'left')
        label3 = Label(toolbar, text = 'sequence length:')
        label3.pack(side = 'left')
        entry3 = Entry(toolbar)
        entry3.pack(side = 'left')
        toolbar.pack(side=BOTTOM)






        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()
