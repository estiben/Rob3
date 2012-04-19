import pygame, sys, os
import math
import Util
import Groups
import Globals
from pygame.locals import *

class GameObj(pygame.sprite.Sprite):
    def __init__(self, x, y, depth=0):
        super(GameObj, self).__init__()
        self.__index = 0
        self.__xspd = 0
        self.__yspd = 0
        self.__speed = 0
        self.__direction = 0
        self.__sprite = 0
        self.__depth = 0

        #List of surfaces to combine into the final image
        self.__drawList = {} 

        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(x, y, 0, 0)

        self.add(Groups.grp_AllSprites)

        self.setXY((x, y))
        self.setDepth(depth)

    def setXY(self, xy):
        #World xy coordinates
        self.__xy = xy

    def setX(self, x):
        self.__xy = (x, self.getY())

    def setY(self, y):
        self.__xy = (self.getX(), y)

    def getXY(self):
        return self.__xy

    def getX(self):
        return self.__xy[0]

    def getY(self):
        return self.__xy[1]

    def setHitRect(self, newRect):
        self.__hitRect = newRect

    def getIndex(self):
        return self.__index

    def setYSpd(self, spd):
        self.__yspd = spd
        self.__speed = math.sqrt(self.__xspd**2 + self.__yspd**2)
        self.__direction = Util.point_direction(self.__xy, (self.__xspd, self.__yspd))

    def getYSpd(self):
        return self.__yspd

    def setXSpd(self, spd):
        self.__xspd = spd
        self.__speed = math.sqrt(self.__xspd**2 + self.__yspd**2)
        self.__direction = Util.point_direction(self.__xy, (self.__xspd, self.__yspd))

    def getXSpd(self):
        return self.__xspd

    def setSpeed(self, spd):
        self.__speed = spd
        (self.__xspd, self.__yspd) = Util.speedDir__xy(self.__speed, self.__direction)

    def getSpeed(self):
        return self.__speed

    def setSprite(self, spr):
        self.__sprite = Globals.sprites[spr]
        self.rect = self.__sprite[self.__index].get_rect()
        self.setHitRect(pygame.Rect(self.__xy[0] - 10, self.__xy[1] - 10, 20, 20)) #hitbox

    def getSprite(self):
        return self.__sprite

    def setDirection(self, d):
        self.__direction = d
        (self.__xspd, self.__yspd) = Util.speedDir__xy(self.__speed, self.__direction)

    def getDirection(self):
        return self.__direction

    def setDepth(self, d):
        self.__depth = d
        Groups.grp_AllSprites.change_layer(self, d)

    def keyUp(self, key):
        pass

    def keyDown(self, key):
        pass

    #add sprite spr to __drawList
    #Surface spr: the sprite to draw
    #int x: the absolute x position to draw spr
    #int y: the absolute y position to draw spr
    #int d: the relative depth to draw the new spr
    #int i: the index of spr to draw
    def drawSprite(self, spr, x, y, d, i):
        if not d in self.__drawList:
            self.__drawList[d] = []
        self.__drawList[d].append([spr, x, y, i])
        #self.__drawList.append([spr, x, y, d, i])

    def update(self):
        if self.__sprite != 0:
            self.drawSprite(self.__sprite, self.getX(), self.getY(), 0, self.__index)
            #tempSurface = pygame.Surface(self.__sprite[self.__index].get_size())
            #tempSurface is the size of the view
            tempSurface = pygame.Surface((Globals.window_w, Globals.window_h))
            tempSurface = tempSurface.convert()
            tempSurface.set_colorkey(0, RLEACCEL)
            #blit the current sprite onto tempSurface
            #tempSurface.blit(self.__sprite[self.__index], (self.getX() - Globals.view.getX(), self.getY() - Globals.view.getY()))
            #tempSurface.blit(self.__sprite[self.__index], (0, 0))
            for d in sorted(self.__drawList.iterkeys()):
                for spr in self.__drawList[d]:
                    tempSurface.blit(spr[0][spr[3] % len(spr[0])], (spr[1] - Globals.view.getX(), spr[2] - Globals.view.getY()))
            self.image = tempSurface
            #self.image = self.__sprite[self.__index]
            tempSurface = pygame.Surface((0, 0))
            self.__index = (self.__index + 1) % len(self.__sprite)

        self.__xy = Util.add2(self.__xy, (self.__xspd, self.__yspd))
        #self.rect.center = (self.__xy[0], self.__xy[1]) #move rect to xy
        self.rect.topleft = (Globals.view.getX(), Globals.view.getY()) #move rect to top left of the view
        self.__hitRect.center = self.__xy #move hitbox to xy
        #self.__drawList = dict({0:[self.__sprite, self.getX(), self.getY(), self.__index]}) #clear the __drawList every step
        self.__drawList = {}
