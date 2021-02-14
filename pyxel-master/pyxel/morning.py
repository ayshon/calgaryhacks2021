# This is the scene of the second morning
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
        pyxel.image(0).load(0, 0, "assets/morning.jpg")
        
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
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        
        # DRAW BLACK TEXTBOX
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)

        # TEXT
        pyxel.text(2, 188, "It's March 16, 1901.", 7)
        pyxel.text(2, 204, "You can hear the birds chiriping outside.", 7)
        pyxel.text(2, 214, "You yawn and stretch your stiff limbs.", 7)
        
        pyxel.text(2, 228, "It's time to move.", 7)

        # NOTE: REQUIRES CODE TO TRANSITION INTO NEXT SCENE

App()