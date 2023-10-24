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

        self.__click_counter = 0 # these variables are for recall_1 and click_square
        self.__recall = [] # ik zet ze hier omdat als ik ze in de functie zelf zet het hele tijd naar 0 wordt gereset

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
#vanaf hier werkt observation wel
# ik gok dat def observation geen toegang meer had tot de hide en show functie wanneer je er een vierkant in plaats
#blijkbaar doet hij t wel als je er overal een aparte functie van maakt
    def hide(self, square):
        self.__canvas.itemconfigure(square, state="hidden")
    def show(self, square):
        self.__canvas.itemconfigure(square, state="normal")

    def hide_blue(self):
        self.hide(self.__blue_square)
    def show_blue(self):
        self.show(self.__blue_square)

    def hide_red(self):
        self.hide(self.__red_square)
    def show_red(self):
        self.show(self.__red_square)

    def hide_green(self):
        self.hide(self.__green_square)
    def show_green(self):
        self.show(self.__green_square)

    def hide_yellow(self):
        self.hide(self.__yellow_square)
    def show_yellow(self):
        self.show(self.__yellow_square)


    def observation(self):
        self.__start_label.config(text = "watch the sequence...", font = self.font)
        self.__start_label.pack()

        self.__blue_square = self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue", tags = "blue")
        self.__red_square = self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red", tags = "red")
        self.__green_square = self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green", tags = "green")
        self.__yellow_square = self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow", tags = "yellow")
        
        self.__ms_invisible = int(self.__entry1.get())
        self.__ms_between = int(self.__entry2.get())
        self.__sequence_length = int(self.__entry3.get())
        loop_time = self.__ms_between + self.__ms_invisible
        self.__sequence = []

        for i in range(self.__sequence_length):
            random_color = randint(1, 4)
            t = self.__ms_between
            back = t + i * loop_time + self.__ms_invisible
            print(f"t: {t}, i: {i}, loop_time: {loop_time}")

            if random_color == 1:
                self.__canvas.after(t + i * loop_time, self.hide_blue)
                self.__canvas.after(back, self.show_blue)
                self.__sequence.append('1')
            elif random_color == 2:
                self.__canvas.after(t + i * loop_time, self.hide_red)
                self.__canvas.after(back, self.show_red)
                self.__sequence.append('2')
            elif random_color == 3:
                self.__canvas.after(t + i * loop_time, self.hide_green)
                self.__canvas.after(back, self.show_green)
                self.__sequence.append('3')
            elif random_color == 4:
                self.__canvas.after(t + i * loop_time, self.hide_yellow)
                self.__canvas.after(back, self.show_yellow)
                self.__sequence.append('4')
        print(self.__sequence)
        self.__canvas.after(self.__sequence_length*loop_time + self.__ms_between + self.__ms_invisible, self.recall_1)
            
    def recall_1(self): #opdracht 5
        self.__start_label.config(text = "repeat the sequence...", font = self.font)
        self.__start_label.pack()
        
        self.__squares = []
        self.__squares.append(self.__blue_square)
        self.__squares.append(self.__red_square)
        self.__squares.append(self.__green_square)
        self.__squares.append(self.__yellow_square) 

        self.__canvas.bind("<Button-1>", self.click_square) 

    def click_square(self, event):
        x = self.__canvas.canvasx(event.x) #coordinaat van muisklik omzetten naar canvas coordinaat
        y = self.__canvas.canvasy(event.y)

        for item in self.__squares:
            overlapping_items = self.__canvas.find_overlapping(x, y, x, y)
            if item in overlapping_items:
                #print(f"Vierkant {item} is geklikt.")
                if item == 5:
                    self.__canvas.after(0, self.hide_blue)
                    self.__canvas.after(self.__ms_invisible, self.show_blue)
                    self.__recall.append('1')
                elif item == 6:
                    self.__canvas.after(0, self.hide_red)
                    self.__canvas.after(self.__ms_invisible, self.show_red)
                    self.__recall.append('2')
                elif item == 7:
                    self.__canvas.after(0, self.hide_green)
                    self.__canvas.after(self.__ms_invisible, self.show_green)
                    self.__recall.append('3')
                elif item == 8:
                    self.__canvas.after(0, self.hide_yellow)
                    self.__canvas.after(self.__ms_invisible, self.show_yellow)
                    self.__recall.append('4')
                self.__click_counter += 1  
                if self.__click_counter == self.__sequence_length: #when click counter == seq lenght, no more clicks allowed
                    self.__canvas.unbind("<Button-1>")
                    self.__canvas.after(self.__ms_invisible + 500, self.check_recall)

    def check_recall(self): # opdracht 6
        #print(self.__recall)
        #print(self.__sequence)
        self.__start_label.config(text = "", font = self.font)
        self.__start_label.pack()
        self.__canvas.delete('all')
        self.__startbutton.config(state="active")

        if self.__recall == self.__sequence:
            self.__canvas.create_text(600, 350, text = 'the sequence was correct!', font = self.font)
            #print('the sequence was correct!')
        else:
            self.__canvas.create_text(600, 350, text = 'the sequence was incorrect...', font = self.font)
            #print('the sequence was incorrect ...')
        
        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()


