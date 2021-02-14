import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="The Great Canadian Masterpiece", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/group_of_seven.jpg")
        pyxel.image(2).load(0, 0, "assets/title.png")
        pyxel.image(1).load(0, 0, "assets/sunset.png")
    
        
        pyxel.mouse(True)

        a = "c3d2e2b3 a2b2c3b2"
        b = "c3d2e2a3 a2b2c3a2"
        
        pyxel.sound(0).set(a * 3 + b * 1, "t", "2", "nf", 30)
        pyxel.sound(1).set("a1b1b1a1", "p", "2", "nf", 120)
        pyxel.sound(2).set("c3g3c4g3", "p", "1", "nf", 150)
        pyxel.sound(3).set("c1d1e1d1 c2d2e2a1", "t", "2", "nf", 100)

        # SCENE ORGANIZATION
        self.scene = [0,1,2]
        # 0 - TITLE
        # 1 - GENDER CHOICE
        # 2 - ENTER NAME
        # 25 - CHAPTER
        # 3 - STORE
        # 4 - Travelling Days
        # 5 - Camp at night
        # 6 - Morning
        # 7 - TRACKS
        # 8 - CARIBOU

        #   TITLE
        self.active_scene = 0
        self.blurbText = 0

        self.option1 = Option(2,232,5,6)
        self.option2 = Option(2,240,5,6)
        self.option3 = Option(2,248,5,6)

        # CHAPTER
        self.option1_chapter = Option(10, 206, 5, 12)
        self.option2_chapter = Option(10, 216, 5,12)
        self.option3_chapter = Option(10, 226, 5, 12)
        self.option4_chapter = Option(10, 236, 5, 12)
        self.option_chapter_highlight = 0

        # CHOOSE YOUR GENDER
        self.gender_option_m = Option(2, 200, 5, 12)
        self.gender_option_f = Option(202,200,5,12)
        self.gender_option_b = Option(102,200,5,12)
        self.gender = 0
        self.option_gender_highlight = 0

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

        # TRAVELLING HIGHLIGHT
        self.option_t_highlight = 0

        # CAMP NIGHT TIME
        self.activeBank = 0
        self.gender = 0
        self.inventory = [["Canadian Bacon", 2], ["Dummy", 1]]
        self.status = 0  # ENSURES INVENTORY IS ONLY UPDATED ONCE
        self.consumed = 0 # WHAT WAS EATEN

        # MORNING - NO OTHER VARIABLES

        # TRACKS
        self.option1_tracks = Option(64,236,5,12)
        self.option2_tracks = Option(146,236,5,12)
        self.option_tracks_highlight = 0

        #   CARIBOU
        self.option1_caribou = Option(66,242,5,12)
        self.option2_caribou = Option(146,242,5,12)
        self.option_caribou_highlight = 0

        #   CONSEQUENCE
        self.page = 0

        #   TWOPATHS
        self.option1_r = Option(2,232,5,6)
        self.option2_r = Option(2,240,5,6)
        self.option3_r = Option(2,248,5,6)
        self.split_road_state = 1
        self.option_r_highlight = 0

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)

    def stop_music(self):
        pyxel.stop(0)
        pyxel.stop(1)
        pyxel.stop(2)
        pyxel.stop(3)

    def play_music(self, track):
        if (track == 0):
            pyxel.play(0, 0, loop=True)
            pyxel.play(1, 1, loop=True)
        elif (track == 1):
            pyxel.play(2, 2, loop=True)
            pyxel.play(3, 3 ,loop=True)

    def update(self):
####### TITLE #######
        if self.active_scene == 0:
            if pyxel.btnp(pyxel.KEY_ENTER):
                if(self.blurbText == 1):
                    self.active_scene = 1
                self.blurbText = 1

