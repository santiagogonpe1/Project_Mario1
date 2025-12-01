import pyxel

class Truck:
    img = 0
    u = 80
    v = 0
    truck_width = 32
    truck_height = 16
    DX = 1

    def __init__(self):
        self.x= 13
        self.y= 88
        self.truck= Truck
        self.has_package = False
        self.num_package = 0
        self.current_load = 0
        self.max_capacity = 9

    def load_package(self, num_package):
        self.current_load = min(num_package, self.max_capacity)
        self.draw()


    def draw(self):
        if self.current_load == 0:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v,
                      Truck.truck_width, Truck.truck_height)
        elif self.current_load == 1:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 2:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*2, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 3:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*3, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 4:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*4, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 5:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*5, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 6:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*6, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 7:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*7, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 8:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16*8, Truck.truck_width, Truck.truck_height)



