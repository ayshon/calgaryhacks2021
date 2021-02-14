# This is the end of day campire scene.
import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="endofday", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/camp.png")
        
        pyxel.mouse(True)
        
        self.activeBank = 0
        self.gender = 0
        self.inventory = [["Canadian Bacon", 2], ["Dummy", 1]]
        self.status = 0  # ENSURES INVENTORY IS ONLY UPDATED ONCE
        self.consumed = 0 # WHAT WAS EATEN

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

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
        if (self.status < 1):
            self.consumed = self.inventory[0][0]

        pyxel.text(2, 188, "You have decided to make camp and rest for the next day.", 7)
        pyxel.text(2, 198, "You have decided to eat one " + self.consumed + ".", 7)

        pyxel.text(2, 212, "Changes in inventory:", 7)
        pyxel.text(2, 222, "-" + self.consumed + "      -1", 7)

        pyxel.text(2, 238, "Click anywhere to continue.", 7)
        # NOTE: REQUIRES CODE TO TRANSITION INTO NEXT SCENE

        if(self.status < 1):
            self.inventory[0][1] -= 1
            if (self.inventory[0][1] == 0):
                self.inventory.pop(0)
        self.status = 1

App()