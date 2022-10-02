from threading import Thread
from tkinter import Tk, Scale, Button

class App(Tk):
    def __init__(self, data, gMod):
        Tk.__init__(self)

        self.data = data
        self.gMod = gMod

        self.jump_power_scale = Scale(self, from_ = 0, to = 1000, orient = 'h')
        self.jump_power_scale.grid(row = 0, column = 1)

        self.gravity_scale = Scale(self, from_ = 0, to = 10000, orient = 'h')
        self.gravity_scale.grid(row = 1, column = 1)

        self.config_btn = Button(self, text = 'Save', command = self.configure)
        self.config_btn.grid(row = 2, column = 0)

    def configure(self):
        self.data.jump_power = self.jump_power_scale.get()
        self.gMod.GRAVITY_FORCE = self.gravity_scale.get() / 100

if __name__ == '__main__':
    App().mainloop()
