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

        # SCENE ORGANIZATION
        self.scene = [0,1,2]
        # 0 - TITLE
        # 1 - GENDER CHOICE, 
        # 2 - ENTER NAME,
        # 3 - STORE
        # 4 - Travelling Days
        self.active_scene = 1 

        self.option1 = Option(2,232,5,6)
        self.option2 = Option(2,240,5,6)
        self.option3 = Option(2,248,5,6)

        # CHOOSE YOUR GENDER
        self.gender_option_m = Option(2, 200, 5, 12)
        self.gender_option_f = Option(202,200,5,12)
        self.gender_option_b = Option(102,200,5,12)
        self.gender = 0

        # ENETER NAME
        self.name = ""
        
        # GENERAL STORE SCENE
        self.cart = [[],[]]
        self.cash = 100
        self.option1_g = Option(2,200,5,7)
        self.option2_g = Option(2,210,5,7)
        self.option3_g = Option(2,220,5,7)
        self.option4_g = Option(2,230,5,7)
        self.option_highlight = 0
        self.storeText = 0
        self.cartText = 0

        # TRAVELLING DAYS
        self.option1_t = Option(2,232,5,6)
        self.option2_t = Option(2,240,5,6)
        self.option3_t = Option(2,248,5,6)
        self.day_state =1 #1 for morning, #2 for afternoon, #3 for evening 
        self.choice = 1 #1 for new state, #2 for lost, #3 for camp
        self.previous_state = 1

        self.option_t_highlight = 0

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
####### CHOOSE YOUR GENDER #######
        if self.active_scene == 1:
            pyxel.image(0).load(0, 0, "assets/choose gender.jpg")
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                
                # MALE
                if(pyxel.mouse_x > self.gender_option_m.x and pyxel.mouse_x < (self.gender_option_m.x + self.gender_option_m.side) and pyxel.mouse_y > self.gender_option_m.y and pyxel.mouse_y < (self.gender_option_m.y + self.gender_option_m.side)):
                    if(self.gender_option_m.color == 12):
                        # if(self.gender_option_f.color == 0 and self.gender_option_b == 0):
                        self.gender_option_f.color = 12
                        self.gender_option_b.color = 12
                        #^shift tab

                        self.gender_option_m.color = 10
                        self.gender = 2
                
                # FEMALE
                if(pyxel.mouse_x > self.gender_option_f.x and pyxel.mouse_x < (self.gender_option_f.x + self.gender_option_f.side) and pyxel.mouse_y > self.gender_option_f.y and pyxel.mouse_y < (self.gender_option_f.y + self.gender_option_f.side)):
                    if(self.gender_option_f.color == 12):
                        # if(self.gender_option_m.color == 0 and self.gender_option_b == 0):
                        self.gender_option_m.color = 12
                        self.gender_option_b.color = 12
                        self.gender_option_f.color = 10
                        self.gender = 1

                # NON-BINARY
                if(pyxel.mouse_x > self.gender_option_b.x and pyxel.mouse_x < (self.gender_option_b.x + self.gender_option_b.side) and pyxel.mouse_y > self.gender_option_b.y and pyxel.mouse_y < (self.gender_option_b.y + self.gender_option_b.side)):
                    if(self.gender_option_b.color == 12):
                        # if(self.gender_option_m.color == 0 and self.gender_option_f.color == 0):
                        self.gender_option_m.color = 12
                        self.gender_option_f.color = 12
                        self.gender_option_b.color = 10
                        self.gender = 3

            if((self.gender == 1 or self.gender == 2 or self.gender == 3) and pyxel.btnp(pyxel.KEY_ENTER)):
                self.active_scene = 2
        
########### ENTER NAME ##########
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
        
