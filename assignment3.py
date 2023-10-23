from tkinter import *
from random import randint
import time

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
        window.minsize(200, 200)

        self.font = ('sans 20 bold')

        #top label
        self.__start_label = Label(text = "click 'Start' to begin the memory test", font = self.font)
        self.__start_label.pack()

        #make canvas
        self.__canvas = Canvas(root, width = 1200, height = 700)
        self.__canvas.pack()

        #bottom text
        toolbar = Frame(window)
        #start button
        self.__startbutton = Button(toolbar, text = 'start', font = self.font, command= self.count_down)
        self.__startbutton.pack(side = 'left')
        #ms invisible
        label1 = Label(toolbar, text = 'ms invisible:', font = self.font)
        label1.pack(side = 'left')
        #entry from ms invisible
        self.__entry1 = Entry(toolbar, font = self.font)
        self.__entry1.insert(0, "500")
        self.__entry1.pack(side = 'left')
        #ms between
        label2 = Label(toolbar, text = 'ms between:', font = self.font)
        label2.pack(side = 'left')
        #entry ms between
        self.__entry2 = Entry(toolbar, font = self.font)
        self.__entry2.pack(side = 'left')
        self.__entry2.insert(0, "500")
        #sequence length
        label3 = Label(toolbar, text = 'sequence length:', font = self.font)
        label3.pack(side = 'left')
        #entry sequence length
        self.__entry3 = Entry(toolbar, font = self.font)
        self.__entry3.insert(0, "3")
        self.__entry3.pack(side = 'left')
        toolbar.pack(side=BOTTOM)

    #count down
    def count_down(self, count=3):
        self.__startbutton.config(state="disabled")
        if count >= 0:
            self.__start_label.config(text = "counting down...")
            self.__start_label.pack()

            self.__canvas.delete('all')
            self.__canvas.create_text(600, 350, text= count * '.', font=('Arial', 80))
            self.__canvas.after(1000, self.count_down, count-1)
        else: #3. start obervation phase
            self.observation()

    def show(self, square):
        self.__canvas.itemconfigure(square, state="normal")

    def hide(self, square):
        self.__canvas.itemconfigure(square, state="hidden")

    def observation(self):
        self.__start_label.config(text = "watch the sequence...", font = self.font)
        self.__start_label.pack()

        self.__blue_square = self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue", tags = "blue")
        self.__red_square = self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red", tags = "red")
        self.__green_square = self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green", tags = "green")
        self.__yellow_square = self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow", tags = "yellow")
        
        sequence_length = int(self.__entry3.get())
        self.__ms_between = int(self.__entry2.get())
        self.__ms_invisible = int(self.__entry1.get())
        self.__loop_time = self.__ms_between + self.__ms_invisible
        sequence = []

        for i in range(sequence_length):
            random_color = randint(1, 4)
            self.__t = self.__ms_between
            self.__back = self.__t + i*self.__loop_time + self.__ms_invisible
            

            if random_color == 1:
                self.__canvas.after(self.__t + i*self.__loop_time, lambda: self.hide(self.__blue_square))
                self.__canvas.after(self.__back, lambda: self.show(self.__blue_square))
                sequence.append('1')
            elif random_color == 2:
                self.__canvas.after(self.__t + i*self.__loop_time, lambda: self.hides(self.__red_square))
                self.__canvas.after(self.__back, lambda: self.show(self.__red_square))
                sequence.append('2')
            elif random_color == 3:
                self.__canvas.after(self.__t + i*self.__loop_time, lambda: self.hide(self.__green_square))
                self.__canvas.after(self.__back, lambda: self.show(self.__green_square))
                sequence.append('3')
            elif random_color == 4:
                self.__canvas.after(self.__t + i*self.__loop_time, lambda: self.hide(self.__yellow_square))
                self.__canvas.after(self.__back, lambda: self.show(self.__yellow_square))
                sequence.append('4')
       
        
        #sequence list is heel waarschijnlijk nodig voor opdracht 6 vandaar dat ik hem heb laten staan want ik had m ook gebruikt om de code te testen en bekijken
        # hij doet het wel maar ik weet niet hoe ik hem over moet laten gaan naar def sequence()
    
    def sequence(self): #opdracht 5
        self.__start_label.config(text = "repeat the sequence...", font = self.font)
        self.__start_label.pack()
        
        squares = []
        squares.append(self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue"))
        squares.append(self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red"))
        squares.append(self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green"))
        squares.append(self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow"))        

        def click_square(event):
            x = self.__canvas.canvasx(event.x) #coordinaat van muisklik omzetten naar canvas coordinaat
            y = self.__canvas.canvasy(event.y)

            self.__blue_square = self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue", tags = "blue")
            self.__red_square = self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red", tags = "red")
            self.__green_square = self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green", tags = "green")
            self.__yellow_square = self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow", tags = "yellow")
            
            for item in squares:
                if self.__canvas.coords(item)[0] < x < self.__canvas.coords(item)[2] and self.__canvas.coords(item)[1] < y < self.__canvas.coords(item)[3]:
                    print(f"Vierkant {item} is geklikt.")
                    if item == 5:
                        self.__canvas.after(0, lambda: self.hide(self.__blue_square))
                        self.__canvas.after(self.__ms_invisible, lambda: self.show(self.__blue_square))

        self.__canvas.bind("<Button-1>", click_square)


        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()


