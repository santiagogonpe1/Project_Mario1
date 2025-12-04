#To open the sprites: pyxel edit assets/sprites2.pyxres


import pyxel

#Import all game objects
from mario import Mario
from luigi import Luigi
from truck import Truck
from score import Score
from package import Package
from boss import Boss

class App:
    def __init__(self):
        """Initialize all attributes"""
        pyxel.init(240, 160)
        pyxel.load("assets/sprites.pyxres")
        self.mario = Mario()
        self.luigi = Luigi()
        self.truck = Truck()
        self.package = []
        self.boss = Boss()
        self.score = Score()
        # Connection with package and characters
        self.mario.package = self.package
        self.luigi.package = self.package
        # Parameters for package spam
        self.max_package_batch = 1
        self.batch_count = 0
        self.spawn_interval = 200
        self.wait_time = 0
        self.spawning = True
        # Connection with the packages
        self.boss.package = self.package
        # Connection with the boss
        self.luigi.boss = self.boss
        self.mario.boss = self.boss
        # Connection with the truck
        self.truck.package = self.package
        self.mario.truck = self.truck
        self.luigi.truck = self.truck
        # Connection with the score
        self.score.mario = self.mario
        self.score.luigi = self.luigi
        self.score.truck = self.truck
        # Freezing parameters
        self.freeze = False
        self.freeze_timer = 0
        # Lives on-game
        self.max_lives = 3
        self.lives_lost = 0
        self.last_fail = False
        self.game_over = False
        self.game_start= False

        pyxel.run(self.update, self.draw)

    def update(self):
        """Develops different actions, multiple packages, fps count and
        initializes or finishes game"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #Start game update in game
        if not self.game_start:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.game_start = True
            return
        #Game over updated in game
        if self.game_over:
            # Allows restart when pressing space
                if pyxel.btnp(pyxel.KEY_R):
                    self.reset_game()
                if pyxel.btnp(pyxel.KEY_Q):
                    pyxel.quit()
                return

        # The game is frozen if player misses a package (stop update)
        if self.freeze:
            # During freeze time, boss still animated
            self.boss.update()
            if self.freeze_timer > 0:
                self.freeze_timer -= 1
            else:
                if self.last_fail:
                    self.game_over = True
                    self.last_fail = False
                else:
                    self.unfreeze_game()
            return

        self.mario.update()
        self.luigi.update()
        #Package spawning
        if self.spawning:
            if self.batch_count < self.max_package_batch:
                if pyxel.frame_count % self.spawn_interval == 0:
                    self.spawn_package()
            else:
                self.spawning = False
                self.wait_time = 300
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
            # Boolean variables: finished to see if the package is ready to
            # be removed and successful if it was thrown successfully
            package_resolved = False

            if package.falling and package.y > 150:
                life_lost = self.boss.handle_package_resolution(package,
                                                                is_success=False)
                if life_lost:
                    self.lives_lost += 1
                    if self.lives_lost >= self.max_lives:
                        self.last_fail = True
                    # If game is not over, freeze game and start animation
                    self.freeze_game()
                package_resolved = True
            #Package thrown into the truck: spawn more packages and notify boss
            elif package.throw:
                self.boss.handle_package_resolution(package, is_success=True)
                package_resolved = True
            # Package still in game
            if not package_resolved:
                updated_packages.append(package)

        self.package[:] = updated_packages
        self.truck.update()
        #The game will be frozen when the truck is full
        if self.truck.full and not self.freeze:
            self.freeze_truck()

        self.score.update()

    def draw(self):
        """Draws the initial and final interfaces, and the game itself"""
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,240,160)

        #Draw the game start
        if not self.game_start:
            pyxel.cls(5)
            pyxel.text(80, 30, "SUPER MARIO BROS", 7)
            if (pyxel.frame_count // 8) % 2 == 0:
                pyxel.text(75, 45, "Press return to start", 7)
            else:
                pyxel.text(75, 45, "Press return to start", 5)
            pyxel.text(20, 85, "Luigi:", 7)
            pyxel.text(20, 95, "W -> UP", 7)
            pyxel.text(20, 105, "S -> DOWN", 7)
            pyxel.text(160, 85, "Mario:", 7)
            pyxel.text(160, 95, " Up Arrow -> UP", 7)
            pyxel.text(160, 105, "Down Arrow -> DOWN", 7)
            return

        # Draw of game over
        if self.game_over:
            pyxel.cls(5)
            pyxel.text(90, 40, "GAME OVER", 7)
            pyxel.text(81, 65, f"Final score: {self.score.points}", 7)
            pyxel.text(85, 90, "R - RESTART", 7)
            pyxel.text(90, 105, "Q - QUIT", 7)
            return
        self.mario.draw()
        self.luigi.draw()
        self.truck.draw()
        for crying_faces in range(self.lives_lost):
            x_position = 8 + (crying_faces * 18)
            pyxel.blt(x_position, 8, 1, 40, 0, 16, 16)
        for package in self.package:
            package.draw()
        self.boss.draw()
        self.score.draw()

    def reset_game(self):
        """This function resets the game if user press R"""
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
        if self.truck.full:
            self.truck.full = False
            self.truck.current_load = 0

    def freeze_truck(self):
        """ This method will help us to then freeze the game when the truck is
        full"""
        self.freeze = True
        self.freeze_timer = 180
        self.mario.frozen = True
        self.luigi.frozen = True
        # freeze packages (assuming Package respects p.frozen)
        for p in self.package:
            p.frozen = True

        self.boss.start_rest(self.freeze_timer)


App()