####### CHOOSE YOUR GENDER #######
        elif self.active_scene == 1:
            #self.stop_music()

            pyxel.image(0).load(0, 0, "assets/choose gender.jpg")
            pyxel.image(1).load(0, 0, "assets/nonbinary.jpg")
            pyxel.image(2).load(0, 0, "assets/female.jpg")
            #pyxel.image(3).load(0, 0, "assets/male.jpg")
            
            # MALE
            if(pyxel.mouse_x > self.gender_option_m.x and pyxel.mouse_x < (self.gender_option_m.x + self.gender_option_m.side) and pyxel.mouse_y > self.gender_option_m.y and pyxel.mouse_y < (self.gender_option_m.y + self.gender_option_m.side)):
                self.option_gender_highlight = 1
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if(self.gender_option_m.color == 12):
                        # if(self.gender_option_f.color == 0 and self.gender_option_b == 0):
                        self.gender_option_f.color = 12
                        self.gender_option_b.color = 12
                        #^shift tab

                        self.gender_option_m.color = 10
                        self.gender = 2
            
            # FEMALE
            elif(pyxel.mouse_x > self.gender_option_f.x and pyxel.mouse_x < (self.gender_option_f.x + self.gender_option_f.side) and pyxel.mouse_y > self.gender_option_f.y and pyxel.mouse_y < (self.gender_option_f.y + self.gender_option_f.side)):
                self.option_gender_highlight = 2
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if(self.gender_option_f.color == 12):
                        # if(self.gender_option_m.color == 0 and self.gender_option_b == 0):
                        self.gender_option_m.color = 12
                        self.gender_option_b.color = 12
                        self.gender_option_f.color = 10
                        self.gender = 1

            # NON-BINARY
            elif(pyxel.mouse_x > self.gender_option_b.x and pyxel.mouse_x < (self.gender_option_b.x + self.gender_option_b.side) and pyxel.mouse_y > self.gender_option_b.y and pyxel.mouse_y < (self.gender_option_b.y + self.gender_option_b.side)):
                self.option_gender_highlight =3
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if(self.gender_option_b.color == 12):
                        # if(self.gender_option_m.color == 0 and self.gender_option_f.color == 0):
                        self.gender_option_m.color = 12
                        self.gender_option_f.color = 12
                        self.gender_option_b.color = 10
                        self.gender = 3
            else:
                self.option_gender_highlight = 0

            if((self.gender == 1 or self.gender == 2 or self.gender == 3) and pyxel.btnp(pyxel.KEY_ENTER)):
                # self.play_music(0)
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
                self.active_scene = 25
                pyxel.image(0).load(0, 0, "assets/lake.png")

########### SELECT CHAPTER ##########
        elif self.active_scene == 25:
            pyxel.image(0).load(0, 0, "assets/camp.png")
            if(pyxel.mouse_x > self.option1_chapter.x and pyxel.mouse_x < (self.option1_chapter.x + self.option1_chapter.side) and pyxel.mouse_y > self.option1_chapter.y and pyxel.mouse_y < (self.option1_chapter.y + self.option1_chapter.side)):
                self.option_chapter_highlight = 1
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.active_scene = 3
            else:
                self.option_chapter_highlight = 0
                 
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

            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            
                #CHOICE THAT CHANGES DAY STATE
                if(pyxel.mouse_x > self.option1_t.x and pyxel.mouse_x < (self.option1_t.x + self.option1_t.side) and pyxel.mouse_y > self.option1_t.y and pyxel.mouse_y < (self.option1_t.y + self.option1_t.side)):
                    if(self.option1_t.color == 6):
                        self.option1_t.color = 8
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
                        self.option1_t.color = 6
                #LOST CHOICE
                if(pyxel.mouse_x > self.option2_t.x and pyxel.mouse_x < (self.option2_t.x + self.option2_t.side) and pyxel.mouse_y > self.option2_t.y and pyxel.mouse_y < (self.option2_t.y + self.option2_t.side)):
                    if(self.option2_t.color == 6):
                        self.option2_t.color = 8
                        pyxel.image(0).load(0, 0, "assets/lost.jpg")
                        self.day_state = 1  #MAINTAINS MORNING
                        self.choice = 2     #GOES INTO LOST CHOICE
                    else:
                        self.choice = 1     #MAINTAINS RIGHT CHOICE
                        self.day_state = 1  #GOES INTO LOST CHOICE
                        pyxel.image(0).load(0, 0, "assets/morning.jpg")
                    self.option1_t.color = 6
                    self.option3_t.color = 6

                #CAMP CHOICE
                if(pyxel.mouse_x > self.option3_t.x and pyxel.mouse_x < (self.option3_t.x + self.option3_t.side) and pyxel.mouse_y > self.option3_t.y and pyxel.mouse_y < (self.option3_t.y + self.option3_t.side)):
                    if(self.option3_t.color == 6):
                        self.option3_t.color = 8
                        pyxel.image(0).load(0, 0, "assets/camp.png")
                        self.day_state = 1
                        self.choice = 3  #GOES INTO CAMP CHOICE
                    else:
                        self.day_state = 1
                        self.choice = 2
                    self.option1_t.color = 6
                    self.option2_t.color = 6
                    
