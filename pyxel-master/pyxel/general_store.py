import pyxel

class Option:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

class App:
    def __init__(self):
        pyxel.init(256, 256, caption="General Store", fullscreen=True)
        pyxel.image(0).load(0, 0, "assets/store.jpg")
        
        pyxel.mouse(True)

        self.inventory = ["Compass", "Cash" "Painting Supplies"]
        self.cart = [[],[]]
        self.cash = 100
        self.option1 = Option(2,200,5,7)
        self.option2 = Option(2,210,5,7)
        self.option3 = Option(2,220,5,7)
        self.option4 = Option(2,230,5,7)
        self.gender = 1
        self.storeText = 0
        self.cartText = 0
        
        # EVERYTHING MUST BE ABOVE THIS LINE
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            self.storeText = 0
            self.cartText = 0
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            if(pyxel.mouse_x > self.option1.x and pyxel.mouse_x < (self.option1.x + self.option1.side) and pyxel.mouse_y > self.option1.y and pyxel.mouse_y < (self.option1.y + self.option1.side)):
                if(self.storeText == 1):
                    self.cash -= 2
                    if("Maple Syrup" not in self.cart[0]):
                        self.cart[0].append("Maple Syrup")
                        self.cart[1].append(1)
                    else:
                        self.cart[1][self.cart[0].index("Maple Syrup")] += 1
                self.storeText = 1
            if(pyxel.mouse_x > self.option2.x and pyxel.mouse_x < (self.option2.x + self.option2.side) and pyxel.mouse_y > self.option2.y and pyxel.mouse_y < (self.option2.y + self.option2.side)):
                if(self.storeText == 1):
                    self.cash -= 2
                self.storeText = 1
            if(pyxel.mouse_x > self.option4.x and pyxel.mouse_x < (self.option4.x + self.option4.side) and pyxel.mouse_y > self.option4.y and pyxel.mouse_y < (self.option4.y + self.option4.side)):
                if(self.cartText == 0):
                    self.cartText = 1 
                else:
                    self.cartText = 0

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
        if(self.gender == 1):
            self.genderText = "guy"
        elif(self.gender == 2):
            self.genderText = "gal"
        else:
            self.genderText = "pal"

        pyxel.text(2, 182, "\"Mornin', what will a young " + self.genderText + " like yourself be buying today?\" the shopkeeper says gruffly.", 7)

        # OPTIONS
        # pyxel.text(2, 232, str(self.option1.y), pyxel.frame_count % 16)
        # One letter - 5x4
        # Where the remaining cash amount will be.
        pyxel.rect(200, 0, 56, 10, 13)
        pyxel.rectb(200, 0, 56, 10, 0)
        pyxel.text(202, 3, "Cash:$" + str(self.cash), 0)

        pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option1.y, "Food", 3)
        pyxel.rect(self.option1.x, self.option2.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option2.y, "Clothing", 3)
        pyxel.rect(self.option1.x, self.option3.y, self.option1.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option3.y, "Supplies", 3)
        pyxel.rect(self.option1.x, self.option4.y, self.option4.side, self.option1.side, self.option1.color)
        pyxel.text(10, self.option4.y, "Check your basket", 3)

        if(self.storeText == 1):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"This is all the grub I have. Should keep your stomach filled.\"", 7)
            pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option1.y, "Maple Syrup - $2", 2)
            pyxel.rect(self.option1.x, self.option2.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option2.y, "Bread - $5", 2)
            pyxel.rect(self.option1.x, self.option3.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option3.y, "Canned Beans - $10", 2)
            pyxel.rect(self.option1.x, self.option4.y, self.option4.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option4.y, "Canadian Bacon - $25", 2)
            # pyxel.text(2, 240, self.cart[0][0] + " - " + str(self.cart[1][0]), 11)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)


        if(self.cartText == 1):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "Cart:", 7)
            tempColumn = 190
            for j in range(len(self.cart[0])):
                pyxel.text(2, tempColumn, str(self.cart[0][j]) + " - " + str(self.cart[1][j]), 11)
                tempColumn += 8

App()