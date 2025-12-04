import pyxel

class Score:
    x= 200
    y= 48
    img= 1
    u= 34
    score_width= 4
    score_height= 8


    def __init__(self):
        #Connection with mario, luigi and the truck
        self.__mario= None
        self.__luigi= None
        self.__truck= None
        #Atributes to count points
        self.__points= 0
        self.__num3= 0
        self.__num2= 0
        self.__num1= 0
        #Attributes to store the state of the previous frame so you can
        #detect the change in the events and don´t repeat them.
        self.__last_catch_mario = False
        self.__last_catch_luigi = False
        self.__last_truck_full = False

    @property
    def mario(self):
        return self.__mario
    @mario.setter
    def mario(self, value):
        self.__mario = value

    @property
    def luigi(self):
        return self.__luigi
    @luigi.setter
    def luigi(self, value):
        self.__luigi = value

    @property
    def truck(self):
        return self.__truck
    @truck.setter
    def truck(self, value):
        self.__truck = value

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, value):
        if isinstance(value, int):
            self.__points = value

    @property
    def num1(self):
        return self.__num1
    @num1.setter
    def num1(self, value):
        if isinstance(value, int):
            self.__num1 = value

    @property
    def num2(self):
        return self.__num2
    @num2.setter
    def num2(self, value):
        if isinstance(value, int):
            self.__num2 = value

    @property
    def num3(self):
        return self.__num3
    @num3.setter
    def num3(self, value):
        if isinstance(value, int):
            self.__num3 = value

    @property
    def last_catch_mario(self):
        return self.__last_catch_mario
    @last_catch_mario.setter
    def last_catch_mario(self, value):
        if isinstance(value, bool):
            self.__last_catch_mario = value

    @property
    def last_catch_luigi(self):
        return self.__last_catch_luigi
    @last_catch_luigi.setter
    def last_catch_luigi(self, value):
        if isinstance(value, bool):
            self.__last_catch_luigi = value

    @property
    def last_truck_full(self):
        return self.__last_truck_full
    @last_truck_full.setter
    def last_truck_full(self, value):
        if isinstance(value, bool):
            self.__last_truck_full = value

    def update(self):
        """This method will update the points when mario or luigi catch a
        package or when the truck is full"""
        if self.__mario.catch and not self.__last_catch_mario:
            self.__points+= 1
        if self.__luigi.catch and not self.__last_catch_luigi:
            self.__points+= 1

        self.__last_catch_mario = self.__mario.catch
        self.__last_catch_luigi = self.__luigi.catch

        if self.__truck.full and not self.__last_truck_full:
            self.__points+= 10

        self.__last_truck_full = self.__truck.full


    def show_score(self):
        """This method updates num1, num2 and num3 used for drawing
        the score on screen. It converts the total points into individual
        digits so that each one can be shown separately by the draw
        method."""
        num3 = (self.__points // 100) % 10
        num2 = (self.__points // 10) % 10
        num1 = self.__points % 10

        self.__num3= num3
        self.__num2= num2
        self.__num1= num1


    def draw(self):
        """This method draws the score and uses the attributes of self.num
        to change the "v" of each number when a point is added"""
        self.show_score()

        pyxel.blt(Score.x, Score.y, Score.img, Score.u, self.__num3 *
                  Score.score_height,
                    Score.score_width, Score.score_height)
        pyxel.blt(Score.x + 6, Score.y, Score.img, Score.u, self.__num2 *
                  Score.score_height,
                  Score.score_width, Score.score_height)
        pyxel.blt(Score.x + 12, Score.y, Score.img, Score.u, self.__num1 *
                  Score.score_height,
                    Score.score_width, Score.score_height)
