import pygame, sys, os
from pygame.locals import *
import Globals
import GameObj

class View (GameObj.GameObj):
    def __init__(self, x, y):
        #(x,y) indicates the top-left corner of the view. obj is the object to follow
        super(View, self).__init__(x, y)

        self.__target = 0

    def follow(self, obj):
        self.__target = obj


    def update(self):
        if self.__target != 0:
            if self.__target.getX() > self.getX() + int(Globals.window_w * .75):
                self.setX(min(Globals.room_w - Globals.window_w, self.__target.getX() - int(Globals.window_w * .75)))
            elif self.__target.getX() < self.getX() + int(Globals.window_w * .25):
                self.setX(max(0, self.__target.getX() - int(Globals.window_w * .25)))

            if self.__target.getY() > self.getY() + int(Globals.window_h * .75):
                self.setY(min(Globals.room_h - Globals.window_h, self.__target.getY() - int(Globals.window_h * .75)))
            elif self.__target.getY() < self.getY() + int(Globals.window_h * .25):
                self.setY(max(0, self.__target.getY() - int(Globals.window_h * .25)))
