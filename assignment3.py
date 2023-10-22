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

        #top label
        self.__start_label = Label(text = "click 'Start' to begin the memory test", font = ('Arial bold', 20))
        self.__start_label.pack()

        #make canvas
        self.__canvas = Canvas(root, width = 1200, height = 700, bg = 'white')
        self.__canvas.pack()

        #bottom text
        toolbar = Frame(window)
        self.__startbutton = Button(toolbar, text = 'start', font = ("Arial bold", 20), command = self.count_down)
        self.__startbutton.pack(side = 'left')
        label1 = Label(toolbar, text = 'ms invisible:', font = ("Arial bold", 20))
        label1.pack(side = 'left')
        self.__entry1 = Entry(toolbar, font = ('Arial bold', 20))
        self.__entry1.insert(0, "500")
        self.__entry1.pack(side = 'left')
        label2 = Label(toolbar, text = 'ms between:', font = ("Arial bold", 20))
        label2.pack(side = 'left')
        self.__entry2 = Entry(toolbar, font = ("Arial bold", 20))
        self.__entry2.pack(side = 'left')
        self.__entry2.insert(0, "500")
        label3 = Label(toolbar, text = 'sequence length:', font = ("Arial bold", 20))
        label3.pack(side = 'left')
        self.__entry3 = Entry(toolbar, font = ("Arial bold", 20))
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

    def observation(self): #hier zou je root bij moeten zetten voor de code hieronder maar dan werkt het niet meer
        self.__start_label.config(text = "watch the sequence...", font = ('Arial bold', 20))
        self.__start_label.pack()

        blue_square = self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue", tags = "blue")
        red_square = self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red", tags = "red")
        green_square = self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green", tags = "green")
        yellow_square = self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow", tags = "yellow")
        
        for _ in range(self.__entry3):
            random_color = randint(1,4)
            if random_color == 1:
                def hide_blue(root, blue_square):
                    self.__canvas.delete(blue_square)
                root.after(2000, hide_blue) #ipv 2000 dan de self.__entry1
            if random_color == 2:
                def hide_red(root, red_square):
                    self.__canvas.delete(red_square)
                root.after(2000, hide_red)
            if random_color == 3:
                def hide_green(root, green_square):
                    self.__canvas.delete(green_square)
                root.after(2000, hide_green)
            if random_color == 4:
                def hide_yellow(root, yellow_square):
                    self.__canvas.delete(yellow_square)
                root.after(2000, hide_yellow)

    #hier is de code bewerkt
    #for de range (self.__entry3) wordt self.__entry3 niet gezien als een integer ook niet als ik zet int(self.__entry3)
    #dus vandaar dat ik hem hier als getal 3 heb weergegeven
    #je hebt nu voor elke sqaure een aparte functie gemaakt voor verdwijnen maar je kon ook een fucntie met --> def hide_square(self, sqaure), maken ik heb dat gedaan en toen kon hij de after functie niet
    #toepassen omdat je de after functie alleen kan gebruiken voor een root en niet een self (idk wat dat betekent maar die error kreeg ik)

        for _ in range(3):
            random_color = randint(1, 4)
            if random_color == 1:
                self.__canvas.after(2000, lambda: self.__canvas.delete(blue_square))
            elif random_color == 2:
                self.__canvas.after(2000, lambda: self.__canvas.delete(red_square))
            elif random_color == 3:
                self.__canvas.after(2000, lambda: self.__canvas.delete(green_square))
            elif random_color == 4:
                self.__canvas.after(2000, lambda: self.__canvas.delete(yellow_square))

    #hij doet het nu alleen nog maar 1 keer, maar wel maar 1 vierkantje tegelijk die verdwijnt en dan terugkomt
    #kijk eens naar 8.6 daar is een beetje hetzelfde proces en daarom was ik een beetje aan begonnen

        sequence_length = int(self.__entry3.get())
        ms_between = int(self.__entry2.get())
        ms_invisible = int(self.__entry1.get())
        nr_dissapear = 0

        #for _ in range(sequence_length):
        if nr_dissapear < sequence_length:
            random_color = randint(1, 4)
            if random_color == 1:
                self.__canvas.after(ms_between, lambda: self.__canvas.delete(blue_square))
                self.__canvas.after(2000, lambda: self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue", tags = "blue"))
                nr_dissapear = nr_dissapear +1
            elif random_color == 2:
                self.__canvas.after(ms_between, lambda: self.__canvas.delete(red_square))
                self.__canvas.after(2000, lambda: self.__canvas.create_rectangle(620, 30, 920, 330, fill  = "red", tags = "red"))
                nr_dissapear = nr_dissapear +1
            elif random_color == 3:
                self.__canvas.after(ms_between, lambda: self.__canvas.delete(green_square))
                self.__canvas.after(2000, lambda: self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green", tags = "green"))
                nr_dissapear = nr_dissapear +1
            elif random_color == 4:
                self.__canvas.after(ms_between, lambda: self.__canvas.delete(yellow_square))
                self.__canvas.after(2000, lambda: self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow", tags = "yellow"))
                nr_dissapear = nr_dissapear +1
    
    
    def sequence(self):
        squares = []
        squares.append(self.__canvas.create_rectangle(280, 30, 580, 330, fill = "blue"))
        squares.append(self.__canvas.create_rectangle(620, 30, 920, 330, fill = "red"))
        squares.append(self.__canvas.create_rectangle(280, 370, 580, 670, fill = "green"))
        squares.append(self.__canvas.create_rectangle(620, 370, 920, 670, fill = "yellow"))        

        def click_square(event):
            x = self.__canvas.canvasx(event.x) #coordinaat van muisklik omzetten naar canvas coordinaat
            y = self.__canvas.canvasy(event.y)

            for item in squares:
                if self.__canvas.coords(item)[0] < x < self.__canvas.coords(item)[2] and self.__canvas.coords(item)[1] < y < self.__canvas.coords(item)[3]:
                    print(f"Vierkant {item} is geklikt.")

        self.__canvas.bind("<Button-1>", click_square)


        return  # replace with you code

def main():
    show_duo_names()

    root = Tk()
    window = MemoryTestWindow(root)
    root.mainloop()

main()


