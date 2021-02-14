import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="Evening", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/forest.png")
        pyxel.mouse(True)

        self.name = ""

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw_name)
        
    def update(self):
        if len(self.name) < 15:
            if pyxel.btnp(pyxel.KEY_BACKSPACE) and self.name != "":
                self.name = self.name[:-1]
            if pyxel.btnp(pyxel.KEY_A):
                self.name += 'A'
            if pyxel.btnp(pyxel.KEY_B):
                self.name += 'B'
            if pyxel.btnp(pyxel.KEY_C):
                self.name += 'C'
            if pyxel.btnp(pyxel.KEY_D):
                self.name += 'D'
            if pyxel.btnp(pyxel.KEY_E):
                self.name += 'E'
            if pyxel.btnp(pyxel.KEY_F):
                self.name += 'F'
            if pyxel.btnp(pyxel.KEY_G):
                self.name += 'G'
            if pyxel.btnp(pyxel.KEY_H):
                self.name += 'H'
            if pyxel.btnp(pyxel.KEY_I):
                self.name += 'I'
            if pyxel.btnp(pyxel.KEY_J):
                self.name += 'J'
            if pyxel.btnp(pyxel.KEY_K):
                self.name += 'K'
            if pyxel.btnp(pyxel.KEY_L):
                self.name += 'L'
            if pyxel.btnp(pyxel.KEY_M):
                self.name += 'M'
            if pyxel.btnp(pyxel.KEY_N):
                self.name += 'N'
            if pyxel.btnp(pyxel.KEY_O):
                self.name += 'O'
            if pyxel.btnp(pyxel.KEY_P):
                self.name += 'P'
            if pyxel.btnp(pyxel.KEY_Q):
                self.name += 'Q'
            if pyxel.btnp(pyxel.KEY_R):
                self.name += 'R'
            if pyxel.btnp(pyxel.KEY_S):
                self.name += 'S'
            if pyxel.btnp(pyxel.KEY_T):
                self.name += 'T'
            if pyxel.btnp(pyxel.KEY_U):
                self.name += 'U'
            if pyxel.btnp(pyxel.KEY_V):
                self.name += 'V'
            if pyxel.btnp(pyxel.KEY_W):
                self.name += 'W'
            if pyxel.btnp(pyxel.KEY_X):
                self.name += 'X'
            if pyxel.btnp(pyxel.KEY_Y):
                self.name += 'Y'
            if pyxel.btnp(pyxel.KEY_Z):
                self.name += 'Z'
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.name += ' '
        # if pyxel.btnp(pyxel.KEY_ENTER):
        #         # go to next scene

    def draw_name(self):
        # CLEAR SCREEN
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        pyxel.rect(60, 102, 137, 70, 0)
        pyxel.text(95, 118, "Type in your name", 7)
        pyxel.text(100, 130, self.name, 7)
        nameLength = len(self.name)
        underScores = ""
        for i in range(15):
                underScores += "_"
        pyxel.text(100, 132, underScores, 7)
        pyxel.text(85, 150, "Press ENTER to confirm", 7)

    #THERES A BUG: CAN'T BACKSPACE IF YOU EXCEED THE LETTER COUNT
App()