import pyxel

class Truck:
    img = 0
    u = 80
    v = 0
    truck_width = 32
    truck_height = 16
    DX = 1

    def __init__(self):
        """Parameters needed to initialize a truck"""
        self.x= 13
        self.y= 88
        self.truck= Truck
        self.has_package = False
        self.num_package = 0
        self.current_load = 0
        self.max_capacity = 8

    def load_package(self, new_count):
        """Set a maximum number of possible packages into the truck
         and a counter for each one of them."""
        self.current_load = min(new_count, self.max_capacity)

    def draw(self):
        """Function to draw the truck, tried to optimize at most the coding,
         but animation is needed"""
        if self.current_load == 0:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v,
                      Truck.truck_width, Truck.truck_height)
        elif self.current_load == 1:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + 16, Truck.truck_width, Truck.truck_height)
        elif self.current_load == 2:
            pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                      Truck.v + (16*2), Truck.truck_width, Truck.truck_height)
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