########### CAMP NIGHT TIME  ##########
        elif(self.active_scene == 5):
            pyxel.image(0).load(0, 0, "assets/fire.jpg")
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 6

########### MORNING ############
        elif(self.active_scene == 6):
            pyxel.image(0).load(0, 0, "assets/morning.jpg")
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 7

########### TRACKS ############
        elif self.active_scene == 7:
            pyxel.image(0).load(0, 0, "assets/moose_tracks.jpg")
            if(pyxel.mouse_x > self.option1_tracks.x and pyxel.mouse_x < (self.option1_tracks.x + self.option1_tracks.side) and pyxel.mouse_y > self.option1_tracks.y and pyxel.mouse_y < (self.option1_tracks.y + self.option1_tracks.side)):
                self.option_tracks_highlight = 1
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.active_scene = 8
            elif(pyxel.mouse_x > self.option2_tracks.x and pyxel.mouse_x < (self.option2_tracks.x + self.option2_tracks.side) and pyxel.mouse_y > self.option2_tracks.y and pyxel.mouse_y < (self.option2_tracks.y + self.option2_tracks.side)):
                self.option_tracks_highlight = 2
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.option2_tracks.color = 8
                    # GO TO 2 PATHS
            else:
                self.option_tracks_highlight = 0

########### CARIBOU ############
        elif self.active_scene == 8:
            pyxel.image(0).load(0, 0, "assets/caribou.png")
            if(pyxel.mouse_x > self.option1_caribou.x and pyxel.mouse_x < (self.option1_caribou.x + self.option1_caribou.side) and pyxel.mouse_y > self.option1_caribou.y and pyxel.mouse_y < (self.option1_caribou.y + self.option1_caribou.side)):
                self.option_caribou_highlight = 1
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.option1_caribou.color = 8
                    self.active_scene = 9
                    # GO TO CONSEQUENCE
            elif(pyxel.mouse_x > self.option2_caribou.x and pyxel.mouse_x < (self.option2_caribou.x + self.option2_caribou.side) and pyxel.mouse_y > self.option2_caribou.y and pyxel.mouse_y < (self.option2_caribou.y + self.option2_caribou.side)):
                self.option_caribou_highlight = 2
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    self.option2_caribou.color = 8
                    self.active_scene = 10
                    # GO TO 2 PATHS
            else:
                self.option_caribou_highlight = 0

########### CONSEQUENCE ############
        elif(self.active_scene == 9):
            pyxel.image(0).load(0, 0, "assets/fall.jpg")
            if self.page ==4 and pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 10
                pyxel.image(0).load(0, 0, "assets/sunset.png")

########### TWO PATHS ############
        elif(self.active_scene == 10):

            if pyxel.btnp(pyxel.KEY_ENTER) and self.split_road_state ==4:
                self.active_scene = 11
                pyxel.image(0).load(0, 0, "assets/lake_louise.jpg")    

            if(pyxel.mouse_x > self.option1_r.x and pyxel.mouse_x < (self.option1_r.x + self.option1_r.side) and pyxel.mouse_y > self.option1_r.y and pyxel.mouse_y < (self.option1_r.y + self.option1_r.side)):
                self.option_r_highlight = 1
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                   
                    if(self.option1_r.color == 6):
                        if self.split_road_state == 1:
                            self.split_road_state = 2
                            pyxel.image(0).load(0, 0, "assets/twopaths.jpg")
                        else:
                            self.option1_r.color = 8
                            pyxel.image(0).load(0, 0, "assets/drive2.jpg")
                            self.split_road_state =3
                    else:
                        self.option1_r.color = 6

            elif(pyxel.mouse_x > self.option2_r.x and pyxel.mouse_x < (self.option2_r.x + self.option2_r.side) and pyxel.mouse_y > self.option2_r.y and pyxel.mouse_y < (self.option2_r.y + self.option2_r.side)):
                self.option_r_highlight = 2
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if(self.option2_r.color == 6):
                        self.option2_r.color = 8
                        pyxel.image(0).load(0, 0, "assets/lost.jpg")
                    else:
                        self.option2_r.color = 6
                        pyxel.image(0).load(0, 0, "assets/twopaths.jpg")
            elif(pyxel.mouse_x > self.option3_r.x and pyxel.mouse_x < (self.option3_r.x + self.option3_r.side) and pyxel.mouse_y > self.option3_r.y and pyxel.mouse_y < (self.option3_r.y + self.option3_r.side)):
                self.option_r_highlight = 3
            else:
                self.option_r_highlight = 0

