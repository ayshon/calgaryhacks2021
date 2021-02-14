import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="Evening", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/sunset.png")
        
        pyxel.mouse(True)

        self.option1 = Option(2,232,5,6)
        self.option2 = Option(2,240,5,6)
        self.option3 = Option(2,248,5,6)

        self.gender_option_m = Option(2, 200, 5, 12)
        self.gender_option_f = Option(102,200,5,12)
        
        self.gender = 0

        self.name = ""

        self.scene = [0,1,2]
        self.active_scene = 1

        # self.testNum = 0

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.active_scene == 1:
            pyxel.image(0).load(0, 0, "assets/choose gender.jpg")
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if(pyxel.mouse_x > self.gender_option_m.x and pyxel.mouse_x < (self.gender_option_m.x + self.gender_option_m.side) and pyxel.mouse_y > self.gender_option_m.y and pyxel.mouse_y < (self.gender_option_m.y + self.gender_option_m.side)):
                    if(self.gender_option_m.color == 12):
                        if(self.gender_option_f.color == 0):
                            self.gender_option_f.color = 12
                        self.gender_option_m.color = 0
                        self.gender = 2
                if(pyxel.mouse_x > self.gender_option_f.x and pyxel.mouse_x < (self.gender_option_f.x + self.gender_option_f.side) and pyxel.mouse_y > self.gender_option_f.y and pyxel.mouse_y < (self.gender_option_f.y + self.gender_option_f.side)):
                    if(self.gender_option_f.color == 12):
                        if(self.gender_option_m.color == 0):
                            self.gender_option_m.color = 12
                        self.gender_option_f.color = 0
                        self.gender = 1
            if((self.gender == 1 or self.gender == 2) and pyxel.btnp(pyxel.KEY_ENTER)):
                self.active_scene = 2
        elif self.active_scene == 2:
            pyxel.image(0).load(0, 0, "assets/forest.png")
            if pyxel.btnp(pyxel.KEY_BACKSPACE) and self.name != "":
                    self.name = self.name[:-1]
            if len(self.name) < 15:
                if pyxel.btnp(pyxel.KEY_A):
                    self.name += 'A'
                if pyxel.btnp(pyxel.KEY_B):
                    self.name += 'B'
                if pyxel.btnp(pyxel.KEY_C):
                    self.name += 'C'
                if pyxel.btnp(pyxel.KEY_D):
                    self.name += 'D'
                if pyxel.btnp(pyxel.KEY_E):
                    self.name += 'E'
                if pyxel.btnp(pyxel.KEY_F):
                    self.name += 'F'
                if pyxel.btnp(pyxel.KEY_G):
                    self.name += 'G'
                if pyxel.btnp(pyxel.KEY_H):
                    self.name += 'H'
                if pyxel.btnp(pyxel.KEY_I):
                    self.name += 'I'
                if pyxel.btnp(pyxel.KEY_J):
                    self.name += 'J'
                if pyxel.btnp(pyxel.KEY_K):
                    self.name += 'K'
                if pyxel.btnp(pyxel.KEY_L):
                    self.name += 'L'
                if pyxel.btnp(pyxel.KEY_M):
                    self.name += 'M'
                if pyxel.btnp(pyxel.KEY_N):
                    self.name += 'N'
                if pyxel.btnp(pyxel.KEY_O):
                    self.name += 'O'
                if pyxel.btnp(pyxel.KEY_P):
                    self.name += 'P'
                if pyxel.btnp(pyxel.KEY_Q):
                    self.name += 'Q'
                if pyxel.btnp(pyxel.KEY_R):
                    self.name += 'R'
                if pyxel.btnp(pyxel.KEY_S):
                    self.name += 'S'
                if pyxel.btnp(pyxel.KEY_T):
                    self.name += 'T'
                if pyxel.btnp(pyxel.KEY_U):
                    self.name += 'U'
                if pyxel.btnp(pyxel.KEY_V):
                    self.name += 'V'
                if pyxel.btnp(pyxel.KEY_W):
                    self.name += 'W'
                if pyxel.btnp(pyxel.KEY_X):
                    self.name += 'X'
                if pyxel.btnp(pyxel.KEY_Y):
                    self.name += 'Y'
                if pyxel.btnp(pyxel.KEY_Z):
                    self.name += 'Z'
                if pyxel.btnp(pyxel.KEY_SPACE):
                    self.name += ' '
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 3
                pyxel.image(0).load(0, 0, "assets/lake.png")
        elif self.active_scene == 3:
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if(pyxel.mouse_x > self.option1.x and pyxel.mouse_x < (self.option1.x + self.option1.side) and pyxel.mouse_y > self.option1.y and pyxel.mouse_y < (self.option1.y + self.option1.side)):
                    if(self.option1.color == 6):
                        self.option1.color = 0
                        pyxel.image(0).load(0, 0, "assets/forest.png")
                    else:
                        self.option1.color = 6
                        pyxel.image(0).load(0, 0, "assets/sunset.png")
                if(pyxel.mouse_x > self.option2.x and pyxel.mouse_x < (self.option2.x + self.option2.side) and pyxel.mouse_y > self.option2.y and pyxel.mouse_y < (self.option2.y + self.option2.side)):
                    if(self.option2.color == 6):
                        self.option2.color = 0
                        pyxel.image(0).load(0, 0, "assets/lake.png")
                    else:
                        self.option2.color = 6
                        pyxel.image(0).load(0, 0, "assets/sunset.png")
                if(pyxel.mouse_x > self.option3.x and pyxel.mouse_x < (self.option3.x + self.option3.side) and pyxel.mouse_y > self.option3.y and pyxel.mouse_y < (self.option3.y + self.option3.side)):
                    if(self.option3.color == 6):
                        self.option3.color = 0
                    else:
                        self.option3.color = 6

    def draw(self):
        # CLEAR SCREEN
        pyxel.cls(0)

        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)

        # # testing draw rectanlge 
        # if self.testNum == 1:
        #     pyxel.rect(60, 10, 100, 70, 0)

        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        if self.active_scene != 2:
            pyxel.rect(0, 180, 256, 76, 0)

        # GENDER OPTIONS
        if(self.active_scene == 1):
            self.draw_gender_options()
            
        #  ENTER NAME
        if(self.active_scene ==2):
            self.draw_name()

        # OPTIONS
        elif(self.active_scene != 1):
            self.draw_options()
        
    def draw_gender_options(self):
        # TEXT
        pyxel.text(2, 182, "Choose your gender", 3)

        # OPTIONS
        pyxel.rect(self.gender_option_m.x, self.gender_option_m.y, self.gender_option_m.side, self.gender_option_m.side, self.gender_option_m.color)
        pyxel.text(10, self.gender_option_m.y, "Male", 2)
        pyxel.rect(self.gender_option_f.x, self.gender_option_f.y, self.gender_option_f.side, self.gender_option_f.side, self.gender_option_f.color)
        pyxel.text(110, self.gender_option_f.y, "Female", 8)

        if (self.gender == 1):
            pyxel.text(96, 232, "You are female.", 8)
        elif (self.gender == 2): 
            pyxel.text(96, 232, "You are male.", 2)

    def draw_name(self):
        pyxel.rect(60, 102, 137, 70, 0)
        pyxel.text(95, 118, "Type in your name", 7)
        pyxel.text(100, 130, self.name, 7)
        nameLength = len(self.name)
        underScores = ""
        for i in range(15):
                underScores += "_"
        pyxel.text(100, 132, underScores, 7)
        pyxel.text(85, 150, "Press ENTER to confirm", 7)

    def draw_options(self):
        pyxel.text(2, 182, "There is text here gotem", 1)
        pyxel.text(2, 189, "There is text here too very cool stuff very nice", 2)

        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option1.y, "This is option 1", 3)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(10, self.option2.y, "This is option 2", 4)
        pyxel.rect(self.option3.x, self.option3.y, self.option3.side, self.option3.side, self.option3.color)
        pyxel.text(10, self.option3.y, "This is option 3", 5)

App()