import pyxel
import time

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="Title", fullscreen=True)
        pyxel.image(1).load(0, 0, "assets/endcard.png")

        pyxel.mouse(True)

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
        pyxel.blt(0, 0, 1, 0, 0, 256, 256)
        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.text(0, 190,
        """
          Congratulations! You have painted Lake Louise!
                       What a masterpiece!
        """, 7)
    
App()