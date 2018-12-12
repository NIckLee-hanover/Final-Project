
"""
lines 4-33 copied from lvl 3 for ease.

Pong.py
Author: Nick Lee
Credit: some level 3 snippets for sound, sprite documentation and things
Assignment: Final Project
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame.timer import Timer
from ggame import (App, Color, LineStyle, Sprite, RectangleAsset,
    CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, SoundAsset, Sound, Frame)
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
grid = RectangleAsset(30,30,gridline,white)

class Ball(Sprite):
    popasset = SoundAsset("sounds/pop.mp3")
    b = RectangleAsset(20, 20, noline, white)
    def __init__(self, posistion):
        super().__init__(Ball.b, posistion)
        self.pop = Sound(self.popasset)
        self.pop.volume = 10
        if round(randint(0,1)) == 1:
            self.vx = 4
        else:
            self.vx = -4
        if round(randint(0,1)) == 1:
            self.vy = 3
        else:
            self.vy = -3
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.y < 0 or self.y > Pong.height-20:
            self.vy *= -1
        if self.x < 0:
            Pong.p2s += 1
            del Pong.balll[0]
            self.destroy()
        elif self.x > Pong.width-20:
            Pong.p1s += 1
            del Pong.balll[0]
            self.pop.play()
            self.destroy()
        
        
class Numbers(Sprite):
    n = ImageAsset("images/numbers4.png",
    Frame(0,0,50,68), 11, 'horizontal')
    def __init__(self, posistion):
        super().__init__(Numbers.n, posistion)
        p1s = 0
        self.change = 0
        self.setImage(8)
        Pong.listenKeyEvent("keyup", "o", self.oldnum)#
        Pong.listenKeyEvent("keyup", "i", self.newnum)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self, num):
        self.setImage(num)
        if Pong.p1s == 10:
            Pong.p1s = 0
        if Pong.p2s == 10:
            Pong.p2s = 0

    def oldnum(self, event):
        Pong.p1s += 1
        print(Pong.p1s)
        
    def newnum(self, event):
        Pong.p2s += 1
        
class Leftnum(Numbers):
    def step(self, num):
        self.setImage(num)

class Paddle(Sprite):
    p = RectangleAsset(10, 20, noline, white)
    def __init__(self, posistion):
        super().__init__(Paddle.p, posistion)
        self.vy = 0
        Pong.listenKeyEvent("keydown", "up arrow", self.press)
        Pong.listenKeyEvent("keydown", "down arrow", self.press)
        Pong.listenKeyEvent("keyup", "up arrow", self.stop)
        Pong.listenKeyEvent("keyup", "down arrow", self.stop)

    def press(self,event):
        if event.key == "up arrow":
            self.vy = 3
        elif event.key == "down arrow":
            self.vy = -3
    def stop(self, event):
        self.vy = 0
    def step(self):
        self.y += self.vy
        if self.y > Pong.height-20:
            self.vy = 0
        elif self.y < 0:
            self.vy = 0
            
        
        
        
class Pong(App):
    p1s = 8
    p2s = 8
    balll = []
    ballalive = 0
    drawball = 0
    def __init__(self):
        super().__init__()

        bg_main = RectangleAsset(self.width, self.height, noline, black)
        bg_center =  RectangleAsset(5, round(self.height/40), noline, white)
        bg_top = RectangleAsset(self.width, 20, noline, white)
        bg = Sprite(bg_main, (0,0))
        Numbers((self.width/2-100, 100))
        Leftnum((self.width/2+100, 100))
        paddle((100,100))
        for i in range(round(self.height/20)):
            bg = Sprite(bg_center, (self.width/2-5, i*35))

        Pong.listenKeyEvent("keydown", "space", self.placeball)
    
    def placeball(self, event):
        if len(self.balll) == 0:
            self.balll.append(Ball((self.width/2-5, randint(100, self.height-75))))
        
    def step(self):
        for n in self.getSpritesbyClass(Numbers):
            n.step(self.p1s)
        for n in self.getSpritesbyClass(Leftnum):
            n.step(self.p2s)
        for p in self.getSpritesbyClass(Paddle):
            p.step()
        if len(self.balll) == 1:
            for i in self.balll:
                i.step()








myApp = Pong()
myApp.run()