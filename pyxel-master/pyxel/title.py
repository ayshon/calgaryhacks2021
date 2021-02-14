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
        pyxel.image(0).load(0, 0, "assets/group_of_seven.jpg")
        pyxel.image(1).load(0, 0, "assets/sunset.png")
        pyxel.image(2).load(0, 0, "assets/title.png")
        
        pyxel.mouse(True)

        self.option1 = Option(2,200,5,12)
        self.option2 = Option(102,200,5,12)
        
        self.blurbText = 0

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_ENTER):
            # transition
            self.blurbText = 1

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
              Press ENTER to begin your adventure...
        """, 7)


        if(self.blurbText == 1):
        # TEXT
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
            pyxel.text(0, 185, 
        """
        A group of Canadian artists built their fame across 
         Canada for their paintings inspired by Canada's
            beautiful landscape. Famously known as the
          'Group of Seven,' they have left their legacy
            in their world through their masterpieces. 
        But unbeknownst to some others, there was an eighth 
           person, one who aspired to leave their mark 
                  on Canadian soil as well.
                  """, 7)
    
App()