# Caribou consequence
# This is the scene following the tracks scenario
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
        pyxel.init(256, 256, caption="gender", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/fall.jpg")
        
        pyxel.mouse(True)

        self.page = 0

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
        if (self.page == 0):      
            pyxel.text(4, 186, "This is the first time you've seen such a beautiful animal up", 7)
            pyxel.text(4, 196, "close. You have to get closer to it, drink in all the details,", 7)
            pyxel.text(4, 206, "else you'd never be able to pick up your paintbrush again!", 7)
            pyxel.text(4, 216, "You slink behind a tree and squat down. The caribou stands", 7)
            pyxel.text(4, 226, "still for a moment longer before dipping its head back.", 7)
            pyxel.text(4, 236, "into the water. You swallow your nervousness before", 7)
            pyxel.text(4, 246, "slipping out of your hiding place.", 7)         
            
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):  
                self.page = 1


        if (self.page == 1 or self.page == 2):
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) == False:                            
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

        if (self.page == 2 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)):
            self.page = 3
            
        if (self.page == 3):  
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

App()