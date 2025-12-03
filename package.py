import pyxel

class Package:
    img=0
    u= 51
    v= 5
    package_width= 11
    package_height= 6
    falling= False
    row_y = [130, 112, 96, 80, 64]
    max_x = [68, 148, 68, 148, 68]
    character = ["luigi", "mario", "luigi", "mario", "luigi"]
    check_characters_y = [116, 95, 90, 63, 64]
    next_x = [80, 136, 80, 136, None]

    def __init__(self,luigi, mario, truck):
        """Calling the parameters needed to initialize the package"""
        self.x = 192
        self.y= 130
        # Connection with characters
        self.luigi = luigi
        self.mario= mario
        self.falling= False
        self.throw= False
        self.row= 0
        self.frozen = False
        #Connection with truck
        self.truck = truck


    def mario_row0(self):
        """Special function for row0, as it acts differently to the rest on
        the conveyors"""
        if self.mario.y != 127 and self.x == 174:
            self.falling = True

    def current_character(self):
        """ This method will help us to know which character should be taken
         into account depending on the row the package is"""
        name = Package.character[self.row]
        if name == "luigi":
            return self.luigi
        else:
            return self.mario

    def move_on_belt(self):
        """ This method moves the package on the conveyor belt on the actual row
        depending on if the row is odd or even"""
        target_x = Package.max_x[self.row]
        if self.row % 2 == 0:
            direction = -1
        else:
            direction= 1
        if direction == -1:
            if self.x > target_x:
                self.x -= 0.5
            else:
                self.x = target_x
        else:
            if self.x < target_x:
                self.x += 0.5
            else:
                self.x = target_x

    def check_catch_or_fall(self):
        """This method helps to chek if the package has reached the desired
        destination in the row where it will decide if the package moves up
        to the next row or if it falls"""
        current_character = self.current_character()
        character_y = Package.check_characters_y[self.row]

        if current_character.y != character_y:
            self.falling = True
        else:
            if self.row < len(Package.row_y) - 1:
                self.row += 1
                self.y = Package.row_y[self.row]
                next_x = Package.next_x[self.row - 1]
                if next_x is not None:
                    self.x = next_x
                self.falling = False
            else:
                # Last row reached
                self.falling = False
                self.throw = True
                # Truck parameters to change image
                new_count = self.truck.current_load + 1
                self.truck.load_package(new_count)

    def update(self):
        """Function to update the package unless the image is frozen due to
        a falling package"""
        if self.frozen or self.throw:
            return
        if self.falling:
            self.y += 2
            return
        #Used to make sure that y correspond to the current row
        self.y = Package.row_y[self.row]
        self.move_on_belt()

        if self.row == 0:
            self.mario_row0()
            if self.falling:
                return

        target_x = Package.max_x[self.row]
        if self.x == target_x:
            self.check_catch_or_fall()

    def draw(self):
        """Function to draw the packages depending on
        the row they are (even or odd is a change on the image)"""
        # Special row 0, with different imaging to the rest
        if self.row == 0:
            if not self.falling:
                if self.x >= 176:
                    pyxel.blt(self.x, self.y, Package.img, Package.u,
                              Package.v,
                              Package.package_width, Package.package_height)
                if 120 <= self.x <= 136:
                    pyxel.blt(self.x, self.y, Package.img, Package.u,
                              Package.v,
                              Package.package_width, Package.package_height)
                elif 68 < self.x <= 96:
                    pyxel.blt(self.x, self.y, Package.img, 51,
                              21,
                              Package.package_width, Package.package_height)
            else:
                if self.x < 120:
                    pyxel.blt(64, 132, Package.img, 64,
                              16,
                              11, 14)
                    pyxel.blt(64, 147, Package.img, 65, 166, 13, 10)
                elif self.x > 120:
                    pyxel.blt(164, 134, Package.img, 65, 166, 13, 10)


        # Rest of the conveyors. Not hard coding as we did not find a way to
        # make it continuous change in imaging and position without if and
        # else functions.
        elif self.row == 1:
            if self.x <= 96 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          21,
                          Package.package_width, Package.package_height)
            elif 114 < self.x < 144 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          36,
                          Package.package_width, Package.package_height + 1)
            elif self.falling:
                pyxel.blt(152, 120, Package.img, 64,
                          32,
                          11, 14)
                pyxel.blt(152, 134, Package.img, 65, 166, 13, 10)

        elif self.row == 2:
            if self.x >= 120 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          36,
                          Package.package_width, Package.package_height + 1)
            elif 68 < self.x <= 96 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          52,
                          Package.package_width, Package.package_height + 1)
            elif self.falling:
                pyxel.blt(64, 132, Package.img, 64,
                          48,
                          11, 14)
                pyxel.blt(64, 147, Package.img, 65, 166, 13, 10)

        elif self.row == 3:
            if self.x <= 96 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          52,
                          Package.package_width, Package.package_height + 1)
            elif 114 < self.x < 144 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          68,
                          Package.package_width,
                          Package.package_height + 1)
            elif self.falling:
                pyxel.blt(152, 120, Package.img, 64,
                          64,
                          11, 14)
                pyxel.blt(152, 134, Package.img, 65, 166, 13, 10)

        elif self.row == 4:
            if self.x >= 120 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          68,
                          Package.package_width, Package.package_height + 1)
            elif 68 < self.x <= 96 and not self.falling:
                pyxel.blt(self.x, self.y, Package.img, 51,
                          84,
                          Package.package_width, Package.package_height + 1)
            elif self.falling:
                pyxel.blt(64, 132, Package.img, 64,
                          80,
                          11, 14)
                pyxel.blt(64, 147, Package.img, 65, 166, 13, 10)
            elif self.throw:
                pyxel.blt(36, 64, Package.img, 64,
                          114,
                          11, 14)
