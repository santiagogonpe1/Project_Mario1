import pyxel

class Mario:
    img = 1
    u = 0
    v = 0
    mario_width = 16
    mario_height = 16
    DX = 1

    def __init__(self):
        self.x = 152
        self.y = 127
        self.package = []  # NOW A LIST
        self.boss = None       # boss may be None if not used
        self.frozen = False

    def get_falling_package(self):
        """
        Returns the first package that is currently falling.
        If none are falling, returns None.
        """
        falling = [p for p in self.package if p.falling]
        return falling[0] if falling else None

    def update(self):
        if self.frozen:
            return
        if pyxel.btnp(pyxel.KEY_UP) and self.y > 65:
            self.y -= 32
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.y < 127:
            self.y += 32

    def draw(self):
        package = self.get_falling_package()

        if self.boss and self.boss.boss_mario and self.boss.animation_running:
            pyxel.blt(200, 96,
                Mario.img, 0, 128,
                Mario.mario_width, Mario.mario_height)
        package = self.get_falling_package()
        # CASE 2: Mario reacts to package row
        if package:
            # package in row 1, Mario at middle row
            if self.y == 95 and package.row == 1:
                pyxel.blt(self.x, self.y,
                    Mario.img, 0, 16,
                    Mario.mario_width, Mario.mario_height)

            # package in row 3, Mario at top row
            elif self.y == 63 and package.row == 3:
                pyxel.blt(self.x, self.y,
                    Mario.img, 0, 16,
                    Mario.mario_width, Mario.mario_height)

        pyxel.blt(self.x, self.y,
            Mario.img, Mario.u, Mario.v,
            Mario.mario_width, Mario.mario_height)