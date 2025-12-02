#To open the sprites: pyxel edit assets/sprites2.pyxres

import pyxel

#Import all game objects
from mario import Mario
from luigi import Luigi
from truck import Truck
from package import Package
#from score import Score
from boss import Boss

class App:
    def __init__(self):
        """Initialize all attributes"""
        pyxel.init(240,160)
        pyxel.load("assets/sprites2.pyxres")
        self.mario= Mario()
        self.luigi= Luigi()
        self.truck= Truck()
        self.boss = Boss(self)
        self.package= []
        #Connection with package and characters
        self.mario.package = self.package
        self.luigi.package = self.package
        # Parameters for package spam
        self.max_package_batch = 3
        self.batch_count = 0
        self.spawn_interval = 60
        self.wait_time = 0
        self.spawning = True
        #self.score= Score()
        #Connection with the packages
        self.boss.package= self.package
        #Connection with the boss
        self.luigi.boss= self.boss
        self.mario.boss= self.boss
        #Connection with Truck
        self.truck.package = self.package
        # Freezing parameters
        self.freeze = False
        self.freeze_timer = 0
        # Lives on-game
        self.max_lives = 3
        self.lives_lost = 0
        self.last_fail = False
        self.game_over = False


        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #Game over update in game
        if self.game_over:
            # Allows restart when pressing space
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.reset_game()
            return

        #The game is frozen if player misses a package (stop update)
        if self.freeze:
            #During freeze time, boss still animated
            self.boss.update()
            if self.freeze_timer > 0:
                self.freeze_timer -=1
            else:
                if self.last_fail:
                    self.game_over = True
                    self.last_fail = False
                else:
                    self.unfreeze_game()
            return

        #Basic updates for gameplay
        self.mario.update()
        self.luigi.update()

        #Package spawning
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

        #Package management loop
        updated_packages = []
        for package in self.package:
            package.update()
            # finished to see if the package is ready to be removed and
            # successful if it was thrown successfully
            package_resolved = False

            # If package falls: Boss animation, life lost and freeze gameplay
            if package.falling and package.y > 150:
                life_lost = self.boss.handle_package_resolution(package,
                                                                is_success=False)
                if life_lost:
                    self.lives_lost += 1
                    if self.lives_lost >= self.max_lives:
                        self.last_fail = True
                    #If game is not over, freeze game and start animation
                    self.freeze_game()
                package_resolved = True

            #Package thrown into the truck: spawn more packages and notify boss
            elif package.throw:
                self.boss.handle_package_resolution(package, is_success=True)
                package_resolved = True
                self.spawn_package()
            # Package still in game
            if not package_resolved:
                updated_packages.append(package)

        self.package = updated_packages

        #self.score.update()

    def draw(self):
        """This function draws all the objects for the game to be playable
        and enjoyable"""
        pyxel.cls(0)
        # Draw of game over
        if self.game_over:
            pyxel.bltm(0,0,0,0,256,240,160)
            return
        pyxel.bltm(0,0,0,0,0,240,160)
        if self.game_over:
            self.freeze_game()
            pyxel.bltm(0,0,0,0,256,240,160)
            return
        self.mario.draw()
        self.luigi.draw()
        self.truck.draw()
        # Draw crying faces if there is a live lost
        for crying_faces in range(self.lives_lost):
            x_position = 8 + (crying_faces * 18)
            pyxel.blt(x_position, 8, 1, 40, 0, 16,16)
        # Draw packages
        for package in self.package:
            package.draw()
        self.boss.draw()
        #self.score.draw()

    def reset_game(self):
        """This function resets the game if user press SPACE"""
        self.last_fail = False
        self.game_over = False
        self.lives_lost = 0
        self.boss.packages_thrown = 0
        self.truck.current_load = 0
        self.unfreeze_game()

    def spawn_package(self):
        """Creates the package and ands it to the list of package"""
        new_package = Package(self.luigi, self.mario, self.truck)
        self.package.append(new_package)
        self.batch_count += 1

    def freeze_game(self):
        """Pauses the gameplay, setting up the boss animation"""
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
        """Resets the gameplay after the boss animation"""
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