########### STORE ##########
        elif self.active_scene == 3:
            pyxel.image(0).load(0, 0, "assets/store.jpg")
            if pyxel.btnp(pyxel.KEY_R):
                self.storeText = 0
                self.cartText = 0
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.storeText = 0
                self.active_scene = 4
                #TRAVELLING NEW PHOTO. PUT IN SCENE BEFORE TRAVELING SCENES
                pyxel.image(0).load(0, 0, "assets/morning.jpg")
                #TRANSITION HERE
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                if(pyxel.mouse_x > self.option1_g.x and pyxel.mouse_x < (self.option1_g.x + self.option1_g.side) and pyxel.mouse_y > self.option1_g.y and pyxel.mouse_y < (self.option1_g.y + self.option1_g.side)):
                    if(self.storeText == 1):
                        self.cash -= 2
                        if("Maple Syrup" not in self.cart[0]):
                            self.cart[0].append("Maple Syrup")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Maple Syrup")] += 1
                    elif(self.storeText == 2):
                        self.cash -= 3
                        if("Mittens" not in self.cart[0]):
                            self.cart[0].append("Mittens")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Mittens")] += 1
                    elif(self.storeText == 3):
                        self.cash -= 20
                        if("Fishing Rod" not in self.cart[0]):
                            self.cart[0].append("Fishing Rod")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Fishing Rod")] += 1
                    if self.storeText == 0:
                        self.storeText = 1
                if(pyxel.mouse_x > self.option2_g.x and pyxel.mouse_x < (self.option2_g.x + self.option2_g.side) and pyxel.mouse_y > self.option2_g.y and pyxel.mouse_y < (self.option2_g.y + self.option2_g.side)):
                    if(self.storeText == 1):
                        self.cash -= 5
                        if("Bread" not in self.cart[0]):
                            self.cart[0].append("Bread")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Bread")] += 1
                    elif(self.storeText == 2):
                        self.cash -= 7
                        if("Toque" not in self.cart[0]):
                            self.cart[0].append("Toque")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Toque")] += 1
                    elif(self.storeText == 3):
                        self.cash -= 25
                        if("Medicine" not in self.cart[0]):
                            self.cart[0].append("Medicine")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Medicine")] += 1
                    if self.storeText == 0:
                        self.storeText = 2
                if(pyxel.mouse_x > self.option3_g.x and pyxel.mouse_x < (self.option3_g.x + self.option3_g.side) and pyxel.mouse_y > self.option3_g.y and pyxel.mouse_y < (self.option3_g.y + self.option3_g.side)):
                    if(self.storeText == 1):
                        self.cash -= 10
                        if("Canned Beans" not in self.cart[0]):
                            self.cart[0].append("Canned Beans")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Canned Beans")] += 1
                    elif(self.storeText == 2):
                        self.cash -= 12
                        if("Boots" not in self.cart[0]):
                            self.cart[0].append("Boots")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Boots")] += 1
                    elif(self.storeText == 3):
                        self.cash -= 30
                        if("Trap" not in self.cart[0]):
                            self.cart[0].append("Trap")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Trap")] += 1
                    if self.storeText == 0:
                        self.storeText = 3
                if(pyxel.mouse_x > self.option4_g.x and pyxel.mouse_x < (self.option4_g.x + self.option4_g.side) and pyxel.mouse_y > self.option4_g.y and pyxel.mouse_y < (self.option4_g.y + self.option4_g.side)):
                    if(self.storeText == 1):
                        self.cash -= 25
                        if("Canadian Bacon" not in self.cart[0]):
                            self.cart[0].append("Canadian Bacon")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Canadian Bacon")] += 1
                    elif(self.storeText == 2):
                        self.cash -= 20
                        if("Coat" not in self.cart[0]):
                            self.cart[0].append("Coat")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Coat")] += 1
                    elif(self.storeText == 3):
                        self.cash -= 50
                        if("Tent" not in self.cart[0]):
                            self.cart[0].append("Tent")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Tent")] += 1
                    if self.storeText == 0:
                        self.cartText = 1
            if(pyxel.mouse_x > self.option1_g.x and pyxel.mouse_x < (self.option1_g.x + self.option1_g.side) and pyxel.mouse_y > self.option1_g.y and pyxel.mouse_y < (self.option1_g.y + self.option1_g.side)):
                self.option_highlight = 1
            elif(pyxel.mouse_x > self.option2_g.x and pyxel.mouse_x < (self.option2_g.x + self.option2_g.side) and pyxel.mouse_y > self.option2_g.y and pyxel.mouse_y < (self.option2_g.y + self.option2_g.side)):
                self.option_highlight = 2
            elif(pyxel.mouse_x > self.option3_g.x and pyxel.mouse_x < (self.option3_g.x + self.option3_g.side) and pyxel.mouse_y > self.option3_g.y and pyxel.mouse_y < (self.option3_g.y + self.option3_g.side)):
                self.option_highlight = 3 
            elif(pyxel.mouse_x > self.option4_g.x and pyxel.mouse_x < (self.option4_g.x + self.option4_g.side) and pyxel.mouse_y > self.option4_g.y and pyxel.mouse_y < (self.option4_g.y + self.option4_g.side)):
                self.option_highlight = 4
            else:
                self.option_highlight = 0
        
