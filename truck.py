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

    #def check_package(selfself, package_x, package_y, package_w, package_h):


    def draw(self):
        pyxel.blt(self.x, self.y, Truck.img, Truck.u,
                  Truck.v,
                  Truck.truck_width, Truck.truck_height)

    """Tenemos que haacer este condicional cuando sepamos como meter los 
    paquetes"""
    #def image(self, int):
    #    if package == 0:
    #        self.image = "Insert image without package"
    #    elif package == 1:
    #        self.image = "image2"
    #    elif package == 2:
    #        self.image = "image3"
    #    elif package == 3:
    #        self.image = "image4"
    #    elif  package == 4:
    #        self.image = "image5"
    #    elif package == 5:
    #        self.image = "image6"
    #   elif package == 6:
    #       self.image = "image7"
    #    elif package == 7:
    #        self.image = "image8"
    #    elif package == 8:
    #        self.image = "Insert image without package"


