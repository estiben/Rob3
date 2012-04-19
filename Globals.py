import pygame, sys, os
from pygame.locals import *

room_w = 1000
room_h = 1000
window_w = 640
window_h = 480

step = 0

window = pygame.display.set_mode((window_w,window_h))

baseSurface = pygame.Surface((room_w, room_h))
baseSurface = baseSurface.convert()
viewSurface = pygame.display.get_surface() #the view surface

clock = pygame.time.Clock()

sprites = {}
