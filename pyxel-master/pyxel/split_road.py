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
        
        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if(pyxel.mouse_x > self.option1_r.x and pyxel.mouse_x < (self.option1_r.x + self.option1_r.side) and pyxel.mouse_y > self.option1_r.y and pyxel.mouse_y < (self.option1_r.y + self.option1_r.side)):
                if(self.option1_r.color == 6):
                    self.option1_r.color = 0
                    pyxel.image(0).load(0, 0, "assets/forest.png")
                else:
                    self.option1_r.color = 6
                    pyxel.image(0).load(0, 0, "assets/sunset.png")
            if(pyxel.mouse_x > self.option2_r.x and pyxel.mouse_x < (self.option2_r.x + self.option2_r.side) and pyxel.mouse_y > self.option2_r.y and pyxel.mouse_y < (self.option2_r.y + self.option2_r.side)):
                if(self.option2_r.color == 6):
                    self.option2_r.color = 0
                    pyxel.image(0).load(0, 0, "assets/lake.png")
                else:
                    self.option2_r.color = 6
                    pyxel.image(0).load(0, 0, "assets/sunset.png")
            if(pyxel.mouse_x > self.option3_r.x and pyxel.mouse_x < (self.option3_r.x + self.option3_r.side) and pyxel.mouse_y > self.option3_r.y and pyxel.mouse_y < (self.option3_r.y + self.option3_r.side)):
                if(self.option3_r.color == 6):
                    self.option3_r.color = 0
                else:
                    self.option3_r.color = 6

    def draw(self):
        # CLEAR SCREEN
        pyxel.cls(0)

        # BACKGROUND
        # blt(x, y, img, u, v, w, h, [colkey]) colkey is optional
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)

        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        pyxel.text(2, 182, "DAY 2 - EVENING - BANFF, ALBERTA", 1)
        pyxel.text(2, 189, "", 2)

        # OPTIONS
        # pyxel.text(2, 232, str(self.option1_r.y), pyxel.frame_count % 16)
        pyxel.rect(self.option1_r.x, self.option1_r.y, self.option1_r.side, self.option1_r.side, self.option1_r.color)
        pyxel.text(10, self.option1_r.y, "This is option 1", 3)
        pyxel.rect(self.option2_r.x, self.option2_r.y, self.option2_r.side, self.option2_r.side, self.option2_r.color)
        pyxel.text(10, self.option2_r.y, "This is option 2", 4)
        pyxel.rect(self.option3_r.x, self.option3_r.y, self.option3_r.side, self.option3_r.side, self.option3_r.color)
        pyxel.text(10, self.option3_r.y, "This is option 3", 5)  

App()