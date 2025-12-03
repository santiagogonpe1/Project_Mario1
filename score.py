import pyxel

class Score:
    x= 200
    y= 48
    img= 1
    u= 34
    score_width= 4
    score_height= 8


    def __init__(self):
        self.mario= None
        self.luigi= None
        self.truck= None
        self.points= 0
        self.num3= 0
        self.num2= 0
        self.num1= 0
        self.last_catch_mario = False
        self.last_catch_luigi = False
        self.last_truck_full = False


    def update(self):
        """This method will update the points when mario or luigi catch a
        package or when the truck is full"""
        if self.mario.catch and not self.last_catch_mario:
            self.points+= 1
        if self.luigi.catch and not self.last_catch_luigi:
            self.points+= 1
        #These variables store the state of the previous frame so you can
        #detect the change in the events and don´t repeat them.
        self.last_catch_mario = self.mario.catch
        self.last_catch_luigi = self.luigi.catch

        if self.truck.full and not self.last_truck_full:
            self.points+= 10

        self.last_truck_full = self.truck.full


    def show_score(self):
        num3 = (self.points // 100) % 10
        num2 = (self.points // 10) % 10
        num1 = self.points % 10

        self.num3= num3
        self.num2= num2
        self.num1= num1


    def draw(self):
        """This method draws the score and uses the attributes of self.num
        to change the "v" of each number when a point is added"""
        self.show_score()

        pyxel.blt(Score.x, Score.y, Score.img, Score.u, self.num3 *
                  Score.score_height,
                    Score.score_width, Score.score_height)
        pyxel.blt(Score.x + 6, Score.y, Score.img, Score.u, self.num2 *
                  Score.score_height,
                  Score.score_width, Score.score_height)
        pyxel.blt(Score.x + 12, Score.y, Score.img, Score.u, self.num1 *
                  Score.score_height,
                    Score.score_width, Score.score_height)