########### ARRIVING AT LAKE LOUISE ############
        elif(self.active_scene == 11):
            pyxel.image(0).load(0, 0, "assets/lake_louise.jpg")
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 12
                pyxel.image(0).load(0, 0, "assets/endcard.png")

########### PAINTING ENDING ############
        elif(self.active_scene == 12):
            pyxel.image(0).load(0, 0, "assets/endcard.png")
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.active_scene = 13

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

        # TITLE SCREEN
        if(self.active_scene == 0):
            self.draw_title()

        # GENDER OPTIONS
        if(self.active_scene == 1):
            self.draw_gender_options()
            
        #  ENTER NAME
        elif(self.active_scene == 2):
            self.draw_name()

        #   SELECT CHAPTER 
        elif(self.active_scene == 25):
            self.draw_chapter()

        #   GENERAL STORE
        elif(self.active_scene == 3):
            self.draw_general_store()

        #   TRAVELLING SCENES
        elif(self.active_scene == 4):
            self.draw_travelling()
        
        #   CAMP NIGHT TIME
        elif(self.active_scene == 5):
            self.draw_camp()

        #   MORNING
        elif(self.active_scene == 6):
            self.draw_morning()

        #   TRACKS
        elif(self.active_scene == 7):
            self.draw_tracks()

        elif(self.active_scene == 8):
            self.draw_caribou()

        elif(self.active_scene == 9):
            self.draw_consequence()
        
        elif(self.active_scene == 10):
            self.draw_twopaths()
        
        elif(self.active_scene == 11):
            self.draw_lakeLouise()
        
        elif(self.active_scene == 12):
            self.draw_endcard()

        # OPTIONS
        # elif(self.active_scene != 1):
        #     self.draw_options()

########## TITLE ############
    def draw_title(self):
        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 2, 0, 0, 256, 256)
        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        
        if(self.blurbText == 0):
            pyxel.text(0, 190,
            """
                Press ENTER to begin your adventure
            """, 7)

        elif(self.blurbText == 1):
        # TEXT
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            pyxel.text(0, 185, 
        """
        A group of Canadian artists built their fame across 
         Canada for their paintings inspired by Canada's
            beautiful landscape. Famously known as the
          'Group of Seven,' they have left their legacy
            in their world through their masterpieces. 
        But unbeknownst to some others, there was an eighth 
           person, one who aspired to leave their mark 
                  on Canadian soil as well.
                  """, 7)

########## GENDER OPTIONS ############
    def draw_gender_options(self):
        # TEXT
        pyxel.text(91, 186, "Choose your gender:", 7)

        # OPTIONS
        pyxel.rectb(self.gender_option_m.x, self.gender_option_m.y, self.gender_option_m.side, self.gender_option_m.side, self.gender_option_m.color)
        pyxel.text(10, self.gender_option_m.y, "Male", 2)
        pyxel.rectb(self.gender_option_f.x, self.gender_option_f.y, self.gender_option_f.side, self.gender_option_f.side, self.gender_option_f.color)
        pyxel.text(210, self.gender_option_f.y, "Female", 8)
        pyxel.rectb(self.gender_option_b.x, self.gender_option_b.y, self.gender_option_b.side, self.gender_option_b.side, self.gender_option_b.color)
        pyxel.text(110, self.gender_option_b.y, "Non-Binary", 5)

        if self.option_gender_highlight == 1:
             pyxel.rect(self.gender_option_m.x, self.gender_option_m.y, self.gender_option_m.side, self.gender_option_m.side, self.gender_option_m.color)
        if self.option_gender_highlight == 2:
            pyxel.rect(self.gender_option_f.x, self.gender_option_f.y, self.gender_option_f.side, self.gender_option_f.side, self.gender_option_f.color)
        if self.option_gender_highlight == 3:
            pyxel.rect(self.gender_option_b.x, self.gender_option_b.y, self.gender_option_b.side, self.gender_option_b.side, self.gender_option_b.color)

        # TEXT CONFIRMATION AFTER SELECTION
        # replaces background image
        pyxel.image(0).load(0, 0, "assets/male.jpg")
        if (self.gender == 1):
            pyxel.blt(0, 0, 2, 0, 0, 256, 180)
            pyxel.text(100, 222, "You are female.", 8)
            pyxel.text(83, 240, "Press ENTER to confirm", 7)
        elif (self.gender == 2): 
            pyxel.blt(0, 0, 0, 0, 0, 256, 180)
            pyxel.text(103, 222, "You are male.", 2)
            pyxel.text(83, 240, "Press ENTER to confirm", 7)
        elif (self.gender == 3):
            pyxel.blt(0, 0, 1, 0, 0, 256, 180)
            pyxel.text(91, 222, "You are non-binary.", 5)
            pyxel.text(83, 240, "Press ENTER to confirm", 7)

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

