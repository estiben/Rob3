import pygame, sys, os
from pygame.locals import *
import math
import Util
import Groups
import Globals
import GameObj

class Rob(GameObj.GameObj):
    def __init__(self, x, y, depth):
        super(Rob, self).__init__(x, y, depth)
        self.add(Groups.grp_Player)

        self.setSprite('rob')

        self.attacking = 0

    def keyDown(self, key):
        if key == K_DOWN:
            self.setYSpd(self.getYSpd() + 10)
        elif key == K_LEFT:
            self.setXSpd(self.getXSpd() - 10)
        elif key == K_UP:
            self.setYSpd(self.getYSpd() - 10)
        elif key == K_RIGHT:
            self.setXSpd(self.getXSpd() + 10)
        elif key == K_z:
            self.attack()

    def keyUp(self, key):
        if key == K_DOWN:
            self.setYSpd(self.getYSpd() - 10)
        elif key == K_LEFT:
            self.setXSpd(self.getXSpd() + 10)
        elif key == K_UP:
            self.setYSpd(self.getYSpd() + 10)
        elif key == K_RIGHT:
            self.setXSpd(self.getXSpd() - 10)

    def attack(self):
        if self.attacking == 0:
            self.attacking = 1

    def update(self):
        if self.attacking > 0:
            if self.attacking > 30:
                self.attacking = 0
            else:
                self.attacking += 1
                self.drawSprite(Globals.sprites['blades'], self.getX() - 15, self.getY() - 15, 0, self.attacking)
        super(Rob, self).update()
