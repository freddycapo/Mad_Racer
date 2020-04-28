import pygame
from pygame import *
from Car import Car
from Obstacle import Obstacle

width=900
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Mad Races")

run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()