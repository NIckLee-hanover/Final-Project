
"""
lines 4-33 copied from lvl 3 for ease.

Pong.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from random import randint
blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

class Ball(Sprite):
    b = RectangleAsset(12, 12, noline, white)
    def __init__(self, posistion):
        super().__init__(Ball.b, posistion)
        






class Pong(App):
    def __init__(self):
        super().__init__()
        bg_main = RectangleAsset(self.width, self.height, noline, black)
        bg_center =  RectangleAsset(10, round(self.height/40), noline, white)
        bg_top = RectangleAsset(self.width, 20, noline, white)
        bg = Sprite(bg_main, (0,0))
        #bg = Sprite(bg_top, (0, 100))
        print(round(self.height/20))
        for i in range(round(self.height/20)):
            bg = Sprite(bg_center, (self.width/2, i*40))
        #bg = Sprite(bg_center, (self.width/2, 100))

        Pong.listenKeyEvent("keydown", "space", self.placeball)
    
    
    def placeball(self, event):
        Ball((self.width/2, randint(100, self.height)))











myApp = Pong()
myApp.run()