########### TRAVELLING SCENE ##########
        elif self.active_scene == 4:
            # pyxel.image(0).load(0, 0, "assets/morning.jpg")

            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            
                #CHOICE THAT CHANGES DAY STATE
                if(pyxel.mouse_x > self.option1_t.x and pyxel.mouse_x < (self.option1_t.x + self.option1_t.side) and pyxel.mouse_y > self.option1_t.y and pyxel.mouse_y < (self.option1_t.y + self.option1_t.side)):
                    if(self.option1_t.color == 6):
                        if(self.day_state == 1):
                            pyxel.image(0).load(0, 0, "assets/afternoon.jpg")
                            self.day_state = 2 #GOES INTO AFTERNOON WORDS
                            self.previous_state = 2
                        elif(self.day_state == 2):
                            pyxel.image(0).load(0, 0, "assets/sunset.png")
                            self.day_state = 3 #GOES INTO EVENING WORDS
                            self.previous_state = 3
                        elif(self.previous_state == 3):
                            self.active_scene = 5

                    else:
                        self.day_state = self.previous_state #ELSE GO TO MORNING
                        pyxel.image(0).load(0, 0, "assets/morning.jpg")

                #LOST CHOICE
                if(pyxel.mouse_x > self.option2_t.x and pyxel.mouse_x < (self.option2_t.x + self.option2_t.side) and pyxel.mouse_y > self.option2_t.y and pyxel.mouse_y < (self.option2_t.y + self.option2_t.side)):
                    if(self.option2_t.color == 6):
                        pyxel.image(0).load(0, 0, "assets/lost.jpg")
                        self.day_state = 1  #MAINTAINS MORNING
                        self.choice = 2     #GOES INTO LOST CHOICE
                    else:
                        self.choice = 1     #MAINTAINS RIGHT CHOICE
                        self.day_state = 1  #GOES INTO LOST CHOICE
                        pyxel.image(0).load(0, 0, "assets/morning.jpg")

                #CAMP CHOICE
                if(pyxel.mouse_x > self.option3_t.x and pyxel.mouse_x < (self.option3_t.x + self.option3_t.side) and pyxel.mouse_y > self.option3_t.y and pyxel.mouse_y < (self.option3_t.y + self.option3_t.side)):
                    if(self.option3_t.color == 6):
                        pyxel.image(0).load(0, 0, "assets/camp.png")
                        self.day_state = 1
                        self.choice = 3  #GOES INTO CAMP CHOICE
                    else:
                        self.day_state = 1
                        self.choice = 2

########### DEFAULT ##########        
        else:
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

########### HIGHLIGHT TRAVELLING SCENE #########
        if(pyxel.mouse_x > self.option1_t.x and pyxel.mouse_x < (self.option1_t.x + self.option1_t.side) and pyxel.mouse_y > self.option1_t.y and pyxel.mouse_y < (self.option1_t.y + self.option1_t.side)):
            self.option_t_highlight = 1
        elif(pyxel.mouse_x > self.option2_t.x and pyxel.mouse_x < (self.option2_t.x + self.option2_t.side) and pyxel.mouse_y > self.option2_t.y and pyxel.mouse_y < (self.option2_t.y + self.option2_t.side)):
            self.option_t_highlight = 2
        elif(pyxel.mouse_x > self.option3_t.x and pyxel.mouse_x < (self.option3_t.x + self.option3_t.side) and pyxel.mouse_y > self.option3_t.y and pyxel.mouse_y < (self.option3_t.y + self.option3_t.side)):
            self.option_t_highlight = 3 
        else:
            self.option_t_highlight = 0      

