import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

display_surfase=pygame.display.set_mode((WIDTH,HEIGHT))#create a screen
pygame.display.set_caption("BULBONANDOFF")#this creates a title
img=pygame.image.load("lesson 4/image/bulb.png")
image=pygame.transform.scale(img, (WIDTH,HEIGHT))#this sets the image

while True:

    display_surfase.fill((255,255,255))#this adds white color
    display_surfase.blit(image,(0,0))#this adds image

    pygame.display.update()
    time.sleep(2)#this will pause screen for 2 seconds
    img2=pygame.image.load("lesson 4/image/bulbon.jpg")
    font=pygame.font.SysFont("BULB",38)

    display_surfase.fill((255,255,255))
    display_surfase.blit(img2,(0,0))

    pygame.display.update()
    time.sleep(2)