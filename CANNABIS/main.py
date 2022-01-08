from leaf import Leaf
import pygame
from pygame.time import Clock
W=800
H=500

pygame.init()
screen=pygame.display.set_mode((W, H))
pygame.display.set_caption('CANNABIS!')
clock=Clock()
bg=pygame.image.load('weed.png').convert_alpha()
#Sprite------------------------------------------
leafs=[]
for i in range(35):
    img = Leaf()
    leafs.append(img)
    
done=False
i=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    if i<8:
        i+=1
    else:
        i=0
    screen.blit(bg,(0,0))
    for i in range(35):
        leafs[i].animate(screen)
        leafs[i].move()
    
    pygame.display.update()
    clock.tick(38)
    
pygame.quit()