#############################################################################
#####################       DRAW FUNCTIONS     ##############################
#############################################################################

    #INDICATE WHICH DRAW FUNCTION IS ASSOSIATED WITH WHICH SCENE
    def draw(self):
        # CLEAR SCREEN
        pyxel.cls(0)

        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)


        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        if self.active_scene != 2:
            pyxel.rect(0, 180, 256, 76, 0)

        # GENDER OPTIONS
        if(self.active_scene == 1):
            self.draw_gender_options()
            
        #  ENTER NAME
        elif(self.active_scene == 2):
            self.draw_name()

        #   GENERAL STORE
        elif(self.active_scene == 3):
            self.draw_general_store()

        #   TRAVELLING SCENES
        elif(self.active_scene == 4):
            self.draw_travelling()

        # OPTIONS
        elif(self.active_scene != 1):
            self.draw_options()
    
########## GENDER OPTIONS ############
    def draw_gender_options(self):
        # TEXT
        pyxel.text(2, 182, "Choose your gender and press ENTER", 3)

        # OPTIONS
        pyxel.rect(self.gender_option_m.x, self.gender_option_m.y, self.gender_option_m.side, self.gender_option_m.side, self.gender_option_m.color)
        pyxel.text(10, self.gender_option_m.y, "Male", 2)
        pyxel.rect(self.gender_option_f.x, self.gender_option_f.y, self.gender_option_f.side, self.gender_option_f.side, self.gender_option_f.color)
        pyxel.text(210, self.gender_option_f.y, "Female", 8)
        pyxel.rect(self.gender_option_b.x, self.gender_option_b.y, self.gender_option_b.side, self.gender_option_b.side, self.gender_option_b.color)
        pyxel.text(110, self.gender_option_b.y, "Non-Binary", 5)

        # TEXT CONFIRMATION AFTER SELECTION
        if (self.gender == 1):
            pyxel.text(96, 232, "You are female.", 8)
        elif (self.gender == 2): 
            pyxel.text(96, 232, "You are male.", 2)
        elif (self.gender == 3):
            pyxel.text(96, 232, "You are non-binary.", 5)

########## ENTER NAME ############
    def draw_name(self):
        # VISUALS FOR INPUTTING NAME
        pyxel.rect(60, 102, 137, 70, 0)
        pyxel.text(95, 118, "Type in your name", 7)
        pyxel.text(100, 130, self.name, 7)
        nameLength = len(self.name)
        underScores = ""
        for i in range(15):
                underScores += "_"
        pyxel.text(100, 132, underScores, 7)
        pyxel.text(85, 150, "Press ENTER to confirm", 7)

