import pygame, sys, os
import math
import Globals
import Groups
from pygame.locals import *
import xml.sax

#returns a surface
def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'sprites', name)
    try:
        image = pygame.image.load(fullname) #load a surface
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert() #convert pixel format
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL) #the transparent color
    return image

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', wav
        raise SystemExit, message
    return sound

def loadSprite(name):
    numFiles = len(filter(lambda x: x[-4:] == '.bmp', os.listdir(os.path.join('data', 'sprites', name))))
    Globals.sprites[name] = [0] * numFiles
    for iLoop in range(numFiles):
        Globals.sprites[name][iLoop] = load_image(os.path.join(name, name + str(iLoop) + '.bmp'), -1)

#add
def add2((x1,y1), (x2,y2)):
    return (x1 + x2, y1 + y2)
    #return map(lambda (x, y): x + y, zip((x1, y1), (x2, y2)))

#def loadRoom(name):
#    roomFilePath = os.path.join('data', 'rooms', name) +'.xml'
#    roomFile = open(roomFilePath,'r')
#    roomData = roomFile.read()
#    roomFile.close()
#
#    #parse the xml you got from the file
#    dom = parseString(roomData)
#    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
#    for obj in dom.getElementsByTagName('object'):
#        print obj.toxml()
#    #xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')

#subtract
def sub2((x1,y1), (x2,y2)):
    return (x1 - x2, y1 - y2)
    #return map(lambda (x, y): x - y, zip((x1, y1), (x2, y2)))

#convert view coordinates to world coordinates
def view_to_world((x,y), view):
    return (x + view.getX(), y + view.getY())

#convert world coordinates to view coordinates
def world_to_view((x,y), view):
    return (x - view.getX(), y - view.getY())

#calculate x and y from given speed and direction
def speedDir_xy(s, d):
    return (math.sin(d * math.pi / 8) * s, -math.cos(d * math.pi / 8) * s)

#return direction from 1 to 2
def point_direction((x1, y1), (x2, y2)):
    return math.atan2(y2 - y1, x2 - x1) * 180 / math.pi

