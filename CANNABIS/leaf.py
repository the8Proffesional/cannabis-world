import pygame
from random import randint as ri


class Leaf(pygame.sprite.Sprite):
    def __init__(self, W=800, H=500):
        super().__init__()
        self.img=pygame.Surface((17,20))
        self.img.fill((200,55,25))
        self.scaling=ri(3,6)*0.45
        self.speed=ri(3,5)*0.35
        self.img.convert_alpha()
        self.img1=None
        self.rect=self.img.get_rect(topright=(ri(0,W-17),ri(-2*H,0)))
        self.spreadSheet=pygame.image.load('sprite.png').convert_alpha()
        self.framerowIndex=ri(0,13)
        self.img.blit(self.spreadSheet,(0,0),((0,self.framerowIndex*20),(17,20)))
        self.img.set_colorkey((200,55,25))
        
    def move(self, H=500):
        if self.rect.y < H+100:
            self.rect.y+=self.speed
        else:
            self.rect.y=0
            self.speed=ri(1,5)
        
    def draw(self, screen):
        self.img1=pygame.transform.scale(self.img,(17*self.scaling,20*self.scaling)).convert_alpha()
        screen.blit(self.img1,self.rect)
    
    def animate(self, screen):
        if self.framerowIndex<14:
            self.framerowIndex+=1
        else:
            self.framerowIndex=0
        self.img.fill((200,55,25)) 
        self.img.blit(self.spreadSheet,(0,0),((0,self.framerowIndex*20),(17,20)))
        self.draw(screen)