from tkinter import Tk, Canvas

run = {'red': 7000, 'yellow': 2000, 'green': 5000}
light_number = 0


class TrafficLights(Tk):
    _color = list(run)

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=340, height=120, bg="white")
        self.canvas.grid()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white", outline=self._color[0])
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white", outline=self._color[1])
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white", outline=self._color[2])
        self.running()

    def running(self):
        global light_number
        self.canvas.itemconfigure(self.oval_red, fill='white')
        self.canvas.itemconfigure(self.oval_yellow, fill='white')
        self.canvas.itemconfigure(self.oval_green, fill='white')
        exec(f"self.canvas.itemconfigure(self.oval_{self._color[light_number]}, fill='{self._color[light_number]}')")
        light_number += 1
        if light_number == 3:
            light_number = 0
        self.after(run[self._color[light_number - 1]], self.running)


root = TrafficLights()
root.mainloop()
