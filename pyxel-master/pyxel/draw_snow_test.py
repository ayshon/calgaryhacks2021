from random import randint

import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Pyxel Jump")

        pyxel.load("assets/backpack.pyxres")
        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0
        self.player_is_alive = True

        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        self.floor = [(i * 60, randint(8, 104), True) for i in range(4)]
        self.fruit = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]

        pyxel.playm(0, loop=True)

        a = "c3d2e2b3 a2b2c3b2"
        b = "c3d2e2a3 a2b2c3a2"
        pyxel.sound(0).set(a * 3 + b * 1, "t", "2", "nf", 30)
        pyxel.sound(1).set("a1b1b1a1", "p", "2", "nf", 120)

        #pyxel.play(0, 0, loop=True)
        #pyxel.play(1, 1, loop=True)


        pyxel.sound(2).set("c3g3c4g3", "p", "1", "nf", 150)
        pyxel.sound(3).set("c1d1e1d1 c2d2e2a1", "t", "2", "nf", 100) # 階段
        pyxel.play(2,2,loop=True)
        pyxel.play(3,3,loop=True)

        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


    def draw(self):
        pyxel.cls(12)

        # draw backpack
        pyxel.blt(0, 0, 0, 0, 0, 160, 120)

App()