import pyxel

class Boss:
    img= 0
    boss_width= 12
    boss_height= 14
    door_width= 10
    door_height= 16
    failures_face_width= 16
    failures_face_height= 16

    def __init__(self):
        # Determine the character to punish
        self.boss_luigi= False
        self.boss_mario= False
        self.last_fail = None
        # State when the animation for punishment starts to freeze game
        self.animation_running = False
        self.animation_timer = 0
        #Game stats
        self.max_lives = 3
        self.lives_lost= 0
        self.packages_thrown = 0
        #Reference for packages
        self.package = []

    def handle_package_resolution(self, package_obj, is_success):
        """
        Called by App when a single package is completed (thrown or fallen).
        This method updates the lives lost and animation status.
        """
        if not is_success:
            # Package fell, lose a life
            # Doing it on main file may be easier
            #self.lives_lost += 1
            #if self.lives_lost == self.max_lives:
            #    self.mainFile.game_over = True



            # Determine which side the package fell to set the door flag
            # Note: We rely on the package's final fall position (x) for this
            if package_obj.x < 100:
                self.last_fail = "luigi"
                self.boss_luigi = True
                self.boss_mario = False
            elif package_obj.x > 100:
                self.last_fail = "mario"
                self.boss_mario = True
                self.boss_luigi = False
        else:
            # Package was successfully thrown and keep parameters
            self.packages_thrown += 1
            self.boss_mario = False
            self.boss_luigi = False

    def start_animation(self):
        """Start punishment animation for 5 seconds"""
        self.animation_running = True
        self.animation_timer = 300

    def end_animation(self):
        """Resets all parameters when animation ends"""
        self.animation_running = False
        self.boss_mario = False
        self.boss_luigi = False
        self.animation_timer = 0
        self.last_fail = None

    def update(self):
        """Handles state changes and time decrements."""
        if self.animation_timer > 0:
            self.animation_timer -= 1
        else:
            self.end_animation()

    def draw(self):
        """Draws all the boss animation along with door"""
        #Mario door
        if self.boss_mario and self.animation_running:
            pyxel.blt(227, 96, 1, 51, 104, Boss.door_width, Boss.door_height)
        else:
            pyxel.blt(227,96,1,16,104,Boss.door_width,Boss.door_height)
        #Luigi door
        if self.boss_luigi and self.animation_running:
            pyxel.blt(3, 128, 1, 35, 104, Boss.door_width, Boss.door_height)
        else:
            pyxel.blt(3,128,1,35,88,Boss.door_width, Boss.door_height)

        falling = None
        for p in self.package:
            if p.falling:
                falling = p

        if self.animation_running and self.last_fail:
            #for luigi
            pyxel.blt(8, 8,1,40,0,Boss.failures_face_width,
                      Boss.failures_face_height)
            if self.last_fail == "luigi":
                if (pyxel.frame_count // 6) % 2 == 0:
                    pyxel.blt(14,130, Boss.img, 35, 3, Boss.boss_width,
                              Boss.boss_height)
                else:
                    pyxel.blt(14, 130, Boss.img, 35, 18, Boss.boss_width,
                              Boss.boss_height)
            #for mario
            elif self.last_fail == "mario":
                if (pyxel.frame_count // 6) % 2 == 0:
                    pyxel.blt(212, 98, Boss.img, 33, 35, Boss.boss_width,
                              Boss.boss_height)
                else:
                    pyxel.blt(212, 98, Boss.img, 33, 50, Boss.boss_width,
                              Boss.boss_height)
            elif falling.x == 174:
                if (pyxel.frame_count // 6) % 2 == 0:
                    pyxel.blt(212, 98, Boss.img, 33, 35, Boss.boss_width,
                              Boss.boss_height)
                else:
                    pyxel.blt(212, 98, Boss.img, 33, 50, Boss.boss_width,
                              Boss.boss_height)