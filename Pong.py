
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
keys = ["w", "s", "up arrow", "down arrow"]

class Ball(Sprite):
    b = RectangleAsset(20, 20, noline, white)
    def __init__(self, posistion):
        super().__init__(Ball.b, posistion)
        self.pointasset = SoundAsset("sounds/point1.mp3")
        self.popasset = SoundAsset("sounds/pop1.mp3")
        self.pop = Sound(self.popasset)
        self.point = Sound(self.pointasset)
        
        if round(randint(0,1)) == 1:
            self.vx = 4
        else:
            self.vx = -4
            
        if round(randint(0,1)) == 1:
            self.vy = 3
        else:
            self.vy = -3

    def step(self):
        print(self.vx)
        self.x += self.vx
        self.y += self.vy
        
        if self.y < 1:
            self.vy *= -1
        elif self.y > Pong.height-20:
            self.vy *= -1
            
        if self.x < 0:
            Pong.p2s += 1
            self.point.play()
            del Pong.balll[0]
            self.destroy()
        elif self.x > Pong.width-20:
            Pong.p1s += 1
            self.point.play()
            del Pong.balll[0]
            self.destroy()
            
        self.pcollide = self.collidingWithSprites(Paddle)
        if len(self.pcollide):
            self.pop.play()
            self.vx = (abs(self.vx)+0.5)
            self.vy = randint(-3,3)
            
        self.pcollide = self.collidingWithSprites(RightPaddle)
        if len(self.pcollide):
            self.pop.play()
            self.vx = ((abs(self.vx)+0.5)*-1)
            self.vy = randint(-3,3)
            
class Numbers(Sprite):
    n = ImageAsset("images/numbers4.png",
    Frame(0,0,50,68), 11, 'horizontal')
    def __init__(self, posistion):
        super().__init__(Numbers.n, posistion)
        p1s = 0
        self.change = 0
        self.setImage(8)
        Pong.listenKeyEvent("keyup", "o", self.oldnum)
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
        self.vy2 = 0
        for i in keys:
            Pong.listenKeyEvent("keydown", i, self.press)
            Pong.listenKeyEvent("keyup", i, self.stop)
            
    def press(self,event):
        if event.key == "up arrow":
            self.vy2 = -5
        elif event.key == "down arrow":
            self.vy2 = 5
        elif event.key == "w":
            self.vy = -5
        elif event.key == "s":
            self.vy = 5

    def stop(self, event):
        if event.key == "up arrow":
            self.vy2 = 0
        elif event.key == "down arrow":
            self.vy2 = 0
        else:
            self.vy = 0

    def step(self):
        self.y += self.vy
        if self.y > Pong.height-20:
            self.y = Pong.height-20
        elif self.y < 0:
            self.y = 0

class RightPaddle(Paddle):

    def step(self):
        self.y += self.vy2
        if self.y > Pong.height-20:
            self.y = Pong.height-20
        elif self.y < 0:
            self.y = 0

class Pong(App):
    p1s = 8
    p2s = 8
    balll = []
    def __init__(self):
        super().__init__()
        bg_main = RectangleAsset(self.width, self.height, noline, black)
        bg_center =  RectangleAsset(5, round(self.height/40), noline, white)
        bg_top = RectangleAsset(self.width, 20, noline, white)
        bg = Sprite(bg_main, (0,0))
        Numbers((self.width/2-100, 100))
        Leftnum((self.width/2+100, 100))
        Paddle((50,self.height/2))
        RightPaddle((900,self.height/2))
        for i in range(round(self.height/20)):
            bg = Sprite(bg_center, (self.width/2-5, i*35))

        Pong.listenKeyEvent("keydown", "space", self.placeball)
    
    def placeball(self, event):
        if len(self.balll) == 0:
            self.balll.append(Ball((self.width/2, randint(100, self.height-75))))
        
    def step(self):
        for n in self.getSpritesbyClass(Numbers):
            n.step(self.p1s)
            
        for n in self.getSpritesbyClass(Leftnum):
            n.step(self.p2s)
            
        for p in self.getSpritesbyClass(Paddle):
            p.step()
        
        for p in self.getSpritesbyClass(RightPaddle):
            p.step()

        if len(self.balll) == 1:
            for b in self.getSpritesbyClass(Ball):
                b.step()

myApp = Pong()
myApp.run()