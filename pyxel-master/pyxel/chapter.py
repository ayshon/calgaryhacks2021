# This scene happens after the title page
# This is the scene after the morning scene
import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="chapterselect", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/camp.png")
        
        pyxel.mouse(True)

        self.option1 = Option(10,206,5,12)
        self.option2 = Option(10,216,5,12)
        self.option3 = Option(10, 226, 5, 12)
        self.option4 = Option(10, 236, 5, 12)

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if(pyxel.mouse_x > self.option1.x and pyxel.mouse_x < (self.option1.x + self.option1.side) and pyxel.mouse_y > self.option1.y and pyxel.mouse_y < (self.option1.y + self.option1.side)):
                if(self.option1.color == 12):
                    self.option1.color = 0
                    # pyxel.image(0).load(0, 0, "assets/forest.png") REPLACE WITH CONSEQUENCE
                else:
                    self.option1.color = 12
                    pyxel.image(0).load(0, 0, "assets/sunset.png")
            if(pyxel.mouse_x > self.option2.x and pyxel.mouse_x < (self.option2.x + self.option2.side) and pyxel.mouse_y > self.option2.y and pyxel.mouse_y < (self.option2.y + self.option2.side)):
                if(self.option2.color == 12):
                    self.option2.color = 0
                    # pyxel.image(0).load(0, 0, "assets/lake.png")
                    self.gender = 1
            if(pyxel.mouse_x > self.option3.x and pyxel.mouse_x < (self.option3.x + self.option3.side) and pyxel.mouse_y > self.option3.y and pyxel.mouse_y < (self.option3.y + self.option3.side)):
                if(self.option3.color == 12):
                    self.option3.color = 0
                    # pyxel.image(0).load(0, 0, "assets/lake.png")
                    self.gender = 1
            if(pyxel.mouse_x > self.option4.x and pyxel.mouse_x < (self.option4.x + self.option4.side) and pyxel.mouse_y > self.option4.y and pyxel.mouse_y < (self.option4.y + self.option4.side)):
                if(self.option4.color == 12):
                    self.option4.color = 0
                    # pyxel.image(0).load(0, 0, "assets/lake.png")
            else:
                    self.option2.color = 12
                    # pyxel.image(0).load(0, 0, "assets/sunset.png")

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

        # OPTIONS
        # pyxel.text(2, 232, str(self.option1.y), pyxel.frame_count % 16)
        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(20, self.option1.y, "Forest", 2)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(20, self.option2.y, "Lake             [Locked]", 8)
        pyxel.rect(self.option3.x, self.option3.y, self.option3.side, self.option3.side, self.option3.color)
        pyxel.text(20, self.option3.y, "Mountain         [Locked]", 8)
        pyxel.rect(self.option4.x, self.option4.y, self.option4.side, self.option4.side, self.option4.color)
        pyxel.text(20, self.option4.y, "The Great Lakes  [Locked]", 8)

        pyxel.text(6, 192, "Chapter Select", 7)

App()