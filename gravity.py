GRAVITY_FORCE = 9.81

class SolidRect:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.width, self.height = w, h

class GravityManager:
    def __init__(self, bounciness = 0):
        self._is_falling = False
        self.accel = 0
        self.bounciness = bounciness

    def fallSpeed(self):
        if self._is_falling:
            self.accel += 9.81
            return self.accel
        else:
            return 0

    def jump(self, power):
        self._is_falling = True
        self.accel = -power

    def fall(self):
        self._is_falling = True

    def land(self):
        self._is_falling = False
