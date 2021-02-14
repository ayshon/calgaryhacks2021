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
        
        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.Any):
            pyxel.quit()
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

        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        pyxel.text(2, 182, "There is text here gotem", 1)
        pyxel.text(2, 189, "There is text here too very cool stuff very nice", 2)
        self.test_text(2, 200)

        # OPTIONS
        # pyxel.text(2, 232, str(self.option1.y), pyxel.frame_count % 16)
        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option1.y, "This is option 1", 3)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(10, self.option2.y, "This is option 2", 4)
        pyxel.rect(self.option3.x, self.option3.y, self.option3.side, self.option3.side, self.option3.color)
        pyxel.text(10, self.option3.y, "This is option 3", 5)

    def test_text(self, x, y):
        pyxel.text(x, y, "text(x,y,s,col)", 7)

        x += 4
        y += 8
        s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
            pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
        )

        pyxel.text(x + 1, y, s, 1)
        pyxel.text(x, y, s, 9)
        # pyxel.rect(0, 20, 20, 20, pyxel.frame_count % 16)        

App()