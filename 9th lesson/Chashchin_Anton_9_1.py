from tkinter import *
from time import sleep
from itertools import cycle

background = ['red', 'yellow', 'green']


class TrafficLights:

    def __init__(self, color):
        _color = [color[0], color[1], color[2]]
        window = Tk()
        window.title("Traffic Light")

        self.canvas = Canvas(window, width=340, height=120, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white", outline=_color[0])
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white", outline=_color[1])
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white", outline=_color[2])
        self.running()

    def running(self):
        for item in cycle(background):
            if item == 'red':
                self.canvas.itemconfigure(self.oval_red, fill='red')
                self.canvas.itemconfigure(self.oval_green, fill='white')
                self.canvas.update()
                sleep(7)
            if item == 'yellow':
                self.canvas.itemconfigure(self.oval_yellow, fill='yellow')
                self.canvas.itemconfigure(self.oval_red, fill='white')
                self.canvas.update()
                sleep(2)
            if item == 'green':
                self.canvas.itemconfigure(self.oval_green, fill='green')
                self.canvas.itemconfigure(self.oval_yellow, fill='white')
                self.canvas.update()
                sleep(5)


light = TrafficLights(background)
