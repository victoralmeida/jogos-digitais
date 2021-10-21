import pygame
from pygame.locals import *
from sys import exit
import random


branco = (255, 255, 255)
xr = 1200
yr = random.randint(0, 200)
xr2 = 1600
yr2 = random.randint(0, 200)
xr3 = 2000
yr3 = random.randint(0, 200)    

background_image_filename = 'Noite.png' 
correndo_image_filename = 'Correndo.png' 
pulando_image_filename = 'Pulando.png' 
inimigo1_image_filename = 'Inimigo1.png' 
inimigo2_image_filename = 'Inimigo2.png' 
bala_image_filename = 'Bala.png' 



pygame.init()

screen = pygame.display.set_mode((800, 380), 0, 32)
clock = pygame.time.Clock()
background = pygame.image.load(background_image_filename).convert()
background2 = pygame.image.load(background_image_filename).convert()
correndo = pygame.image.load(correndo_image_filename).convert()
pulando = pygame.image.load(pulando_image_filename).convert()
inimigo1 = pygame.image.load(inimigo1_image_filename).convert()
inimigo2 = pygame.image.load(inimigo2_image_filename).convert()
bala1 = pygame.image.load(bala_image_filename).convert()
bala2 = pygame.image.load(bala_image_filename).convert()
personagem = correndo


bx = 0
bx2 = 801
x = 0
y = 325
xi1 = 710
xi2 = 710
yi1 = 100
yi2 = y
xb1 = 700
xb2 = 700
yb1 = yi1
yb2 = yi2
subir = 0
z = 0
a = 4

while True:

    for event in pygame.event.get():        
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN and subir == 0:
            if event.key==K_SPACE:
                subir = 1
                personagem = pulando
            


    if subir == 1:
        y -= 10
        z += 1

    if z == 25:
        subir = 2

    if subir == 2:
        y += 10
        z -= 1

    if z == 0:
        subir = 0
        personagem = correndo     
    

    if bx < -800:
        bx = 800

    if bx2 < -800:
        bx2 = 800

    if xr < - 200:
        xr = 1000
        yr = random.randint(0, 300)

    if xr2 < - 200:
        xr2 = 1000
        yr2 = random.randint(0, 300)

    if xr3 < - 200:
        xr3 = 1000
        yr3 = random.randint(0, 300)

    if yi1 < 0:
        a = a * (-1)

    if yi1 > 300:
        a = a * (-1)

    if xb1 < -150:
        xb1 = 700
        yb1 = yi1 + 10 

    if xb2 < -150:
        xb2 = 700
        yb2 = yi2 + 10
        


    line_rect = Rect(xr,yr, 200, 50)
    line_rect2 = Rect(xr2,yr2, 200, 50)
    line_rect3 = Rect(xr3,yr3, 200, 50)    
    xr -= 5
    xr2 -= 5
    xr3 -= 5
    bx -= 5
    bx2 -= 5
    yi1 += a
    yi2 = y - 30
    xb1 -= 4
    xb2 -= 4
    clock.tick(60)
    screen.blit(background, (bx,0))
    screen.blit(background2, (bx2,0))
    screen.blit(personagem, (x,y))
    screen.blit(bala1, (xb1,yb1))
    screen.blit(bala2, (xb2,yb2))
    screen.blit(inimigo1, (xi1,yi1))
    screen.blit(inimigo2, (xi2,yi2))



    pygame.draw.rect(screen, branco, line_rect)
    pygame.draw.rect(screen, branco, line_rect2)
    pygame.draw.rect(screen, branco, line_rect3)
    pygame.display.update()