########## TRAVELLING SCENES ############
    def draw_general_store(self):
        
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        if(self.gender == 1):
            self.genderText = "guy"
        elif(self.gender == 2):
            self.genderText = "gal"
        else:
            self.genderText = "pal"

        pyxel.text(2, 182, "\"Mornin', what will a young " + self.genderText + " like yourself be buying today?\" the shopkeeper says gruffly.", 7)

        # OPTIONS
        # One letter - 5x4
        # Where the remaining cash amount will be.
        pyxel.rect(200, 0, 56, 10, 13)
        pyxel.rectb(200, 0, 56, 10, 0)
        pyxel.text(202, 3, "Cash:$" + str(self.cash), 0)

        pyxel.rectb(self.option1_g.x, self.option1_g.y, self.option1_g.side, self.option1_g.side, self.option1_g.color)
        pyxel.text(10, self.option1_g.y, "Food", 3)
        pyxel.rectb(self.option2_g.x, self.option2_g.y, self.option2_g.side, self.option2_g.side, self.option2_g.color)
        pyxel.text(10, self.option2_g.y, "Clothing", 3)
        pyxel.rectb(self.option3_g.x, self.option3_g.y, self.option3_g.side, self.option3_g.side, self.option3_g.color)
        pyxel.text(10, self.option3_g.y, "Supplies", 3)
        pyxel.rectb(self.option4_g.x, self.option4_g.y, self.option4_g.side, self.option4_g.side, self.option4_g.color)
        pyxel.text(10, self.option4_g.y, "Check your basket", 3)
        pyxel.text(2, 250, "Press Enter to checkout your basket.", 2)

        # SHOW FOOD
        if(self.storeText == 1):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"This is all the grub I have. Should keep your stomach filled.\"", 7)
            pyxel.rectb(self.option1_g.x, self.option1_g.y, self.option1_g.side, self.option1_g.side, self.option1_g.color)
            pyxel.text(10, self.option1_g.y, "Maple Syrup - $2", 2)
            pyxel.rectb(self.option2_g.x, self.option2_g.y, self.option2_g.side, self.option2_g.side, self.option2_g.color)
            pyxel.text(10, self.option2_g.y, "Bread - $5", 2)
            pyxel.rectb(self.option3_g.x, self.option3_g.y, self.option3_g.side, self.option3_g.side, self.option3_g.color)
            pyxel.text(10, self.option3_g.y, "Canned Beans - $10", 2)
            pyxel.rectb(self.option4_g.x, self.option4_g.y, self.option4_g.side, self.option4_g.side, self.option4_g.color)
            pyxel.text(10, self.option4_g.y, "Canadian Bacon - $25", 2)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        # SHOW CLOTHING
        elif(self.storeText == 2):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"Should keep yourselves warm. Gets pretty chilly here in Banff.\"", 7)
            pyxel.rectb(self.option1_g.x, self.option1_g.y, self.option1_g.side, self.option1_g.side, self.option1_g.color)
            pyxel.text(10, self.option1_g.y, "Mittens - $3", 2)
            pyxel.rectb(self.option2_g.x, self.option2_g.y, self.option2_g.side, self.option2_g.side, self.option2_g.color)
            pyxel.text(10, self.option2_g.y, "Toque - $7", 2)
            pyxel.rectb(self.option3_g.x, self.option3_g.y, self.option3_g.side, self.option3_g.side, self.option3_g.color)
            pyxel.text(10, self.option3_g.y, "Boots - $12", 2)
            pyxel.rectb(self.option4_g.x, self.option4_g.y, self.option4_g.side, self.option4_g.side, self.option4_g.color)
            pyxel.text(10, self.option4_g.y, "Coat - $20", 2)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        # SHOW SUPPLIES
        elif(self.storeText == 3):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"Ahh, you're one of those hiker folk. Got quality supplies here.\"", 7)
            pyxel.rectb(self.option1_g.x, self.option1_g.y, self.option1_g.side, self.option1_g.side, self.option1_g.color)
            pyxel.text(10, self.option1_g.y, "Fishing Rod - $20", 2)
            pyxel.rectb(self.option2_g.x, self.option2_g.y, self.option2_g.side, self.option2_g.side, self.option2_g.color)
            pyxel.text(10, self.option2_g.y, "Medicine - $25", 2)
            pyxel.rectb(self.option3_g.x, self.option3_g.y, self.option3_g.side, self.option3_g.side, self.option3_g.color)
            pyxel.text(10, self.option3_g.y, "Trap - $30", 2)
            pyxel.rectb(self.option4_g.x, self.option4_g.y, self.option4_g.side, self.option4_g.side, self.option4_g.color)
            pyxel.text(10, self.option4_g.y, "Tent - $50", 2)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        # HOVER ANIMATIONS
        if(self.option_highlight == 1):
            pyxel.rect(self.option1_g.x, self.option1_g.y, self.option1_g.side, self.option1_g.side, self.option1_g.color)
        elif(self.option_highlight == 2):
            pyxel.rect(self.option2_g.x, self.option2_g.y, self.option2_g.side, self.option2_g.side, self.option2_g.color)
        elif(self.option_highlight == 3):
            pyxel.rect(self.option3_g.x, self.option3_g.y, self.option3_g.side, self.option3_g.side, self.option3_g.color)
        elif(self.option_highlight == 4):
            pyxel.rect(self.option4_g.x, self.option4_g.y, self.option4_g.side, self.option4_g.side, self.option4_g.color)

        # SHOW CART
        if(self.cartText == 1):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "Cart:", 7)
            tempColumn = 190
            for j in range(len(self.cart[0])):
                pyxel.text(2, tempColumn, str(self.cart[0][j]) + " - " + str(self.cart[1][j]), 11)
                tempColumn += 8
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

