from tkinter import *
from time import sleep
from itertools import cycle

run = {'red': 7, 'yellow': 2, 'green': 5}


class TrafficLights:
    def __init__(self, color):
        _color = color
        window = Tk()
        window.title("Traffic Light")

        self.canvas = Canvas(window, width=340, height=120, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white", outline=_color[0])
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white", outline=_color[1])
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white", outline=_color[2])
        self.running(_color)

    def running(self, col):
        for item in cycle(col):
            self.canvas.itemconfigure(self.oval_red, fill='white')
            self.canvas.itemconfigure(self.oval_yellow, fill='white')
            self.canvas.itemconfigure(self.oval_green, fill='white')
            if item == 'red':
                self.canvas.itemconfigure(self.oval_red, fill='red')
            if item == 'yellow':
                self.canvas.itemconfigure(self.oval_yellow, fill='yellow')
            if item == 'green':
                self.canvas.itemconfigure(self.oval_green, fill='green')
            self.canvas.update()
            sleep(run[item])


light = TrafficLights(list(run))