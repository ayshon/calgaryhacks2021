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
        pyxel.image(0).load(0, 0, "assets/morning.jpg")
        
        pyxel.mouse(True)

        self.option1 = Option(2,200,5,6)
        self.option2 = Option(2,210,5,6)
        self.option3 = Option(2,220,5,6)
        self.day_state =1 #1 for morning, #2 for afternoon, #3 for evening 
        self.choice = 1 #1 for new state, #2 for lost, #3 for camp
        self.previous_state = 1

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            
            #CHOICE THAT CHANGES DAY STATE
            if(pyxel.mouse_x > self.option1.x and pyxel.mouse_x < (self.option1.x + self.option1.side) and pyxel.mouse_y > self.option1.y and pyxel.mouse_y < (self.option1.y + self.option1.side)):
                if(self.option1.color == 6):
                    self.option1.color = 0
                    if(self.day_state == 1):
                        pyxel.image(0).load(0, 0, "assets/afternoon.jpg")
                        self.day_state = 2 #GOES INTO AFTERNOON WORDS
                        self.previous_state = 2
                    elif(self.day_state == 2):
                        pyxel.image(0).load(0, 0, "assets/sunset.png")
                        self.day_state = 3 #GOES INTO EVENING WORDS
                        self.previous_state = 3

                else:
                    self.day_state = self.previous_state #ELSE GO TO MORNING
                    self.option1.color = 6
                    pyxel.image(0).load(0, 0, "assets/morning.jpg")

            #LOST CHOICE
            if(pyxel.mouse_x > self.option2.x and pyxel.mouse_x < (self.option2.x + self.option2.side) and pyxel.mouse_y > self.option2.y and pyxel.mouse_y < (self.option2.y + self.option2.side)):
                if(self.option2.color == 6):
                    self.option2.color = 0
                    pyxel.image(0).load(0, 0, "assets/lost.jpg")
                    self.day_state = 1  #MAINTAINS MORNING
                    self.choice = 2     #GOES INTO LOST CHOICE
                else:
                    self.choice = 1     #MAINTAINS RIGHT CHOICE
                    self.day_state = 1  #GOES INTO LOST CHOICE
                    self.option2.color = 6
                    pyxel.image(0).load(0, 0, "assets/morning.jpg")

            #CAMP CHOICE
            if(pyxel.mouse_x > self.option3.x and pyxel.mouse_x < (self.option3.x + self.option3.side) and pyxel.mouse_y > self.option3.y and pyxel.mouse_y < (self.option3.y + self.option3.side)):
                if(self.option3.color == 6):
                    self.option3.color = 0
                    pyxel.image(0).load(0, 0, "assets/camp.png")
                    self.day_state = 1
                    self.choice = 3  #GOES INTO CAMP CHOICE
                else:
                    self.day_state = 1
                    self.choice = 2
                    self.option3.color = 6

    def draw(self):
        # CLEAR SCREEN
        pyxel.cls(0)

        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)

        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)
        
        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option1.y, "Go North", 3)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(10, self.option2.y, "See what's in the west", 4)
        pyxel.rect(self.option3.x, self.option3.y, self.option3.side, self.option3.side, self.option3.color)
        pyxel.text(10, self.option3.y, "Make Camp", 5)

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
                pyxel.text(2, 182, "You camped too early! A day is wasted. You will lose more inventory.", 7)
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

        

App()