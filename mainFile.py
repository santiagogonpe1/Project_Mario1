#To open the sprites: pyxel edit assets/sprites2.pyxres


# Arreglar bug de Mario cuando cae paquete y el esta por encima.
# Comentar codigo

import pyxel

from mario import Mario
from luigi import Luigi
from truck import Truck
from package import Package
#from score import Score
from boss import Boss

class App:
    def __init__(self):
        pyxel.init(240,160)
        pyxel.load("assets/sprites2.pyxres")
        self.mario= Mario()
        self.luigi= Luigi()
        self.truck= Truck()
        self.package= []
        self.mario.package = self.package
        self.luigi.package = self.package

        self.max_package_batch = 3
        self.batch_count = 0
        self.spawn_interval = 60
        self.wait_time = 0
        self.spawning = True
        self.boss= Boss()
        #self.score= Score()
        #Connection with the packages
        self.boss.package= self.package
        #Connection with the boss
        self.luigi.boss= self.boss
        self.mario.boss= self.boss
        #Comnnection with Truck
        self.truck.package = self.package


        # Freezing parameters
        self.freeze = False
        self.freeze_timer = 0


        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # For the timer to work, boss must be updating at all times
        self.boss.update()

        if self.freeze:
            if self.freeze_timer > 0:
                self.freeze_timer -=1
            else:
                self.unfreeze_game()
            self.boss.update()
            return

        self.mario.update()
        self.luigi.update()
        if self.spawning:
            if self.batch_count < self.max_package_batch:
                if pyxel.frame_count % self.spawn_interval == 0:
                    self.spawn_package()
            else:
                self.spawning = False
                self.wait_time = 6000
        else:
            if self.wait_time > 0:
                self.wait_time -= 1
            else:
                self.spawning = True
                self.batch_count = 0

        updated_packages = []
        for package in self.package:
            package.update()

            # Boolean variables: finished to see if the package is ready to
            # be removed and successful if it was thrown successfully

            package_resolved = False

            if package.falling and package.y > 150:
                self.boss.handle_package_resolution(package, is_success=False)
                self.freeze_game()
                package_resolved = True
            elif package.throw:
                self.boss.handle_package_resolution(package, is_success=True)
                package_resolved = True
                self.spawn_package()
            if not package_resolved:
                updated_packages.append(package)

        self.package = updated_packages

        #self.score.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,240,160)
        self.mario.draw()
        self.luigi.draw()
        self.truck.draw()
        for package in self.package:
            package.draw()
        self.boss.draw()
        #self.score.draw()

    def spawn_package(self):
        new_package = Package(self.luigi, self.mario, self.truck)
        self.package.append(new_package)
        self.batch_count += 1

    def freeze_game(self):
        self.freeze = True
        self.freeze_timer = 180
        self.mario.frozen = True
        self.luigi.frozen = True
        if self.boss.last_fail == "mario":
            self.mario.y = 500
        else:
            self.luigi.y = 500

        for p in self.package:
            p.frozen = True
        self.boss.start_animation()

    def unfreeze_game(self):
        self.freeze = False
        self.mario.frozen = False
        self.luigi.frozen = False
        self.mario.y = 127
        self.luigi.y = 64
        self.spawning = True
        self.batch_count = 0
        self.package.clear()
        self.boss.end_animation()

App()