########## SELECT CHAPTER ############    
    def draw_chapter(self):
        pyxel.rectb(self.option1_chapter.x, self.option1_chapter.y, self.option1_chapter.side, self.option1_chapter.side, self.option1_chapter.color)
        pyxel.text(20, self.option1_chapter.y, "Forest", 2)
        pyxel.rectb(self.option2_chapter.x, self.option2_chapter.y, self.option2_chapter.side, self.option2_chapter.side, self.option2_chapter.color)
        pyxel.text(20, self.option2_chapter.y, "Lake             [Locked]", 8)
        pyxel.rectb(self.option3_chapter.x, self.option3_chapter.y, self.option3_chapter.side, self.option3_chapter.side, self.option3_chapter.color)
        pyxel.text(20, self.option3_chapter.y, "Mountain         [Locked]", 8)
        pyxel.rectb(self.option4_chapter.x, self.option4_chapter.y, self.option4_chapter.side, self.option4_chapter.side, self.option4_chapter.color)
        pyxel.text(20, self.option4_chapter.y, "The Great Lakes  [Locked]", 8)

        if self.option_chapter_highlight == 1:
            pyxel.rect(self.option1_chapter.x, self.option1_chapter.y, self.option1_chapter.side, self.option1_chapter.side, self.option1_chapter.color)
        
        pyxel.text(6, 192, "Chapter Select", 7)

########## GENERAL STORE ############
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
        pyxel.rect(0, 170, 56, 10, 9)
        pyxel.rectb(0, 170, 56, 10,0)
        pyxel.text(2, 173, "Cash:$" + str(self.cash), 0)

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

        pyxel.text(2, 182, "Day 1 - MORNING - March 16, 1901 - Banff, Alberta", 7)
        pyxel.text(2, 189, "It's morning. Where would you like to go?", 7)
        if self.day_state == 1:
            # SPEACH FOR MORNING AND OTHER CHOICES
            if self.choice == 1:
                pyxel.rect(0, 180, 256, 20, 0)
                pyxel.text(2, 182, "Day 1 - MORNING - March 16, 1901 - Banff, Alberta", 7)
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
            pyxel.text(2, 182, "Day 1 - AFTERNOON - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 12 in the afternoon. Where would you like to go?", 7)
        elif self.day_state == 3:
            # SPEACH FOR Evening 
            pyxel.rect(0, 180, 256, 20, 0)
            pyxel.text(2, 182, "Day 1 - EVENING - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 6pm, in the evening. Where would you like to go?", 7)

########## CAMP NIGHT TIME ############
    def draw_camp(self):
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        if (self.status < 1):
            self.consumed = self.inventory[0][0]

        pyxel.text(2, 188, "You have decided to make camp and rest for the next day.", 7)
        pyxel.text(2, 198, "You have decided to eat one " + self.consumed + ".", 7)

        pyxel.text(2, 212, "Changes in inventory:", 7)
        pyxel.text(2, 222, "-" + self.consumed + "      -1", 7)

        pyxel.text(2, 238, "Press ENTER to continue.", 7)
        # NOTE: REQUIRES CODE TO TRANSITION INTO NEXT SCENE

        if(self.status < 1):
            self.inventory[0][1] -= 1
            if (self.inventory[0][1] == 0):
                self.inventory.pop(0)
        self.status = 1

