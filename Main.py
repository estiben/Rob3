#!/usr/bin/python
import pygame, sys, os
from pygame.locals import *
import xml.sax
import math
import Util
import Groups
import Globals
from View import View
from Rob import Rob
from Wall import Wall

class RoomSAXContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.paramList = []
        self.currentElement = ''
        self.currentClass = ''

    def startElement(self, name, attrs):
        self.currentElement = name
        if name == 'tile':
            print('tile')
        elif name == 'object':
            self.currentClass = attrs.getValue('class')
 
    def endElement(self, name):
        if name == 'object':
            evalString = self.currentClass + '(' + ','.join(self.paramList) + ')'
            eval(evalString)
            self.paramList = []
 
    def characters(self, content):
        if self.currentElement == 'param':
            self.paramList.append(content)
 
def loadRoom(name):
    roomFilePath = os.path.join('data', 'rooms', name) +'.xml'
    source = open(roomFilePath,'r')
    
    xml.sax.parse(source, RoomSAXContentHandler())
    source.close()
 
def main():
    while True:
        Globals.clock.tick(30)
        Globals.step = (Globals.step + 1) % 1000
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                else:
                    for x in Groups.grp_AllSprites:
                        x.keyDown(event.key)
            elif event.type == KEYUP:
                for x in Groups.grp_AllSprites:
                    x.keyUp(event.key)
            elif event.type == QUIT:
                return

        Groups.grp_AllSprites.update()
        Globals.view.update()

        #draw floor tiles
        for w in range(Globals.view.getX() - (Globals.view.getX() % 80), Globals.view.getX() + 720, 80):
            for h in range(Globals.view.getY() - (Globals.view.getY() % 80), Globals.view.getY() + 560, 80):
                Globals.baseSurface.blit(sprFloor, (w, h))

        #draw allsprites
        Groups.grp_AllSprites.draw(Globals.baseSurface)

        #draw grid
        #for i in range(0, 1000, Globals.cellSize):
        #    pygame.draw.line(Globals.baseSurface, pygame.Color(255,255,255,0), (0, i), (1000, i), 1)
        #    pygame.draw.line(Globals.baseSurface, pygame.Color(255,255,255,0), (i, 0), (i, 1000), 1)

#draw to view
        Globals.viewSurface.blit(Globals.baseSurface, (-Globals.view.getX(), -Globals.view.getY()))
        pygame.display.flip()

pygame.init()

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

#create the view surface
Globals.view = View(0, 0)

#initialize window to display
pygame.display.set_caption('ROB')

pygame.mouse.set_visible(0)

if pygame.font:
    font = pygame.font.Font(None, 36) #new font object
    text = font.render("m", 1, (10, 10, 10)) #returns the surface with text
    textpos = text.get_rect()
    textpos.centerx = Globals.baseSurface.get_rect().centerx
    Globals.baseSurface.blit(text, textpos)

#whiff_sound = load_sound('whiff.wav')
#punch_sound = load_sound('punch.wav')

#Load Sprites
Util.loadSprite('rob')
Util.loadSprite('wall_a')
Util.loadSprite('blades')
loadRoom('room1')

sprFloor = Util.load_image('floor_tile.bmp')

player = Rob(10, 10, 100)
#wall1 = Wall(15, 15)
#wall2 = Wall(20, 20)
#wall3 = Wall(25, 25)

Globals.view.follow(player)

main()
