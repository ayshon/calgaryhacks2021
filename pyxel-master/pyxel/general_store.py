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
                    elif(self.storeText == 2):
                        self.cash -= 3
                        if("Mittens" not in self.cart[0]):
                            self.cart[0].append("Mittens")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Mittens")] += 1
                        self.storeText = 2
                    elif(self.storeText == 3):
                        self.cash -= 20
                        if("Fishing Rod" not in self.cart[0]):
                            self.cart[0].append("Fishing Rod")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Fishing Rod")] += 1
                        self.storeText = 3
                    self.storeText = 1
            if(pyxel.mouse_x > self.option2.x and pyxel.mouse_x < (self.option2.x + self.option2.side) and pyxel.mouse_y > self.option2.y and pyxel.mouse_y < (self.option2.y + self.option2.side)):
                    if(self.storeText == 1):
                        self.cash -= 5
                        if("Bread" not in self.cart[0]):
                            self.cart[0].append("Bread")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Bread")] += 1
                        self.storeText = 1
                    elif(self.storeText != 1 or self.storeText != 3 or self.storeText != 4):
                        self.cash -= 7
                        if("Toque" not in self.cart[0]):
                            self.cart[0].append("Toque")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Toque")] += 1
                        self.storeText = 2
                    elif(self.storeText != 1 or self.storeText !=2  or self.storeText != 4):
                        self.cash -= 25
                        if("Medicine" not in self.cart[0]):
                            self.cart[0].append("Medicine")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Medicine")] += 1
                        self.storeText = 3
            if(pyxel.mouse_x > self.option3.x and pyxel.mouse_x < (self.option3.x + self.option3.side) and pyxel.mouse_y > self.option3.y and pyxel.mouse_y < (self.option3.y + self.option3.side)):
                    if(self.storeText == 1):
                        self.cash -= 10
                        if("Canned Beans" not in self.cart[0]):
                            self.cart[0].append("Cannned Beans")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Canned Beans")] += 1
                        self.storeText = 1
                    elif(self.storeText != 1 or self.storeText != 3 or self.storeText != 4):
                        self.cash -= 12
                        if("Boots" not in self.cart[0]):
                            self.cart[0].append("Boots")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Boots")] += 1
                        self.storeText = 2
                    elif(self.storeText != 1 or self.storeText !=2  or self.storeText != 4):
                        self.cash -= 30
                        if("Trap" not in self.cart[0]):
                            self.cart[0].append("Trap")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Trap")] += 1
                        self.storeText = 3
            if(pyxel.mouse_x > self.option4.x and pyxel.mouse_x < (self.option4.x + self.option4.side) and pyxel.mouse_y > self.option4.y and pyxel.mouse_y < (self.option4.y + self.option4.side)):
                    if(self.storeText == 1):
                        self.cash -= 10
                        if("Canadian Bacon" not in self.cart[0]):
                            self.cart[0].append("Canadian Bacon")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Canadian Bacon")] += 1
                        self.storeText = 1
                    elif(self.storeText != 1 or self.storeText != 3 or self.storeText != 4):
                        self.cash -= 12
                        if("Coat" not in self.cart[0]):
                            self.cart[0].append("Coat")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Coat")] += 1
                        self.storeText = 2
                    elif(self.storeText != 1 or self.storeText !=2  or self.storeText != 4):
                        self.cash -= 30
                        if("Tent" not in self.cart[0]):
                            self.cart[0].append("Tent")
                            self.cart[1].append(1)
                        else:
                            self.cart[1][self.cart[0].index("Tent")] += 1
                        self.storeText = 3

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
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        elif(self.storeText == 2):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"Should keep yourselves warm. Gets pretty chilly here in Banff.\"", 7)
            pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option1.y, "Mittens - $3", 2)
            pyxel.rect(self.option1.x, self.option2.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option2.y, "Toque - $7", 2)
            pyxel.rect(self.option1.x, self.option3.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option3.y, "Boots - $12", 2)
            pyxel.rect(self.option1.x, self.option4.y, self.option4.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option4.y, "Coat - $20", 2)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        elif(self.storeText == 3):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "\"Ahh, you're one of those hiker folk. Got quality supplies here.\"", 7)
            pyxel.rect(self.option1.x, self.option1.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option1.y, "Fishing Rod - $20", 2)
            pyxel.rect(self.option1.x, self.option2.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option2.y, "Medicine - $25", 2)
            pyxel.rect(self.option1.x, self.option3.y, self.option1.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option3.y, "Trap - $30", 2)
            pyxel.rect(self.option1.x, self.option4.y, self.option4.side, self.option1.side, self.option1.color)
            pyxel.text(10, self.option4.y, "Tent - $50", 2)
            pyxel.text(2, 250, "Press R to return to General Store - Main.", 2)

        if(self.cartText == 1):
            pyxel.rect(0, 180, 256, 76, 0)
            pyxel.text(2, 182, "Cart:", 7)
            tempColumn = 190
            for i in self.cart:
                for j in self.cart[i][j]:
                    pyxel.text(2, tempColumn, self.cart[i][j] + " - " + str(self.cart[i][j]), 11)




App()