import pygame

class Car():
    def __init__(self,x,y,width,height,velx,WS,HS):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velx=velx
        self.WS=WS
        self.HS=HS

    def move(self):
        keys=pygame.key.get_pressed()
        