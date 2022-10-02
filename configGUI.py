from threading import Thread
from tkinter import Tk, Scale, Button, Label, Entry

class App(Tk):
    def __init__(self, data, gMod):
        Tk.__init__(self)

        self.data = data
        self.gMod = gMod

        self.jump_power_lbl = Label(self, text = 'Jump Power')
        self.jump_power_lbl.grid(row = 0, column = 0)

        self.jump_power_scale = Scale(self, from_ = 0, to = 1000, orient = 'h')
        self.jump_power_scale.grid(row = 0, column = 1)

        self.gravity_lbl = Label(self, text = 'Gravity')
        self.gravity_lbl.grid(row = 1, column = 0)

        self.gravity_inp = Entry(self)
        self.gravity_inp.insert('0', '9.81')
        self.gravity_inp.grid(row = 1, column = 1)

        self.config_btn = Button(self, text = 'Save', command = self.configure)
        self.config_btn.grid(row = 2, column = 0)

    def configure(self):
        self.data.jump_power = self.jump_power_scale.get()
        try:
            self.gMod.GRAVITY_FORCE = eval(self.gravity_inp.get(), {
                'g': self.gMod.GRAVITY_FORCE
            }, {})
        except:
            pass

if __name__ == '__main__':
    App().mainloop()
