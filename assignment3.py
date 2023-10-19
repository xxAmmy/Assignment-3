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

#1 layout start screen
class MemoryTestWindow:
    def __init__(self, root):
        window = root
        window.title('Memory Test')
        window.minsize(600, 400)

        #top label
        self.__start_label = Label(text = "click 'Start' to begin the memory test", font = ('Arial bold', 20))
        self.__start_label.pack()

        #make canvas
        self.__canvas = Canvas(root, width = 1200, height = 700, bg = 'white')
        self.__canvas.pack()

        #bottom text
        toolbar = Frame(window)
        self.__startbutton = Button(toolbar, text = 'start', font = ("Arial bold", 20))
        self.__startbutton.pack(side = 'left')
        label1 = Label(toolbar, text = 'ms invisible:', font = ("Arial bold", 20))
        label1.pack(side = 'left')
        entry1 = Entry(toolbar, font = ('Arial bold', 20))
        entry1.insert(0, "500")
        entry1.pack(side = 'left')
        label2 = Label(toolbar, text = 'ms between:', font = ("Arial bold", 20))
        label2.pack(side = 'left')
        entry2 = Entry(toolbar, font = ("Arial bold", 20))
        entry2.pack(side = 'left')
        entry2.insert(0, "500")
        label3 = Label(toolbar, text = 'sequence length:', font = ("Arial bold", 20))
        label3.pack(side = 'left')
        entry3 = Entry(toolbar, font = ("Arial bold", 20))
        entry3.insert(0, "3")
        entry3.pack(side = 'left')
        toolbar.pack(side=BOTTOM)

    #count down
    def count_down(self, count=3):
        self.__startbutton.config(state="disabled")
        if count >= 0:
            self.__start_label.config(text = "counting down...")
            self.__start_label.pack()

            self.__canvas.delete('all')
            self.__canvas.create_text(100, 100, text= count * '.', font=('Arial', 36))
            self.__canvas.after(1000, self.count_down, count-1)

    #3. start obervation phase
        self.observation()

    def observation(self):
        self.__canvas.create_rectangle(300, 300, 300, 300, fill = "red")

        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()


