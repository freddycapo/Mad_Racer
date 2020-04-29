import pygame
from pygame import *
from Car import Car
from Obstacle import Obstacle

width=900
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Mad Races")

background=pygame.image.load("Background.png")
car_sprite=pygame.image.load("images\car.png")

car=Car(width//2,height*0.80,100,100,5,width,height)
obstacles=[]

def RedrawScreen():
    screen.blit(background,(0,0),(width,height))

run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()