########## MORNING ############
    def draw_morning(self):
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        pyxel.text(2, 188, "It's Day 2 - March 16, 1901.", 7)
        pyxel.text(2, 204, "You can hear the birds chirping outside.", 7)
        pyxel.text(2, 214, "You yawn and stretch your stiff limbs.", 7)
        
        pyxel.text(2, 228, "It's time to move.", 7)

########## TRACKS ############
    def draw_tracks(self):
        pyxel.rectb(self.option1_tracks.x, self.option1_tracks.y, self.option1_tracks.side, self.option1_tracks.side, self.option1_tracks.color)
        pyxel.text(74, self.option1_tracks.y, "Investigate", 2)
        pyxel.rectb(self.option2_tracks.x, self.option2_tracks.y, self.option2_tracks.side, self.option2_tracks.side, self.option2_tracks.color)
        pyxel.text(156, self.option2_tracks.y, "Ignore them", 8)

        if self.option_tracks_highlight == 1:
            pyxel.rect(self.option1_tracks.x, self.option1_tracks.y, self.option1_tracks.side, self.option1_tracks.side, self.option1_tracks.color)
        if self.option_tracks_highlight == 2:
            pyxel.rect(self.option2_tracks.x, self.option2_tracks.y, self.option2_tracks.side, self.option2_tracks.side, self.option2_tracks.color)
        
        pyxel.text(4, 188, "You encounter animal tracks along the trail you are traveling", 7)
        pyxel.text(4, 198, "along. You are not an expert in wildlife so you are unsure", 7)
        pyxel.text(4, 208, "as to whose prints it belongs to. However, your curiosity is ", 7)
        pyxel.text(4, 218, "getting the better of you. What do you do?", 7)

########## CARIBOU ############
    def draw_caribou(self):
        pyxel.rectb(self.option1_caribou.x, self.option1_caribou.y, self.option1_caribou.side, self.option1_caribou.side, self.option1_caribou.color)
        pyxel.text(76, self.option1_caribou.y, "Go closer", 2)
        pyxel.rectb(self.option2_caribou.x, self.option2_caribou.y, self.option2_caribou.side, self.option2_caribou.side, self.option2_caribou.color)
        pyxel.text(156, self.option2_caribou.y, "Stay still", 8)

        if self.option_caribou_highlight == 1:
            pyxel.rect(self.option1_caribou.x, self.option1_caribou.y, self.option1_caribou.side, self.option1_caribou.side, self.option1_caribou.color)
        if self.option_caribou_highlight == 2:
            pyxel.rect(self.option2_caribou.x, self.option2_caribou.y, self.option2_caribou.side, self.option2_caribou.side, self.option2_caribou.color)

        pyxel.text(2, 188, "You followed the tracks and it led you to a small creek where", 7)
        pyxel.text(2, 198, "you spot a caribou drinking from the clear waters. Its horns ", 7)
        pyxel.text(2, 208, "are long and curved. It lifts its head up upon your approach.", 7)
        pyxel.text(2, 218, "The majestic creature shifts nervously, and upon closer", 7)
        pyxel.text(2, 228, "inspection, you can see that its fur is matted with blood.", 7)

