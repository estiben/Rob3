import pygame, sys, os
from pygame.locals import *
import GameObj
import Globals
import Groups

#<obj>
#<name>Wall</name>
#<params>(x, y)</params>
#<img>/home/steven/Projects/Rob3/data/sprites/wall_a/wall_a0.bmp</img>
#</obj>
class Wall(GameObj.GameObj):
    def __init__(self, x, y, depth):
        super(Wall, self).__init__(x, y, depth)
        self.add(Groups.grp_Solid)

        self.setSprite('wall_a')
