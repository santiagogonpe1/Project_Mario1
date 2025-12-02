import pyxel


class Luigi:
    img= 1
    u= 16
    v=0
    luigi_width= 16
    luigi_height= 16
    DX= 1

    def __init__(self):
        self.x = 54
        self.y = 64
        self.package = []
        self.boss= None
        self.frozen = False

    def get_falling_package(self):
        """
        Returns the first falling package, or None if no package is falling.
        """
        falling = [p for p in self.package if p.falling]
        return falling[0] if falling else None

    def update(self):
        """Frozen function initialized here to avoid character to move
        during animation"""
        if self.frozen:
            return
        if pyxel.btnp(pyxel.KEY_W) and self.y > 65:
            self.y-=26
        elif pyxel.btnp(pyxel.KEY_S) and self.y < 115:
            self.y+=26
    def draw(self):
        """Function to draw the character during gameplay and animated when
        falling package"""
        package = self.get_falling_package()
        if self.boss and self.boss.boss_luigi and self.boss.animation_running:
            pyxel.blt(24, 128, Luigi.img, 16, 128,Luigi.luigi_width,
                      Luigi.luigi_height )
        # Luigi reacts to package row
        if package:
            # package in row 1, Mario at middle row
            if self.y == 116 and package.row == 1:
                pyxel.blt(self.x, self.y, Luigi.img, 16,
                          16,
                          Luigi.luigi_width, Luigi.luigi_height)
            # package in row 3, Mario at top row
            elif self.y == 90 and package.row == 3:
                pyxel.blt(self.x, self.y, Luigi.img, 16,
                          16,
                          Luigi.luigi_width, Luigi.luigi_height)

        pyxel.blt(self.x, self.y, Luigi.img, Luigi.u, Luigi.v,
                  Luigi.luigi_width, Luigi.luigi_height)
