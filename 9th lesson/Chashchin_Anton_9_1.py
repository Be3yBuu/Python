from tkinter import Tk, Canvas


class TrafficLights(Tk):
    __color = {'red': 7000, 'yellow': 2000, 'green': 5000}
    __light_number = 0

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=240, height=340, bg="black")
        self.canvas.pack()
        self.resizable(width=False, height=False)
        self.title('Traffic Lights')

        self.oval_red = self.canvas.create_oval(70, 10, 170, 110)
        self.oval_yellow = self.canvas.create_oval(70, 120, 170, 220)
        self.oval_green = self.canvas.create_oval(70, 230, 170, 330)
        self.running()

    def running(self):
        for item in list(self.__color):
            exec(f"self.canvas.itemconfigure(self.oval_{item}, fill='grey')")
        exec(f"self.canvas.itemconfigure(self.oval_{list(self.__color)[self.__light_number]},"
             f" fill='{list(self.__color)[self.__light_number]}')")
        self.__light_number += 1
        if self.__light_number == 3:
            self.__light_number = 0
        self.after(self.__color[list(self.__color)[self.__light_number - 1]], self.running)


root = TrafficLights()
root.mainloop()
