import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 256, caption="Sunset")
        pyxel.image(0).load(0, 0, "assets/sunset.png")
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
App()