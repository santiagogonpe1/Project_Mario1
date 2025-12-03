import pyxel

class Mario:
    img = 1
    u = 0
    v = 0
    mario_width = 16
    mario_height = 16

    def __init__(self):
        #Mario´s coordinates
        self.__x = 152
        self.__y = 127
        #Attribute needed for Mario to follow the packages behavior
        self.__package = []
        #Attribute needed for Mario to follow the boss behavior
        self.__boss = None
        #Attribute needed for Mario to freeze
        self.__frozen = False
        #Attributes needed for Mario to know when a package is caught and in
        #which row
        self.__catch= False
        self.__catch_row= None
        #Attribute needed for Mario to follow the truck behavior
        self.__truck= None

    # Properties and setters of coordinates
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value
    # Frozen state
    @property
    def frozen(self):
        return self.__frozen
    @frozen.setter
    def frozen(self, value):
        if not isinstance(value, bool):
            raise ValueError('Frozen value must be bool')
        else:
            self.__frozen = value

    # Catching packages property and setter
    @property
    def catch(self):
        return self.__catch
    @catch.setter
    def catch(self, value):
        if isinstance(value, bool):
            self.__catch = value
    @property
    def catch_row(self):
        return self.__catch_row
    @catch_row.setter
    def catch_row(self, value):
        if isinstance(value, int) or value is None:
            self.__catch_row = value

    #References to other classes
    @property
    def package(self):
        return self.__package
    @package.setter
    def package(self, value):
        if isinstance(value, list):
            self.__package = value
    @property
    def boss(self):
        return self.__boss
    @boss.setter
    def boss(self, value):
        self.__boss = value
    @property
    def truck(self):
        return self.__truck
    @truck.setter
    def truck(self, value):
        self.__truck = value
    # Methods
    def catch_package(self):
        """Returns True when a package is caught and its row"""
        caught = False
        caught_row = None
        for p in self.package:
            if self.y == 127 and 170 < p.x < 176:
                caught = True
                caught_row = 0
            elif self.y == 95 and 145 < p.x < 151:
                caught = True
                caught_row = 1
            elif self.y == 63 and 145 < p.x < 151:
                caught = True
                caught_row = 3

        self.catch = caught
        self.catch_row = caught_row

    def update(self):
        """Frozen function initialized here to avoid character to move
        during animation"""
        if self.frozen:
            return

        self.catch_package()

        if pyxel.btnp(pyxel.KEY_UP) and self.y > 65:
            self.y -= 32
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.y < 127:
            self.y += 32

    def draw(self):
        """Function to draw the character during gameplay and animated when
        a package is caught or when a package is fallen"""
        if self.boss and self.boss.boss_mario and self.boss.animation_running:
            pyxel.blt(192, 96,
                      Mario.img, Mario.u, 128,
                      Mario.mario_width, Mario.mario_height)

        if self.truck.full:
            pyxel.blt(self.x, self.y,
                      Mario.img, Mario.u, 144,
                      Mario.mario_width, Mario.mario_height)
        else:
            if self.catch and self.catch_row == 0:
                pyxel.blt(self.x, self.y,
                          Mario.img, Mario.u, 160,
                          Mario.mario_width, Mario.mario_height)
            elif self.catch:
                pyxel.blt(self.x, self.y,
                          Mario.img, Mario.u, 16,
                          Mario.mario_width, Mario.mario_height)
            else:
                pyxel.blt(self.x, self.y,
                          Mario.img, Mario.u, Mario.v,
                          Mario.mario_width, Mario.mario_height)