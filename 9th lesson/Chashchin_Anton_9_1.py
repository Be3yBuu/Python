from tkinter import Tk, Canvas

run = {'red': 7000, 'yellow': 2000, 'green': 5000}
light_number = 0


class TrafficLights(Tk):
    _color = list(run)

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=240, height=340, bg="white")
        self.canvas.grid()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white", outline=self._color[0])
        self.oval_yellow = self.canvas.create_oval(10, 120, 110, 220, fill="white", outline=self._color[1])
        self.oval_green = self.canvas.create_oval(10, 230, 110, 330, fill="white", outline=self._color[2])
        self.running()

    def running(self):
        global light_number
        for item in self._color:
            exec(f"self.canvas.itemconfigure(self.oval_{item}, fill='white')")
        exec(f"self.canvas.itemconfigure(self.oval_{self._color[light_number]}, fill='{self._color[light_number]}')")
        light_number += 1
        if light_number == 3:
            light_number = 0
        self.after(run[self._color[light_number - 1]], self.running)


root = TrafficLights()
root.mainloop()
