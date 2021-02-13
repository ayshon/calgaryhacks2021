import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="Evening", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/sunset.png")
        pyxel.mouse(True)

        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        # rect(x, y, w, h, col)
        pyxel.rect(0, 180, 256, 76, 0)
        pyxel.text(2, 182, "There is text here gotem", pyxel.frame_count % 16)
        pyxel.text(2, 189, "There is text here too very cool stuff very nice", pyxel.frame_count % 16)
        self.test_text(2, 200)

    def test_text(self, x, y):
        pyxel.text(x, y, "text(x,y,s,col)", 7)

        x += 4
        y += 8
        s = "Elapsed frame count is {}\n" "Current mouse position is ({},{})".format(
            pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y
        )

        pyxel.text(x + 1, y, s, 1)
        pyxel.text(x, y, s, 9)

App()