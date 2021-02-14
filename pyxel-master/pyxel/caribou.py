import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="gender", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/caribou.png")
        
        pyxel.mouse(True)

        self.option1 = Option(66,242,5,12)
        self.option2 = Option(146,242,5,12)
        
        self.activeBank = 0
        self.gender = 0

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
                else:
                    self.option2.color = 12
                    # pyxel.image(0).load(0, 0, "assets/sunset.png")
                    #self.gender = 1

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
        pyxel.text(76, self.option1.y, "Go closer", 2)
        pyxel.rect(self.option2.x, self.option2.y, self.option2.side, self.option2.side, self.option2.color)
        pyxel.text(156, self.option2.y, "Stay still", 8)

        pyxel.text(2, 188, "You followed the tracks and it led you to a small creek where", 7)
        pyxel.text(2, 198, "you spot a caribou drinking from the clear waters. Its horns ", 7)
        pyxel.text(2, 208, "are long and curved. It lifts its head up upon your approach.", 7)
        pyxel.text(2, 218, "The majestic creature shifts nervously, and upon closer", 7)
        pyxel.text(2, 228, "inspection, you can see that its fur is matted with blood.", 7)

App()