########## CONSEQUENCE ############

    def draw_consequence(self):
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        if (self.page == 0):      
            pyxel.text(4, 186, "This is the first time you've seen such a beautiful animal up", 7)
            pyxel.text(4, 196, "close. You have to get closer to it, drink in all the details,", 7)
            pyxel.text(4, 206, "else you'd never be able to pick up your paintbrush again!", 7)
            pyxel.text(4, 216, "You slink behind a tree and squat down. The caribou stands", 7)
            pyxel.text(4, 226, "still for a moment longer before dipping its head back.", 7)
            pyxel.text(4, 236, "into the water. You swallow your nervousness before", 7)
            pyxel.text(4, 246, "slipping out of your hiding place.", 7)         
            
            if pyxel.btnp(pyxel.KEY_ENTER):  
                self.page = 1


        if (self.page == 1 or self.page == 2):
            if pyxel.btnp(pyxel.KEY_ENTER) == False:                            
                # BACKGROUND
                # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
                pyxel.blt(0, 0, 0, 0, 0, 256, 256)
                
                # DRAW BLACK TEXTBOX
                # rect(x, y, w, h, col)
                pyxel.rect(0, 180, 256, 76, 0)

                pyxel.text(4, 188, "A mistake! The creature locks eyes with you, and with a", 7)
                pyxel.text(4, 198, "shrill cry, he dips his head and charges at you!", 7)
                pyxel.text(4, 212, "You try to move, but it's too late.", 7)

                pyxel.text(4, 226, "Pain shoots through your spine as your back hits the sharp", 7)
                pyxel.text(4, 236, "rocks on the edge of the creek. The caribou pays you no", 7)
                pyxel.text(4, 246, "mind and keeps running, quickly disappearing into the forest.", 7) 

                self.page = 2

        if (self.page == 2 and pyxel.btnp(pyxel.KEY_ENTER)):
            self.page = 3
            
        if (self.page == 3 or self.page == 4):  
            pyxel.cls(0)

            # BACKGROUND
            # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            
            # DRAW BLACK TEXTBOX
            # rect(x, y, w, h, col)
            pyxel.rect(0, 180, 256, 76, 0)

            pyxel.text(4, 188, "You grimace as you pull yourself back to your feet. Your", 7)
            pyxel.text(4, 198, "clothes are wet and your back throbs. You lift your shirt", 7)
            pyxel.text(4, 212, "to examine your injuries. There is an open gash where the", 7)
            pyxel.text(4, 222, "caribou's horn pierced your skin, but thankfully it's not", 7)
            pyxel.text(4, 232, "too deep. You hobble out of the water, cursing your luck.", 7)

            self.page = 4

########## TWOPATHS ############
    def draw_twopaths(self):

        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(0, 180, 256, 76, 0)

        if self.split_road_state == 2:
        # TEXT
            pyxel.text(2, 182, "DAY 2 - EVENING - BANFF, ALBERTA\n\n", 7)
            pyxel.text(2, 189, "You see two paths, one leads north, the other leads north west. \nThe north road looks dangerous.\nWhich way do you go?", 7)

            # OPTIONS
            pyxel.rectb(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
            pyxel.text(10, self.option1_r.y, "Go North Road", 3)
            pyxel.rectb(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
            pyxel.text(10, self.option2_r.y, "Go Nort West Road", 4)

        elif self.split_road_state == 1:
            pyxel.text(2, 182, "Day 2 - EVENING - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 6pm, in the evening. Where would you like to go?", 7)

            # OPTIONS
            pyxel.rectb(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
            pyxel.text(10, self.option1_r.y, "Go North", 3)
            pyxel.rectb(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
            pyxel.text(10, self.option2_r.y, "Go West", 4)
            pyxel.rectb(self.option3_r.x, self.option3_r.y, self.option3_r.side, self.option3_r.side, self.option3_r.color)
            pyxel.text(10, self.option3_r.y, "Make Camp", 5)
        
        elif self.split_road_state == 3 or self.split_road_state == 4:
            pyxel.text(2, 182, "You were found in the morning passed out from the darkness!", 7)
            pyxel.text(2, 189, "Fortunately, some kind strangers saw you on the road and \n offered to take you where you need to go! \n\n\nPress ENTER to continue", 7)
        
        if self.option_r_highlight == 1:
            pyxel.rect(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
        elif self.option_r_highlight == 2:
            pyxel.rect(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
        elif self.option_r_highlight == 3:
            pyxel.rect(self.option3_r.x, self.option3_r.y, self.option3_r.side, self.option3_r.side, self.option3_r.color)
            self.split_road_state = 4
            

########## LAKE LOUISE ############
    def draw_lakeLouise(self):
        pyxel.image(0).load(0, 0, "assets/lake_louise.jpg")
        pyxel.blt(0, 0, 1, 0, 0, 256, 256)
        pyxel.text(0, 190,
            """
        You arrive at a beautiful blue-green lake.
        You can see a soaring white mountain in the background and 
        the sun just peaking from behind.

        Your sould overwhelms with awe and wonder and you turn to 
        your paintbrush. Your hands move careful as to capture every
        inch of its beauty. You have traveled long and far but alas, 
        you have found your new muse.
                
            """, 7)

    ########## END CARD ############
    def draw_endcard(self):
        pyxel.image(0).load(0, 0, "assets/endcard.png")
        pyxel.blt(0, 0, 1, 0, 0, 256, 256)
        pyxel.text(0, 190,
            """
            Congratulations! You have painted Lake Louise!
                        What a masterpiece!
            """, 7)

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