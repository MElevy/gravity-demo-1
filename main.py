from pyglet import app
from pyglet.clock import schedule_interval
from pyglet.shapes import Rectangle
from pyglet.window import Window, key as keys

from threading import Thread

import gravity as g
from configGUI import App

def runGuiThread():
    Thread(target = App(Data).mainloop).start()

class Data:
    jump_power = 500
    x_direction = 0

class KeyManager:
    class Pressed:
        W = False
        A = False
        D = False

def isYColliding(rect1, rect2):
    return (
        (rect1.y < rect2.y and rect1.y + rect1.height > rect2.y) or
        (rect2.y < rect1.y and rect2.y + rect2.height > rect1.y)
    )

def isXColliding(rect1, rect2):
    return (
        (rect1.x < rect2.x and rect1.x + rect1.width > rect2.x) or
        (rect2.x < rect1.x and rect2.x + rect2.width > rect1.x)
    )

def isColliding(rect1, rect2):
    return isYColliding(rect1, rect2) and isXColliding(rect1, rect2)

class GravityDemo(Window):
    def __init__(self):
        Window.__init__(self, width = 1000, height = 750)

        self.platform = Rectangle(
            100, 100, self.width - 200, 50, color = (50, 225, 100)
        )
        self.platform_collider = Rectangle(100, 103, self.width - 200, 50)
        self.player = Rectangle(self.width / 2, self.height / 2, 50, 50)

        self.gManager = g.GravityManager(100)

        schedule_interval(self.update, 1 / 60)

    def on_key_press(self, key, mod):
        if key == keys.A:
            KeyManager.Pressed.A = True
        elif key == keys.D:
            KeyManager.Pressed.D = True
        elif key == keys.W:
            KeyManager.Pressed.W = True

    def on_key_release(self, key, mod):
        if key == keys.A:
            KeyManager.Pressed.A = False
        elif key == keys.D:
            KeyManager.Pressed.D = False
        elif key == keys.W:
            KeyManager.Pressed.W = False

    def update(self, dt):
        if not isColliding(self.platform_collider, self.player):
            if Data.x_direction == 1:
                self.player.x += 100 * dt
            elif Data.x_direction == -1:
                self.player.x -= 100 * dt

            self.gManager.fall()
        else:
            self.gManager.land()
            if KeyManager.Pressed.A:
                self.player.x -= 250 * dt
                Data.x_direction = -1
            if KeyManager.Pressed.D:
                self.player.x += 250 * dt
                Data.x_direction = 1
            if not (KeyManager.Pressed.A or KeyManager.Pressed.D):
                Data.x_direction = 0

            if KeyManager.Pressed.W:
                self.gManager.jump(Data.jump_power)

        self.player.y -= self.gManager.fallSpeed() * dt

    def on_draw(self):
        self.clear()

        self.platform.draw()
        self.player.draw()

if __name__ == '__main__':
    window = GravityDemo()
    Thread(target = app.run).start()
    App(Data, g).mainloop()
