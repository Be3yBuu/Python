from tkinter import Tk, Canvas


class TrafficLights(Tk):
    _color = {'red': 7000, 'yellow': 2000, 'green': 5000}
    light_number = 0

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=240, height=340, bg="black")
        self.canvas.pack()
        self.resizable(width=False, height=False)

        self.oval_red = self.canvas.create_oval(70, 10, 170, 110, fill="white", outline=list(self._color)[0])
        self.oval_yellow = self.canvas.create_oval(70, 120, 170, 220, fill="white", outline=list(self._color)[1])
        self.oval_green = self.canvas.create_oval(70, 230, 170, 330, fill="white", outline=list(self._color)[2])
        self.running()

    def running(self):
        for item in list(self._color):
            exec(f"self.canvas.itemconfigure(self.oval_{item}, fill='white')")
        exec(f"self.canvas.itemconfigure(self.oval_{list(self._color)[self.light_number]},"
             f" fill='{list(self._color)[self.light_number]}')")
        self.light_number += 1
        if self.light_number == 3:
            self.light_number = 0
        self.after(self._color[list(self._color)[self.light_number - 1]], self.running)


root = TrafficLights()
root.mainloop()
