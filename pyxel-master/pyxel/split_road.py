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

        self.option1_r = Option(2,232,5,6)
        self.option2_r = Option(2,240,5,6)
        self.option3_r = Option(2,248,5,6)
        self.split_road_state = 1
        
        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):

        if pyxel.btnp(pyxel.KEY_ENTER) and self.split_road_state ==4:
            pyxel.quit()
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if(pyxel.mouse_x > self.option1_r.x and pyxel.mouse_x < (self.option1_r.x + self.option1_r.side) and pyxel.mouse_y > self.option1_r.y and pyxel.mouse_y < (self.option1_r.y + self.option1_r.side)):
                if(self.option1_r.color == 6):
                    if self.split_road_state == 1:
                        self.split_road_state = 2
                        pyxel.image(0).load(0, 0, "assets/twopaths.jpg")
                    else:
                        self.option1_r.color = 0
                        pyxel.image(0).load(0, 0, "assets/drive2.jpg")
                        self.split_road_state =3
                else:
                    self.option1_r.color = 6

            if(pyxel.mouse_x > self.option2_r.x and pyxel.mouse_x < (self.option2_r.x + self.option2_r.side) and pyxel.mouse_y > self.option2_r.y and pyxel.mouse_y < (self.option2_r.y + self.option2_r.side)):
                if(self.option2_r.color == 6):
                    self.option2_r.color = 0
                    pyxel.image(0).load(0, 0, "assets/lost.jpg")
                else:
                    self.option2_r.color = 6
                    pyxel.image(0).load(0, 0, "assets/twopaths.jpg")

    def draw(self):
        # CLEAR SCREEN
        pyxel.cls(0)

        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)

        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)

        if self.split_road_state == 2:
        # TEXT
            pyxel.text(2, 182, "DAY 2 - EVENING - BANFF, ALBERTA\n\n", 7)
            pyxel.text(2, 189, "You see two paths, one leads north, the other leads north west. \nThe north road looks dangerous.\nWhich way do you go?", 7)

            # OPTIONS
            pyxel.rect(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
            pyxel.text(10, self.option1_r.y, "Go North Road", 3)
            pyxel.rect(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
            pyxel.text(10, self.option2_r.y, "Go Nort West Road", 4)

        elif self.split_road_state ==1:
            pyxel.text(2, 182, "Day 2 - EVENING - March 16, 1901 - Banff, Alberta", 7)
            pyxel.text(2, 189, "It's 6pm, in the evening. Where would you like to go?", 7)

            # OPTIONS
            pyxel.rect(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
            pyxel.text(10, self.option1_r.y, "Go North", 3)
            pyxel.rect(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
            pyxel.text(10, self.option2_r.y, "Go West", 4)
            pyxel.rect(self.option3_r.x, self.option3_r.y, self.option3_r.side, self.option3_r.side, self.option3_r.color)
            pyxel.text(10, self.option3_r.y, "Make Camp", 5)
        
        elif self.split_road_state == 3 or self.split_road_state == 4:
            pyxel.text(2, 182, "You were found in the morning passed out from the darkness!", 7)
            pyxel.text(2, 189, "Fortunately, some kind strangers saw you on the road and \n offered to take you where you need to go! \n\n\nPress ENTER to continue", 7)
            self.split_road_state = 4
App()