########## TRAVELLING SCENES ############
    def draw_travelling(self):
        # CLEAR SCREEN
        # pyxel.cls(0)

        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(0, 180, 256, 76, 0)
        
        #CONSTANT OPTIONS
        pyxel.rectb(self.option1_t.x, self.option1_t.y, self.option1_t.side, self.option1_t.side, self.option1_t.color)
        pyxel.text(10, self.option1_t.y, "Go North", 3)
        pyxel.rectb(self.option2_t.x, self.option2_t.y, self.option2_t.side, self.option2_t.side, self.option2_t.color)
        pyxel.text(10, self.option2_t.y, "See what's in the west", 4)
        pyxel.rectb(self.option3_t.x, self.option3_t.y, self.option3_t.side, self.option3_t.side, self.option3_t.color)
        pyxel.text(10, self.option3_t.y, "Make Camp", 5)
        
        # HOVER ANIMATIONS
        if(self.option_t_highlight == 1):
            pyxel.rect(self.option1_t.x, self.option1_t.y, self.option1_t.side, self.option1_t.side, self.option1_t.color)
        elif(self.option_t_highlight == 2):
            pyxel.rect(self.option2_t.x, self.option2_t.y, self.option2_t.side, self.option2_t.side, self.option2_t.color)
        elif(self.option_t_highlight == 3):
            pyxel.rect(self.option3_t.x, self.option3_t.y, self.option3_t.side, self.option3_t.side, self.option3_t.color)

        pyxel.text(2, 182, "Day 2 - MORNING - March 16, 1901 - Banff, Alberta", 7)
        pyxel.text(2, 189, "It's morning. Where would you like to go?", 7)
        if self.day_state == 1:
            # SPEACH FOR MORNING AND OTHER CHOICES
            if self.choice == 1:
                pyxel.rect(0, 180, 256, 20, 0)
                pyxel.text(2, 182, "Day 2 - MORNING - March 16, 1901 - Banff, Alberta", 7)
                pyxel.text(2, 189, "It's morning. Where would you like to go?", 7)
            elif self.choice == 2:
                pyxel.rect(0, 180, 256, 20, 0)
                pyxel.text(2, 182, "You got lost! Stay on track next time!", 7)
                pyxel.text(2, 189, "Where would you like to go?", 7)
            elif self.choice == 3:
                pyxel.rect(0, 180, 256, 20, 0)
                pyxel.text(2, 182, "You camped too early! A day is wasted. You will lose life.", 7)
                pyxel.text(2, 189, "Where would you like to go?", 7)
        elif self.day_state == 2:
            # SPEACH FOR AFTERNOON 
            pyxel.rect(0, 180, 256, 20, 0)
            pyxel.text(2, 182, "Day 2 - AFTERNOON - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 12 in the afternoon. Where would you like to go?", 7)
        elif self.day_state == 3:
            # SPEACH FOR Evening 
            pyxel.rect(0, 180, 256, 20, 0)
            pyxel.text(2, 182, "Day 2 - EVENING - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 6pm, in the evening. Where would you like to go?", 7)

########## DEFAULT ############
    def draw_options(self):
        # TEMPLATE FOR OPTION SELECT
        pyxel.text(2, 182, "There is text here gotem", 1)
        pyxel.text(2, 189, "There is text here too very cool stuff very nice", 2)

        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option1.y, "This is option 1", 3)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(10, self.option2.y, "This is option 2", 4)
        pyxel.rect(self.option3.x, self.option3.y, self.option3.side, self.option3.side, self.option3.color)
        pyxel.text(10, self.option3.y, "This is option 3", 5)

App()