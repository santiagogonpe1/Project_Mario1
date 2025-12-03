import pyxel


class Luigi:
    img= 1
    u= 16
    v=0
    luigi_width= 16
    luigi_height= 16

    def __init__(self):
        #Luigi´s coordinates
        self.__x = 54
        self.__y = 64
        #Attribute needed for Luigi to follow the packages behavior
        self.__package = []
        #Attribute needed for Luigi to follow the boss behavior
        self.__boss= None
        #Attribute needed for Luigi to freeze
        self.__frozen = False
        # Attributes needed for Mario to know when a package is caught and in
        # which row
        self.__catch= False
        self.__catch_row= None
        #Attribute needed for Luigi to follow the truck behavior
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

    # Class Methods
    def catch_package(self):
        """Returns True when a package is caught and its row"""
        caught= False
        caught_row= None
        for p in self.package:
            if self.y == 116 and 64 < p.x < 70:
                 caught= True
                 caught_row= 0
            elif self.y == 90 and 64 < p.x < 70:
                caught= True
                caught_row = 2
            elif self.y == 64 and 64 < p.x < 70:
                caught= True
                caught_row = 4

        self.catch= caught
        self.catch_row= caught_row

    def update(self):
        """Frozen function initialized here to avoid character to move
        during animation"""
        if self.frozen:
            return

        self.catch_package()

        if pyxel.btnp(pyxel.KEY_W) and self.y > 65:
            self.y-=26
        elif pyxel.btnp(pyxel.KEY_S) and self.y < 115:
            self.y+=26


    def draw(self):
        """Function to draw the character during gameplay and animated when
                a package is caught or when a package is fallen"""
        if self.boss and self.boss.boss_luigi and self.boss.animation_running:
            pyxel.blt(26, 124, Luigi.img, 16, 128,Luigi.luigi_width,
                      Luigi.luigi_height )

        if self.truck.full:
            pyxel.blt(self.x, self.y,
                      Luigi.img, Luigi.u, 144,
                      Luigi.luigi_width, Luigi.luigi_height)
        else:
            if self.catch and self.catch_row == 4:
                pyxel.blt(self.x, self.y, Luigi.img, Luigi.u,
                            160,
                            Luigi.luigi_width, Luigi.luigi_height)
            elif self.catch:
                pyxel.blt(self.x, self.y, Luigi.img, Luigi.u,
                            16,
                             Luigi.luigi_width, Luigi.luigi_height)
            else:
                pyxel.blt(self.x, self.y, Luigi.img, Luigi.u, Luigi.v,
                         Luigi.luigi_width, Luigi.luigi_height)